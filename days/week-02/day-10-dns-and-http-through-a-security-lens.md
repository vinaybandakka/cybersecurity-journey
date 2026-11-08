# Day 10: DNS and HTTP through a security lens

**Phase 2: Networking for security** · Area: Networking · Planned: 2026-11-18 · Time: 45 min

## Outcome

By the end of today you can: Trace a DNS resolution, read every part of an HTTP request and response, and name DNS attacks.

## 1. Learn (15 min)

- [Cloudflare Learning: What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [MDN: An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- ▶️ [freeCodeCamp: How does the internet work? (YouTube)](https://www.youtube.com/watch?v=zN8YNNHcaZc)

## 2. Lab (25 min)

- [ ] `dig +trace example.com` and label root, TLD and authoritative servers.
- [ ] `dig example.com TXT`, `dig example.com MX` and explain what each record is used for.
- [ ] `curl -v https://example.com` and label the method, status code, headers and cookies.
- [ ] Write two lines each on DNS spoofing/cache poisoning, DNS tunnelling and subdomain takeover.

## 3. Explain it like an SME (5 min)

> How can DNS be used to exfiltrate data, and how would you detect it?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-10.md`
- [ ] Update the Notion tracker row for Day 10 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 09](../week-02/day-09-ip-addressing-subnets-nat-and-ports.md) · [Roadmap](../../ROADMAP.md) · [Day 11 →](../week-02/day-11-packet-analysis-with-wireshark.md)
