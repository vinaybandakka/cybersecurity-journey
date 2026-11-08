# Day 25: Secrets management and crypto failures

**Phase 4: Cryptography, PKI and web basics** · Area: Cryptography · Planned: 2026-12-03 · Time: 45 min

## Outcome

By the end of today you can: Explain why secrets leak, how to rotate them, and run a secrets manager and a secrets scanner.

## 1. Learn (15 min)

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [HashiCorp Vault documentation](https://developer.hashicorp.com/vault/docs)

## 2. Lab (25 min)

- [ ] Run Vault in dev mode: `docker run --rm -p 8200:8200 hashicorp/vault`, then write and read a KV secret.
- [ ] Make a scratch git repo, commit a fake AWS key, delete it in a second commit, then run gitleaks and find it.
- [ ] Write the 4-step response to a real leaked key (revoke, rotate, investigate usage, prevent).

## 3. Explain it like an SME (5 min)

> Why is deleting a leaked secret from git not enough?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

You have wired secrets into pipelines. Now ask what happens when one leaks and how fast you can rotate.

## Deliverable

- [ ] Commit: `notes/day-25.md`
- [ ] Update the Notion tracker row for Day 25 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 24](../week-04/day-24-pki-and-tls.md) · [Roadmap](../../ROADMAP.md) · [Day 26 →](../week-04/day-26-browser-security-model-and-security-headers.md)
