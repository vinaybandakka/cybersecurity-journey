# Day 04: Build your home lab with Docker

**Phase 1: Foundations and home lab** · Area: Foundations · Planned: 2026-11-12 · Time: 45 min

## Outcome

By the end of today you can: Run an isolated, disposable lab with vulnerable apps and an attacker toolbox.

## 1. Learn (15 min)

- [OWASP Juice Shop project](https://owasp.org/www-project-juice-shop/)
- [DVWA (Damn Vulnerable Web Application)](https://github.com/digininja/DVWA)
- [Kali Linux Docker images](https://www.kali.org/docs/containers/official-kalilinux-docker-images/)

## 2. Lab (25 min)

- [ ] Read labs/LAB_SETUP.md, then run `docker compose -f labs/docker-compose.yml up -d`.
- [ ] Open Juice Shop on http://localhost:3000 and DVWA on http://localhost:8081, and confirm both load.
- [ ] Exec into the attacker box: `docker compose -f labs/docker-compose.yml exec attacker bash`, then `curl -I http://juice-shop:3000`.
- [ ] Confirm with `docker network inspect` that the lab network is internal-only and write down why that matters.

## 3. Explain it like an SME (5 min)

> Why must vulnerable lab targets never be exposed on a public IP, and how did you enforce that?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

You already know Compose and networks. This is the same skill pointed at a security lab.

## Deliverable

- [ ] Commit: `notes/day-04.md with a screenshot or the output proving the lab works.`
- [ ] Update the Notion tracker row for Day 04 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 03](../week-01/day-03-security-frameworks-nist-csf-2-0-and-cis-controls.md) · [Roadmap](../../ROADMAP.md) · [Day 05 →](../week-01/day-05-linux-command-line-for-security-part-1.md)
