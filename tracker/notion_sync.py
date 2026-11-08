#!/usr/bin/env python3
"""Sync the 60-day tracker with a Notion database.

    push  create the database (first run) and create or update one row per day from notion-tracker.csv.
          Your own progress fields (Status, Done, Confidence, Minutes, Notes) are never overwritten.
    pull  download your progress from Notion into tracker/progress.csv, so the repo has a record too.

Setup (once): see tracker/NOTION_SETUP.md, then

    export NOTION_TOKEN=ntn_...            # internal integration secret
    export NOTION_PARENT_PAGE_ID=...       # page the database is created under (first push only)
    python3 tracker/notion_sync.py push    # prints NOTION_DATABASE_ID; export it for later runs
    python3 tracker/notion_sync.py pull

Only needs the `requests` package.
"""
from __future__ import annotations

import csv
import os
import sys
import time
from pathlib import Path

import requests

API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "notion-tracker.csv"
PROGRESS_PATH = HERE / "progress.csv"

STATUS_OPTIONS = [("Not started", "gray"), ("In progress", "blue"), ("Done", "green"), ("Skipped", "red")]
# Fields that belong to you. push sets them only when it creates a row.
USER_FIELDS = {"Status", "Done", "Confidence", "Minutes", "Notes"}


def session() -> requests.Session:
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        sys.exit("Set NOTION_TOKEN first (see tracker/NOTION_SETUP.md).")
    s = requests.Session()
    s.headers.update({"Authorization": f"Bearer {token}", "Notion-Version": NOTION_VERSION,
                      "Content-Type": "application/json"})
    return s


def call(s: requests.Session, method: str, path: str, **kw) -> dict:
    for attempt in range(5):
        r = s.request(method, f"{API}{path}", timeout=30, **kw)
        if r.status_code == 429:  # Notion allows about 3 requests per second
            time.sleep(float(r.headers.get("Retry-After", 1 + attempt)))
            continue
        if r.status_code >= 400:
            sys.exit(f"Notion API {r.status_code} on {path}: {r.text}")
        return r.json()
    sys.exit("Notion API kept rate limiting; try again in a minute.")


def text(value: str) -> list[dict]:
    return [{"type": "text", "text": {"content": value[:2000]}}] if value else []


def schema(phases: list[str], areas: list[str]) -> dict:
    return {
        "Name": {"title": {}},
        "Day": {"number": {"format": "number"}},
        "Week": {"number": {"format": "number"}},
        "Phase": {"select": {"options": [{"name": p} for p in phases]}},
        "Area": {"select": {"options": [{"name": a} for a in areas]}},
        "Planned Date": {"date": {}},
        "Status": {"select": {"options": [{"name": n, "color": c} for n, c in STATUS_OPTIONS]}},
        "Done": {"checkbox": {}},
        "Confidence": {"number": {"format": "number"}},
        "Minutes": {"number": {"format": "number"}},
        "Outcome": {"rich_text": {}},
        "Lab": {"rich_text": {}},
        "SME Question": {"rich_text": {}},
        "Deliverable": {"rich_text": {}},
        "Resources": {"rich_text": {}},
        "Day Page": {"url": {}},
        "Notes": {"rich_text": {}},
    }


def props(row: dict, include_user_fields: bool) -> dict:
    p = {
        "Name": {"title": text(row["Name"])},
        "Day": {"number": int(row["Day"])},
        "Week": {"number": int(row["Week"])},
        "Phase": {"select": {"name": row["Phase"]}},
        "Area": {"select": {"name": row["Area"]}},
        "Planned Date": {"date": {"start": row["Planned Date"]}},
        "Outcome": {"rich_text": text(row["Outcome"])},
        "Lab": {"rich_text": text(row["Lab"])},
        "SME Question": {"rich_text": text(row["SME Question"])},
        "Deliverable": {"rich_text": text(row["Deliverable"])},
        "Resources": {"rich_text": text(row["Resources"])},
        "Day Page": {"url": row["Day Page"]},
    }
    if include_user_fields:
        p["Status"] = {"select": {"name": row["Status"] or "Not started"}}
        p["Done"] = {"checkbox": row["Done"].lower() in {"yes", "true", "1"}}
        if row["Confidence"]:
            p["Confidence"] = {"number": float(row["Confidence"])}
        if row["Minutes"]:
            p["Minutes"] = {"number": float(row["Minutes"])}
        p["Notes"] = {"rich_text": text(row["Notes"])}
    return p


def all_pages(s: requests.Session, db: str) -> list[dict]:
    pages, cursor = [], None
    while True:
        body = {"page_size": 100, **({"start_cursor": cursor} if cursor else {})}
        res = call(s, "POST", f"/databases/{db}/query", json=body)
        pages += res["results"]
        if not res.get("has_more"):
            return pages
        cursor = res["next_cursor"]


def push() -> None:
    s = session()
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    db = os.environ.get("NOTION_DATABASE_ID")
    if not db:
        parent = os.environ.get("NOTION_PARENT_PAGE_ID")
        if not parent:
            sys.exit("Set NOTION_PARENT_PAGE_ID (first run) or NOTION_DATABASE_ID (later runs).")
        phases = list(dict.fromkeys(r["Phase"] for r in rows))
        areas = list(dict.fromkeys(r["Area"] for r in rows))
        res = call(s, "POST", "/databases", json={
            "parent": {"type": "page_id", "page_id": parent},
            "title": text("Cybersecurity 60-day tracker"),
            "properties": schema(phases, areas),
        })
        db = res["id"]
        print(f"Created database {res.get('url', db)}")
        print(f"export NOTION_DATABASE_ID={db}")
    existing = {int(p["properties"]["Day"]["number"]): p["id"]
                for p in all_pages(s, db) if p["properties"].get("Day", {}).get("number") is not None}
    created = updated = 0
    for row in rows:
        day = int(row["Day"])
        if day in existing:
            call(s, "PATCH", f"/pages/{existing[day]}", json={"properties": props(row, False)})
            updated += 1
        else:
            call(s, "POST", "/pages", json={"parent": {"database_id": db}, "properties": props(row, True)})
            created += 1
    print(f"Done: {created} rows created, {updated} rows updated (your progress fields were left alone).")


def plain(prop: dict) -> str:
    kind = prop.get("type")
    v = prop.get(kind)
    if kind in {"title", "rich_text"}:
        return "".join(t.get("plain_text", "") for t in v or [])
    if kind == "select":
        return (v or {}).get("name", "")
    if kind == "checkbox":
        return "Yes" if v else "No"
    if kind == "number":
        return "" if v is None else (str(int(v)) if float(v).is_integer() else str(v))
    if kind == "date":
        return (v or {}).get("start", "")
    if kind == "url":
        return v or ""
    return ""


def pull() -> None:
    s = session()
    db = os.environ.get("NOTION_DATABASE_ID") or sys.exit("Set NOTION_DATABASE_ID.")
    pages = all_pages(s, db)
    fields = ["Day", "Name", "Planned Date", "Status", "Done", "Confidence", "Minutes", "Notes"]
    out = []
    for p in pages:
        pr = p["properties"]
        out.append({f: plain(pr[f]) for f in fields if f in pr})
    out.sort(key=lambda r: int(r.get("Day") or 0))
    with PROGRESS_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    done = sum(1 for r in out if r.get("Done") == "Yes" or r.get("Status") == "Done")
    print(f"Wrote {PROGRESS_PATH.relative_to(HERE.parent)}: {done}/{len(out)} days done.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    {"push": push, "pull": pull}.get(cmd, lambda: sys.exit(__doc__))()
