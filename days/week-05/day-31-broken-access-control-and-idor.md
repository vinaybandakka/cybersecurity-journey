# Day 31: Broken access control and IDOR

**Phase 5: Web and API security** · Area: Web · Planned: 2026-12-09 · Time: 45 min

## Outcome

By the end of today you can: Find horizontal and vertical privilege escalation and explain server-side authorization checks.

## 1. Learn (15 min)

- [PortSwigger Web Security Academy: Access control vulnerabilities](https://portswigger.net/web-security/access-control)
- [OWASP Top 10: A01 Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/)

## 2. Lab (25 min)

- [ ] Solve two access control apprentice labs (unprotected admin, user ID in request parameter).
- [ ] In Juice Shop, view another user's basket by changing an ID in Burp.
- [ ] Write the code-level fix (check ownership on the server for every object access).

## 3. Explain it like an SME (5 min)

> Why has broken access control been the number one OWASP risk, and why can scanners rarely find it?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `labs/writeups/portswigger-access-control.md`
- [ ] Update the Notion tracker row for Day 31 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 30](../week-05/day-30-cross-site-scripting-xss.md) · [Roadmap](../../ROADMAP.md) · [Day 32 →](../week-05/day-32-authentication-flaws-sessions-and-csrf.md)
