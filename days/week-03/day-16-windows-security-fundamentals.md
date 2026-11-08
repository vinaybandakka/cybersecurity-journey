# Day 16: Windows security fundamentals

**Phase 3: Systems and identity** · Area: Systems · Planned: 2026-11-24 · Time: 45 min

## Outcome

By the end of today you can: Explain Windows accounts, UAC, the registry, and the event IDs every analyst knows.

## 1. Learn (15 min)

- [TryHackMe: Windows Fundamentals 1 (free room)](https://tryhackme.com/room/windowsfundamentals1xbx)
- [Ultimate Windows Security: event ID encyclopedia](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/)
- [Microsoft Sysinternals Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)

## 2. Lab (25 min)

- [ ] Complete the TryHackMe room (it gives you a browser-based Windows VM).
- [ ] Learn these event IDs and write one line each: 4624, 4625, 4634, 4648, 4672, 4688, 4720, 4732, 1102, 7045.
- [ ] Note what Sysmon adds over the default logs (process command lines, network connections, hashes).

## 3. Explain it like an SME (5 min)

> Which Windows events would show a brute-force attack followed by a successful login and a new admin user?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-16.md with your event ID table.`
- [ ] Update the Notion tracker row for Day 16 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 15](../week-03/day-15-linux-hardening-and-logging.md) · [Roadmap](../../ROADMAP.md) · [Day 17 →](../week-03/day-17-active-directory-and-kerberos-basics.md)
