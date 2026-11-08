# Day 41: Phishing, email security and password attacks

**Phase 6: Offensive security and vulnerability management** · Area: Offensive · Planned: 2026-12-19 · Time: 45 min

## Outcome

By the end of today you can: Analyse a phishing email and explain SPF, DKIM, DMARC, password spraying and credential stuffing.

## 1. Learn (15 min)

- [Cloudflare Learning: DMARC, DKIM and SPF](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/)
- [OWASP: Credential stuffing](https://owasp.org/www-community/attacks/Credential_stuffing)

## 2. Lab (25 min)

- [ ] `dig TXT gmail.com`, `dig TXT _dmarc.gmail.com` and explain each record.
- [ ] Open the raw headers of a spam email in your own inbox and trace the Received chain and auth results.
- [ ] Write the red flags and the verdict like a SOC analyst would.

## 3. Explain it like an SME (5 min)

> Why does DMARC with p=reject matter, and why can phishing still land in inboxes?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-41.md`
- [ ] Update the Notion tracker row for Day 41 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 40](../week-06/day-40-linux-privilege-escalation.md) · [Roadmap](../../ROADMAP.md) · [Day 42 →](../week-06/day-42-week-6-review-and-mini-pentest-report.md)
