# Day 02: Threats, vulnerabilities, risk and controls

**Phase 1: Foundations and home lab** · Area: Foundations · Planned: 2026-11-10 · Time: 45 min

## Outcome

By the end of today you can: Define threat, vulnerability, exploit, risk and impact precisely, and classify controls by type and function.

## 1. Learn (15 min)

- ▶️ [Professor Messer playlist: 'Threat Actors' and 'Common Threat Vectors' videos](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv)
- [NIST SP 800-30 Rev. 1, Guide for Conducting Risk Assessments (skim chapter 2)](https://csrc.nist.gov/pubs/sp/800/30/r1/final)

## 2. Lab (25 min)

- [ ] Build a 5-row risk register for a CI/CD pipeline in a markdown table.
- [ ] Columns: asset, threat, vulnerability, likelihood (1-5), impact (1-5), risk score, control, control type (preventive/detective/corrective).
- [ ] Include at least one supply-chain risk (for example a compromised dependency) and one insider risk.

## 3. Explain it like an SME (5 min)

> What is the difference between a threat, a vulnerability and a risk? Give an example from a Kubernetes cluster.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

Your incident postmortems already reason about likelihood and impact. A risk register is that, written before the incident.

## Deliverable

- [ ] Commit: `notes/day-02.md with your risk register.`
- [ ] Update the Notion tracker row for Day 02 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 01](../week-01/day-01-the-security-mindset-cia-and-aaa.md) · [Roadmap](../../ROADMAP.md) · [Day 03 →](../week-01/day-03-security-frameworks-nist-csf-2-0-and-cis-controls.md)
