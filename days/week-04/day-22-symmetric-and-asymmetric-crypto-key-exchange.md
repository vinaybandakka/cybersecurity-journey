# Day 22: Symmetric and asymmetric crypto, key exchange

**Phase 4: Cryptography, PKI and web basics** · Area: Cryptography · Planned: 2026-11-30 · Time: 45 min

## Outcome

By the end of today you can: Explain AES, block modes, RSA/ECC and Diffie-Hellman, and when each is used.

## 1. Learn (15 min)

- ▶️ [Computerphile: Public Key Cryptography (YouTube)](https://www.youtube.com/watch?v=GSIDS_lvRv4)
- ▶️ [Computerphile: Secret Key Exchange (Diffie-Hellman) (YouTube)](https://www.youtube.com/watch?v=NmM9HA2MQGI)
- [CyberChef](https://gchq.github.io/CyberChef/)

## 2. Lab (25 min)

- [ ] Encrypt and decrypt a file with `openssl enc -aes-256-cbc -pbkdf2 -salt`. Note that `openssl enc` cannot do AEAD modes like GCM, which is one reason apps use crypto libraries instead.
- [ ] Generate an Ed25519 and an RSA key with `openssl genpkey` and compare sizes.
- [ ] In CyberChef, encrypt the same text with AES-ECB and AES-CBC and see why ECB leaks patterns.

## 3. Explain it like an SME (5 min)

> Why does TLS use asymmetric crypto to agree a key and then switch to symmetric crypto?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-22.md`
- [ ] Update the Notion tracker row for Day 22 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 21](../week-03/day-21-week-3-review-and-checkpoint.md) · [Roadmap](../../ROADMAP.md) · [Day 23 →](../week-04/day-23-hashing-macs-and-digital-signatures.md)
