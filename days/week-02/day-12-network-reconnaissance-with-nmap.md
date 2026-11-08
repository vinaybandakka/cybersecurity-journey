# Day 12: Network reconnaissance with Nmap

**Phase 2: Networking for security** · Area: Networking · Planned: 2026-11-20 · Time: 45 min

## Outcome

By the end of today you can: Choose the right Nmap scan for the job and interpret open, closed and filtered results.

## 1. Learn (15 min)

- [Nmap reference guide](https://nmap.org/book/man.html)
- [Nmap: port scanning basics](https://nmap.org/book/man-port-scanning-basics.html)

## 2. Lab (25 min)

- [ ] From the attacker container: `nmap -sn 172.30.0.0/24` to find hosts on the lab network.
- [ ] `nmap -sV -sC -p- juice-shop dvwa` and record services and versions.
- [ ] Compare a SYN scan (-sS) and a connect scan (-sT) and note the difference in your own words.
- [ ] Only scan your lab or scanme.nmap.org, which Nmap explicitly allows. Scanning anything else needs written permission.

## 3. Explain it like an SME (5 min)

> Why can a port show as 'filtered', and what does that tell you about the network?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `labs/writeups/nmap-lab.md`
- [ ] Update the Notion tracker row for Day 12 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 11](../week-02/day-11-packet-analysis-with-wireshark.md) · [Roadmap](../../ROADMAP.md) · [Day 13 →](../week-02/day-13-firewalls-ids-ips-segmentation-and-zero-trust.md)
