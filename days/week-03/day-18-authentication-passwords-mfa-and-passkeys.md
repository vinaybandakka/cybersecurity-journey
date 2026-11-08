# Day 18: Authentication, passwords, MFA and passkeys

**Phase 3: Systems and identity** · Area: Identity · Planned: 2026-11-26 · Time: 45 min

## Outcome

By the end of today you can: Explain modern password guidance, how passwords should be stored, and why phishing-resistant MFA matters.

## 1. Learn (15 min)

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- ▶️ [Computerphile: How NOT to Store Passwords! (YouTube)](https://www.youtube.com/watch?v=8ZtInClXe1Q)
- [FIDO Alliance: passkeys](https://fidoalliance.org/passkeys/)

## 2. Lab (25 min)

- [ ] Create 5 test passwords of your own (weak and strong), hash them with MD5 and bcrypt using Python.
- [ ] Crack the MD5 ones with hashcat or john and a small wordlist, then try the bcrypt ones and time it.
- [ ] Write down why salting and slow hashes changed the outcome.

## 3. Explain it like an SME (5 min)

> Why are SMS codes weaker than passkeys, and what is MFA fatigue?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-18.md with your timings.`
- [ ] Update the Notion tracker row for Day 18 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 17](../week-03/day-17-active-directory-and-kerberos-basics.md) · [Roadmap](../../ROADMAP.md) · [Day 19 →](../week-03/day-19-authorization-iam-and-least-privilege.md)
