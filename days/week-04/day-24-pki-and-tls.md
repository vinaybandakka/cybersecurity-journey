# Day 24: PKI and TLS

**Phase 4: Cryptography, PKI and web basics** · Area: Cryptography · Planned: 2026-12-02 · Time: 45 min

## Outcome

By the end of today you can: Read a certificate chain, explain the TLS 1.3 handshake and debug common TLS failures.

## 1. Learn (15 min)

- [The Illustrated TLS 1.3 Connection](https://tls13.xargs.org/)
- [Cloudflare Learning: What happens in a TLS handshake?](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)

## 2. Lab (25 min)

- [ ] `openssl s_client -connect github.com:443 -showcerts` and identify leaf, intermediate and root.
- [ ] Look up a domain you know on crt.sh (https://crt.sh/) and explain Certificate Transparency.
- [ ] Run the Qualys SSL Labs test (https://www.ssllabs.com/ssltest/) on a site you own or a big public site.
- [ ] Create a local CA, issue a server cert and a client cert, and describe how mTLS uses them.

## 3. Explain it like an SME (5 min)

> A service throws 'certificate verify failed'. List five possible causes in order of likelihood.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-24.md`
- [ ] Update the Notion tracker row for Day 24 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 23](../week-04/day-23-hashing-macs-and-digital-signatures.md) · [Roadmap](../../ROADMAP.md) · [Day 25 →](../week-04/day-25-secrets-management-and-crypto-failures.md)
