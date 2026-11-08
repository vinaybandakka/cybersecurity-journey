# Day 08: OSI and TCP/IP models, TCP handshake

**Phase 2: Networking for security** · Area: Networking · Planned: 2026-11-16 · Time: 45 min

## Outcome

By the end of today you can: Walk through encapsulation layer by layer and spot a TCP three-way handshake in a capture.

## 1. Learn (15 min)

- [Cloudflare Learning: What is the OSI model?](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)
- ▶️ [freeCodeCamp: Computer Networking Course (YouTube), watch the TCP/IP and OSI sections](https://www.youtube.com/watch?v=qiQR5rTSshw)

## 2. Lab (25 min)

- [ ] In the attacker container: `tcpdump -i any -nn -w /tmp/day08.pcap port 3000` in one shell.
- [ ] In another shell run `curl http://juice-shop:3000`, then stop the capture.
- [ ] Read it back with `tcpdump -nn -r /tmp/day08.pcap` and label SYN, SYN-ACK, ACK, data and FIN.

## 3. Explain it like an SME (5 min)

> What happens at each layer when you type a URL and press Enter, and where can an attacker interfere?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-08.md with the annotated handshake.`
- [ ] Update the Notion tracker row for Day 08 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 07](../week-01/day-07-week-1-review-and-checkpoint.md) · [Roadmap](../../ROADMAP.md) · [Day 09 →](../week-02/day-09-ip-addressing-subnets-nat-and-ports.md)
