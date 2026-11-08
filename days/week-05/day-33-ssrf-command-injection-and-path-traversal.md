# Day 33: SSRF, command injection and path traversal

**Phase 5: Web and API security** · Area: Web · Planned: 2026-12-11 · Time: 45 min

## Outcome

By the end of today you can: Exploit server-side injection classes in labs and explain why SSRF is critical in the cloud.

## 1. Learn (15 min)

- [PortSwigger Web Security Academy: SSRF](https://portswigger.net/web-security/ssrf)
- [PortSwigger Web Security Academy: OS command injection](https://portswigger.net/web-security/os-command-injection)
- [PortSwigger Web Security Academy: Path traversal](https://portswigger.net/web-security/file-path-traversal)

## 2. Lab (25 min)

- [ ] Solve one apprentice lab in each of SSRF, OS command injection and path traversal.
- [ ] Read about how SSRF to the cloud metadata endpoint (169.254.169.254) leads to stolen IAM credentials.
- [ ] Write why IMDSv2 (session tokens, hop limit) mitigates it.

## 3. Explain it like an SME (5 min)

> Walk through how an SSRF bug can turn into a full AWS account compromise, and the three controls that break the chain.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

You know instance profiles and IMDS from the infrastructure side. This is the attacker's view of them.

## Deliverable

- [ ] Commit: `labs/writeups/portswigger-server-side.md`
- [ ] Update the Notion tracker row for Day 33 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 32](../week-05/day-32-authentication-flaws-sessions-and-csrf.md) · [Roadmap](../../ROADMAP.md) · [Day 34 →](../week-05/day-34-api-security.md)
