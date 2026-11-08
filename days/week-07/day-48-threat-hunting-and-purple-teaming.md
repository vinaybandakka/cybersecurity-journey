# Day 48: Threat hunting and purple teaming

**Phase 7: Defensive security operations** · Area: Defensive · Planned: 2026-12-26 · Time: 45 min

## Outcome

By the end of today you can: Run a hypothesis-driven hunt and test a detection with an Atomic Red Team test.

## 1. Learn (15 min)

- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- ▶️ [Black Hills Information Security (YouTube channel, webcasts on hunting)](https://www.youtube.com/@BlackHillsInformationSecurity)

## 2. Lab (25 min)

- [ ] Write a hunt hypothesis, for example 'an attacker added persistence via cron on a Linux host'.
- [ ] Simulate it in your Ubuntu container (add a cron job) using the matching Atomic test as a guide (T1053.003).
- [ ] Find it with commands or logs, then write a detection for it.

## 3. Explain it like an SME (5 min)

> What is the difference between detection and hunting, and how does purple teaming connect them?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-48-hunt.md`
- [ ] Update the Notion tracker row for Day 48 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 47](../week-07/day-47-malware-basics-threat-intelligence-and-yara.md) · [Roadmap](../../ROADMAP.md) · [Day 49 →](../week-07/day-49-week-7-review-and-tabletop-exercise.md)
