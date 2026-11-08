# Day 44: Detection engineering with Sigma

**Phase 7: Defensive security operations** · Area: Defensive · Planned: 2026-12-22 · Time: 45 min

## Outcome

By the end of today you can: Write a Sigma rule, convert it to a SIEM query and treat detections as code.

## 1. Learn (15 min)

- [Sigma rules repository](https://github.com/SigmaHQ/sigma)
- [Sigma documentation: rules](https://sigmahq.io/docs/basics/rules.html)
- [sigma-cli](https://github.com/SigmaHQ/sigma-cli)

## 2. Lab (25 min)

- [ ] Write a Sigma rule that detects 10 failed SSH logins from one IP in 5 minutes.
- [ ] Install sigma-cli with pip and convert your rule and one rule from the repo to a backend query.
- [ ] Add the rule to detections/ and describe how you would unit test it in CI.

## 3. Explain it like an SME (5 min)

> What makes a detection good? Talk about true positives, false positives, coverage and maintenance.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

Detection-as-code is GitOps for the SOC. Linting, tests and CI for rules is a skill many SOCs lack.

## Deliverable

- [ ] Commit: `detections/ssh-bruteforce.yml`
- [ ] Update the Notion tracker row for Day 44 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 43](../week-07/day-43-security-logging-and-siem-fundamentals.md) · [Roadmap](../../ROADMAP.md) · [Day 45 →](../week-07/day-45-incident-response-lifecycle.md)
