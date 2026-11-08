# Day 11: Packet analysis with Wireshark

**Phase 2: Networking for security** · Area: Networking · Planned: 2026-11-19 · Time: 45 min

## Outcome

By the end of today you can: Filter, follow streams and pull evidence (credentials, files, hostnames) out of a pcap.

## 1. Learn (15 min)

- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Wireshark sample captures](https://wiki.wireshark.org/SampleCaptures)

## 2. Lab (25 min)

- [ ] Install Wireshark on your host machine.
- [ ] Download a plain-text protocol capture (HTTP or FTP or Telnet) from the sample captures page.
- [ ] Use display filters: `http.request`, `ftp`, `tcp.stream eq 0`, `dns.qry.name contains`.
- [ ] Use Follow TCP Stream to recover the cleartext credentials or content, then write what control would have prevented it.

## 3. Explain it like an SME (5 min)

> A pcap from a breach lands on your desk. What are the first five filters you apply and why?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-11.md with your filters cheat sheet.`
- [ ] Update the Notion tracker row for Day 11 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 10](../week-02/day-10-dns-and-http-through-a-security-lens.md) · [Roadmap](../../ROADMAP.md) · [Day 12 →](../week-02/day-12-network-reconnaissance-with-nmap.md)
