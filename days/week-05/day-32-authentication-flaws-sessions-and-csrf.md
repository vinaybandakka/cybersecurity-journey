# Day 32: Authentication flaws, sessions and CSRF

**Phase 5: Web and API security** · Area: Web · Planned: 2026-12-10 · Time: 45 min

## Outcome

By the end of today you can: Attack weak login and session handling in labs and explain CSRF and its defences.

## 1. Learn (15 min)

- [PortSwigger Web Security Academy: Authentication vulnerabilities](https://portswigger.net/web-security/authentication)
- [PortSwigger Web Security Academy: CSRF](https://portswigger.net/web-security/csrf)
- ▶️ [PwnFunction: Cross-Site Request Forgery (CSRF) Explained (YouTube)](https://www.youtube.com/watch?v=eWEgUcHPle0)

## 2. Lab (25 min)

- [ ] Solve the username enumeration via different responses lab.
- [ ] Solve the CSRF vulnerability with no defences lab.
- [ ] Note how SameSite=Lax cookies change the CSRF picture.

## 3. Explain it like an SME (5 min)

> How do SameSite cookies, CSRF tokens and re-authentication each reduce CSRF risk?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `labs/writeups/portswigger-auth-csrf.md`
- [ ] Update the Notion tracker row for Day 32 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 31](../week-05/day-31-broken-access-control-and-idor.md) · [Roadmap](../../ROADMAP.md) · [Day 33 →](../week-05/day-33-ssrf-command-injection-and-path-traversal.md)
