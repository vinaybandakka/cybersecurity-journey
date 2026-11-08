#!/usr/bin/env python3
"""Generate the daily pages, the Notion tracker CSV and PROGRESS.md from data/curriculum.yaml.

Usage:
    python3 scripts/generate.py                     # planned dates start 2026-11-09
    python3 scripts/generate.py --start 2026-12-01  # pick your own start date
    python3 scripts/generate.py --weekends-off      # plan 5 study days per week

Requires PyYAML (pip install pyyaml).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/vinaybandakka/cybersecurity-journey/blob/main"
DEFAULT_START = "2026-11-09"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:50].rstrip("-")


def phase_for(day: int, phases: list[dict]) -> dict:
    for p in phases:
        if p["days"][0] <= day <= p["days"][1]:
            return p
    raise ValueError(f"day {day} has no phase")


def planned_dates(start: dt.date, n: int, weekends_off: bool) -> list[dt.date]:
    dates, d = [], start
    while len(dates) < n:
        if not (weekends_off and d.weekday() >= 5):
            dates.append(d)
        d += dt.timedelta(days=1)
    return dates


def is_youtube(url: str) -> bool:
    return "youtube.com" in url or "youtu.be" in url


def day_path(d: dict) -> Path:
    week = (d["day"] - 1) // 7 + 1
    return Path("days") / f"week-{week:02d}" / f"day-{d['day']:02d}-{slug(d['title'])}.md"


def render_day(d: dict, phase: dict, date: dt.date, prev: dict | None, nxt: dict | None) -> str:
    lines = [
        f"# Day {d['day']:02d}: {d['title']}",
        "",
        f"**Phase {phase['id']}: {phase['name']}** · Area: {d['area']} · Planned: {date.isoformat()} · Time: 45 min",
        "",
        "## Outcome",
        "",
        f"By the end of today you can: {d['outcome']}",
        "",
        "## 1. Learn (15 min)",
        "",
    ]
    for r in d["learn"]:
        icon = "▶️ " if is_youtube(r["u"]) else ""
        lines.append(f"- {icon}[{r['t']}]({r['u']})")
    lines += ["", "## 2. Lab (25 min)", ""]
    for step in d["lab"]:
        lines.append(f"- [ ] {step}")
    lines += ["", "## 3. Explain it like an SME (5 min)", "", f"> {d['explain']}", "",
              "Answer out loud first, then write a 3 to 5 sentence answer in your notes."]
    if d.get("bridge"):
        lines += ["", "## DevOps bridge", "", d["bridge"]]
    lines += [
        "",
        "## Deliverable",
        "",
        f"- [ ] Commit: `{d['deliverable']}`",
        f"- [ ] Update the Notion tracker row for Day {d['day']:02d} (Status, Confidence 1-5, Minutes, Notes)",
        "",
        "---",
        "",
    ]
    nav = []
    if prev:
        nav.append(f"[← Day {prev['day']:02d}](../{day_path(prev).parent.name}/{day_path(prev).name})")
    nav.append("[Roadmap](../../ROADMAP.md)")
    if nxt:
        nav.append(f"[Day {nxt['day']:02d} →](../{day_path(nxt).parent.name}/{day_path(nxt).name})")
    lines.append(" · ".join(nav))
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=DEFAULT_START, help="first study day, YYYY-MM-DD")
    ap.add_argument("--weekends-off", action="store_true", help="skip Saturdays and Sundays")
    args = ap.parse_args()

    data = yaml.safe_load((ROOT / "data" / "curriculum.yaml").read_text())
    phases, days = data["phases"], data["days"]
    assert [d["day"] for d in days] == list(range(1, len(days) + 1)), "days must be 1..N in order"
    dates = planned_dates(dt.date.fromisoformat(args.start), len(days), args.weekends_off)

    out_days = ROOT / "days"
    if out_days.exists():
        shutil.rmtree(out_days)

    rows = []
    for i, d in enumerate(days):
        phase = phase_for(d["day"], phases)
        rel = day_path(d)
        (ROOT / rel).parent.mkdir(parents=True, exist_ok=True)
        prev = days[i - 1] if i > 0 else None
        nxt = days[i + 1] if i + 1 < len(days) else None
        (ROOT / rel).write_text(render_day(d, phase, dates[i], prev, nxt))
        rows.append({
            "Name": f"Day {d['day']:02d}: {d['title']}",
            "Day": d["day"],
            "Week": (d["day"] - 1) // 7 + 1,
            "Phase": f"{phase['id']}. {phase['name']}",
            "Area": d["area"],
            "Planned Date": dates[i].isoformat(),
            "Status": "Not started",
            "Done": "No",
            "Confidence": "",
            "Minutes": "",
            "Outcome": d["outcome"],
            "Lab": " | ".join(d["lab"]),
            "SME Question": d["explain"],
            "Deliverable": d["deliverable"],
            "Resources": " ".join(r["u"] for r in d["learn"]),
            "Day Page": f"{REPO_URL}/{rel.as_posix()}",
            "Notes": "",
        })

    tracker = ROOT / "tracker" / "notion-tracker.csv"
    tracker.parent.mkdir(exist_ok=True)
    with tracker.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # PROGRESS.md: a git-native checklist, for days you want to tick off in the repo too.
    prog = ["# Progress", "",
            "Tick a box when the day's deliverable is committed. Notion holds the richer tracking (confidence, minutes, notes).",
            ""]
    for p in phases:
        prog += [f"## Phase {p['id']}: {p['name']} (days {p['days'][0]}-{p['days'][1]})", "", f"_{p['goal']}_", ""]
        for i, d in enumerate(days):
            if p["days"][0] <= d["day"] <= p["days"][1]:
                prog.append(f"- [ ] [Day {d['day']:02d}: {d['title']}]({day_path(d).as_posix()}) · {dates[i].isoformat()}")
        prog.append("")
    (ROOT / "PROGRESS.md").write_text("\n".join(prog))

    (ROOT / "ROADMAP.md").write_text(render_roadmap(phases, days, dates))
    print(f"Wrote {len(days)} day pages, ROADMAP.md, PROGRESS.md and {tracker.relative_to(ROOT)}")


def render_roadmap(phases: list[dict], days: list[dict], dates: list[dt.date]) -> str:
    total_hours = len(days) * 45 / 60
    out = [
        "# 60-day security fundamentals roadmap",
        "",
        f"{len(days)} days × 45 minutes = {total_hours:.0f} focused hours. Every day follows the same rhythm:",
        "",
        "| Block | Minutes | What you do |",
        "|---|---|---|",
        "| Learn | 15 | One video or reading from the day page. Take notes in your own words. |",
        "| Lab | 25 | Hands-on work in your lab or on a free platform. Always produces evidence. |",
        "| Explain | 5 | Answer the SME question out loud, then write 3 to 5 sentences. |",
        "",
        "Every seventh day is a review and checkpoint against [sme/INTERVIEW_QUESTIONS.md](sme/INTERVIEW_QUESTIONS.md).",
        "",
        "## Phases at a glance",
        "",
        "| Phase | Days | Focus | Milestone |",
        "|---|---|---|---|",
    ]
    for p in phases:
        out.append(f"| {p['id']}. {p['name']} | {p['days'][0]}-{p['days'][1]} | {p['goal']} | {p['milestone']} |")
    for p in phases:
        out += ["", f"## Phase {p['id']}: {p['name']} (days {p['days'][0]}-{p['days'][1]})", "",
                f"**Goal:** {p['goal']}", "",
                "**Topics:** " + ", ".join(p["topics"]) + ".", "",
                f"**Milestone:** {p['milestone']}", "",
                "| Day | Topic | You will be able to | Key resource |",
                "|---|---|---|---|"]
        for i, d in enumerate(days):
            if p["days"][0] <= d["day"] <= p["days"][1]:
                r = d["learn"][0]
                icon = "▶️ " if is_youtube(r["u"]) else ""
                out.append(f"| [{d['day']:02d}]({day_path(d).as_posix()}) | {d['title']} | {d['outcome']} | {icon}[link]({r['u']}) |")
    out += ["", "## After day 60", "",
            "See [resources/RESOURCES.md](resources/RESOURCES.md) for certifications and specialisation paths, "
            "and write your plan on day 60.", ""]
    return "\n".join(out)


if __name__ == "__main__":
    main()
