# Day 52: Container security

**Phase 8: Cloud, containers and DevSecOps** · Area: Cloud · Planned: 2026-12-30 · Time: 45 min

## Outcome

By the end of today you can: Harden images and runtime, and explain container escape risks.

## 1. Learn (15 min)

- [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [Docker Bench for Security](https://github.com/docker/docker-bench-security)
- [Trivy](https://trivy.dev/)

## 2. Lab (25 min)

- [ ] Take a naive Dockerfile (root user, full OS base, secrets in ENV) and harden it (non-root, distroless or slim, multi-stage, no secrets).
- [ ] Scan both images with Trivy and compare counts.
- [ ] Run Docker Bench on your host and fix two findings.

## 3. Explain it like an SME (5 min)

> Why is mounting the Docker socket into a container equivalent to giving root on the host?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

You have written hundreds of Dockerfiles. Today you review them like an attacker would.

## Deliverable

- [ ] Commit: `labs/container-hardening/ with both Dockerfiles and results.`
- [ ] Update the Notion tracker row for Day 52 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 51](../week-08/day-51-aws-security-services-and-cloud-detection.md) · [Roadmap](../../ROADMAP.md) · [Day 53 →](../week-08/day-53-kubernetes-security.md)
