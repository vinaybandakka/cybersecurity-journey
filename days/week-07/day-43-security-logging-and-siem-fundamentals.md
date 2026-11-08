# Day 43: Security logging and SIEM fundamentals

**Phase 7: Defensive security operations** · Area: Defensive · Planned: 2026-12-21 · Time: 45 min

## Outcome

By the end of today you can: Explain what to log, how a SIEM normalises and correlates data, and investigate raw logs.

## 1. Learn (15 min)

- [TryHackMe: Introduction to SIEM (room)](https://tryhackme.com/room/introtosiem)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

## 2. Lab (25 min)

- [ ] Export the Juice Shop container logs and your Ubuntu auth.log from earlier labs.
- [ ] Using grep, awk and jq, answer which IP made the most failed logins and when the first suspicious request happened.
- [ ] Write which fields a good security log must have (who, what, when, where, outcome).

## 3. Explain it like an SME (5 min)

> Logging everything is expensive. How do you decide what goes into the SIEM?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

You built observability stacks. A SIEM is observability with an adversary in the threat model.

## Deliverable

- [ ] Commit: `notes/day-43.md`
- [ ] Update the Notion tracker row for Day 43 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 42](../week-06/day-42-week-6-review-and-mini-pentest-report.md) · [Roadmap](../../ROADMAP.md) · [Day 44 →](../week-07/day-44-detection-engineering-with-sigma.md)
