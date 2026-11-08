# Day 23: Hashing, MACs and digital signatures

**Phase 4: Cryptography, PKI and web basics** · Area: Cryptography · Planned: 2026-12-01 · Time: 45 min

## Outcome

By the end of today you can: Distinguish hash, HMAC and signature, and sign and verify artifacts.

## 1. Learn (15 min)

- ▶️ [Computerphile: Hashing Algorithms and Security (YouTube)](https://www.youtube.com/watch?v=b4b8ktEV4Bg)
- [Sigstore documentation (cosign)](https://docs.sigstore.dev/)

## 2. Lab (25 min)

- [ ] `sha256sum` a file, change one byte and compare (avalanche effect).
- [ ] Create an HMAC with `openssl dgst -sha256 -hmac`.
- [ ] Sign a file with your Ed25519 key and verify it, then tamper with the file and verify again.
- [ ] Optional: sign a container image with `cosign sign-blob` or `cosign sign`.

## 3. Explain it like an SME (5 min)

> Why is a hash on a download page not enough to prove the file came from the vendor?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

Artifact signing and checksum verification in pipelines are supply-chain controls. You are now the one who designs them.

## Deliverable

- [ ] Commit: `notes/day-23.md`
- [ ] Update the Notion tracker row for Day 23 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 22](../week-04/day-22-symmetric-and-asymmetric-crypto-key-exchange.md) · [Roadmap](../../ROADMAP.md) · [Day 24 →](../week-04/day-24-pki-and-tls.md)
