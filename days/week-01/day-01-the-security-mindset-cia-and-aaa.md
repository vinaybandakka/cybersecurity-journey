# Day 01: The security mindset, CIA and AAA

**Phase 1: Foundations and home lab** · Area: Foundations · Planned: 2026-11-09 · Time: 45 min

## Outcome

By the end of today you can: Explain confidentiality, integrity, availability, authentication, authorization and accounting with a real example of each.

## 1. Learn (15 min)

- ▶️ [Professor Messer SY0-701 course (YouTube playlist): watch 'Security Controls' and 'The CIA Triad'](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv)
- [NIST CSRC glossary (look up: confidentiality, integrity, availability, non-repudiation)](https://csrc.nist.gov/glossary)

## 2. Lab (25 min)

- [ ] Clone this repo and create notes/day-01.md from notes/TEMPLATE.md.
- [ ] Pick a system you ran in DevOps (for example a CI server or a production API).
- [ ] For that system write one way an attacker could break C, I and A, and one control that stops each.
- [ ] Add which AAA control is in place today (SSO? audit logs?) and which is missing.

## 3. Explain it like an SME (5 min)

> A product manager asks: 'We encrypt everything, so we are secure, right?' Answer in 60 seconds using CIA.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

Availability is SRE territory you already own. Security adds confidentiality and integrity to the same thinking.

## Deliverable

- [ ] Commit: `notes/day-01.md with your CIA/AAA table.`
- [ ] Update the Notion tracker row for Day 01 (Status, Confidence 1-5, Minutes, Notes)

---

[Roadmap](../../ROADMAP.md) · [Day 02 →](../week-01/day-02-threats-vulnerabilities-risk-and-controls.md)
