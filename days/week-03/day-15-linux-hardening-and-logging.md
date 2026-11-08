# Day 15: Linux hardening and logging

**Phase 3: Systems and identity** · Area: Systems · Planned: 2026-11-23 · Time: 45 min

## Outcome

By the end of today you can: Audit and harden a Linux host, and know where its security logs live.

## 1. Learn (15 min)

- [Lynis security auditing tool](https://cisofy.com/lynis/)
- [Mozilla OpenSSH guidelines](https://infosec.mozilla.org/guidelines/openssh)

## 2. Lab (25 min)

- [ ] In an Ubuntu container, install and run `lynis audit system`, and note the hardening index.
- [ ] Find SUID binaries: `find / -perm -4000 -type f 2>/dev/null`.
- [ ] Harden sshd_config (no root login, no passwords, modern ciphers) and explain each line.
- [ ] Look at /var/log/auth.log (or `journalctl -u ssh`) and find failed logins.
- [ ] Re-run Lynis and record the new score.

## 3. Explain it like an SME (5 min)

> Give the five Linux hardening steps you would bake into every base image and why.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

Golden images and Ansible roles are where these controls belong. Hardening is config management.

## Deliverable

- [ ] Commit: `notes/day-15.md with before/after Lynis scores.`
- [ ] Update the Notion tracker row for Day 15 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 14](../week-02/day-14-week-2-review-and-checkpoint.md) · [Roadmap](../../ROADMAP.md) · [Day 16 →](../week-03/day-16-windows-security-fundamentals.md)
