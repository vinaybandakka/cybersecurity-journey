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
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "roadmap.svg").write_text(render_svg(phases, days))
    print(f"Wrote {len(days)} day pages, ROADMAP.md, PROGRESS.md and {tracker.relative_to(ROOT)}")


# One colour pair (accent, light tint) per phase.
PHASE_COLOURS = [
    ("#2563eb", "#eff6ff"), ("#0891b2", "#ecfeff"), ("#7c3aed", "#f5f3ff"),
    ("#c026d3", "#fdf4ff"), ("#dc2626", "#fef2f2"), ("#ea580c", "#fff7ed"),
    ("#16a34a", "#f0fdf4"), ("#0d9488", "#f0fdfa"), ("#475569", "#f8fafc"),
]


def render_svg(phases: list[dict], days: list[dict]) -> str:
    """One-page picture of the whole plan: a row per phase, a card per day."""
    import textwrap
    from xml.sax.saxutils import escape

    card_w, card_h, gap = 186, 70, 10
    label_w, margin, top = 270, 24, 118
    row_h = card_h + 26
    width = margin * 2 + label_w + 7 * (card_w + gap) - gap
    height = top + row_h * len(phases) + 64
    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif">',
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'<text x="{margin}" y="46" font-size="28" font-weight="700" fill="#0f172a">DevOps to Security: 60-day fundamentals roadmap</text>',
        f'<text x="{margin}" y="76" font-size="15" fill="#475569">45 minutes a day: 15 min learn, 25 min lab, 5 min explain like an SME. '
        'Every 7th day is a review checkpoint.</text>',
        f'<text x="{margin}" y="100" font-size="13" fill="#64748b">▶ = has a YouTube video   ★ = review and checkpoint day   '
        '◆ = DevOps bridge (your background helps)</text>',
    ]
    for i, p in enumerate(phases):
        accent, tint = PHASE_COLOURS[i % len(PHASE_COLOURS)]
        y = top + i * row_h
        o.append(f'<rect x="{margin}" y="{y}" width="{width - 2 * margin}" height="{card_h + 14}" rx="12" fill="{tint}"/>')
        o.append(f'<rect x="{margin}" y="{y}" width="6" height="{card_h + 14}" rx="3" fill="{accent}"/>')
        o.append(f'<text x="{margin + 18}" y="{y + 24}" font-size="12" font-weight="700" fill="{accent}" letter-spacing="0.5">'
                 f'PHASE {p["id"]} · WEEK {i + 1} · DAYS {p["days"][0]}-{p["days"][1]}</text>')
        for j, line in enumerate(textwrap.wrap(p["name"], 26)[:2]):
            o.append(f'<text x="{margin + 18}" y="{y + 46 + j * 19}" font-size="16" font-weight="700" fill="#0f172a">{escape(line)}</text>')
        phase_days = [d for d in days if p["days"][0] <= d["day"] <= p["days"][1]]
        for k, d in enumerate(phase_days):
            x = margin + label_w + k * (card_w + gap)
            cy = y + 7
            review = d["area"] == "Review"
            dash = ' stroke-dasharray="5 4"' if review else ""
            o.append(f'<rect x="{x}" y="{cy}" width="{card_w}" height="{card_h}" rx="9" fill="#ffffff" stroke="{accent}" stroke-width="1.5"{dash}/>')
            marks = ("▶" if any(is_youtube(r["u"]) for r in d["learn"]) else "") + ("◆" if d.get("bridge") else "") + ("★" if review else "")
            o.append(f'<text x="{x + 10}" y="{cy + 18}" font-size="11" font-weight="700" fill="{accent}">DAY {d["day"]:02d}</text>')
            if marks:
                o.append(f'<text x="{x + card_w - 10}" y="{cy + 18}" font-size="11" text-anchor="end" fill="{accent}">{marks}</text>')
            for j, line in enumerate(textwrap.wrap(d["title"], 27)[:3]):
                o.append(f'<text x="{x + 10}" y="{cy + 35 + j * 14}" font-size="11.5" fill="#1e293b">{escape(line)}</text>')
    o.append(f'<text x="{margin}" y="{height - 24}" font-size="12" fill="#94a3b8">Generated from data/curriculum.yaml by scripts/generate.py · '
             'github.com/vinaybandakka/cybersecurity-journey</text>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


def render_roadmap(phases: list[dict], days: list[dict], dates: list[dt.date]) -> str:
    total_hours = len(days) * 45 / 60
    out = [
        "# 60-day security fundamentals roadmap",
        "",
        "![The whole 60-day roadmap on one page: nine phases, one card per day](assets/roadmap.svg)",
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
