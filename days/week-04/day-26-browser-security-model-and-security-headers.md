# Day 26: Browser security model and security headers

**Phase 4: Cryptography, PKI and web basics** · Area: Web · Planned: 2026-12-04 · Time: 45 min

## Outcome

By the end of today you can: Explain same-origin policy, CORS, cookie flags and the main security headers.

## 1. Learn (15 min)

- [MDN: Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)
- [MDN: Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [MDN HTTP Observatory](https://developer.mozilla.org/en-US/observatory)

## 2. Lab (25 min)

- [ ] Scan two public sites with the HTTP Observatory and compare grades.
- [ ] In browser dev tools, inspect cookies on a site and note Secure, HttpOnly and SameSite.
- [ ] Write the header set you would ship by default (CSP, HSTS, X-Content-Type-Options, frame-ancestors, Referrer-Policy).

## 3. Explain it like an SME (5 min)

> CORS is not a security control that protects your server. Explain why.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

These headers usually live in ingress or CDN config, which is your territory.

## Deliverable

- [ ] Commit: `notes/day-26.md`
- [ ] Update the Notion tracker row for Day 26 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 25](../week-04/day-25-secrets-management-and-crypto-failures.md) · [Roadmap](../../ROADMAP.md) · [Day 27 →](../week-04/day-27-owasp-top-10-overview-and-burp-suite.md)
