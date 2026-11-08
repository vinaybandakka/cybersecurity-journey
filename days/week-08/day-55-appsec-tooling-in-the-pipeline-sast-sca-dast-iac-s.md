# Day 55: AppSec tooling in the pipeline (SAST, SCA, DAST, IaC, secrets)

**Phase 8: Cloud, containers and DevSecOps** · Area: DevSecOps · Planned: 2027-01-02 · Time: 45 min

## Outcome

By the end of today you can: Build a security pipeline and explain what each tool class finds and misses.

## 1. Learn (15 min)

- [Semgrep documentation](https://semgrep.dev/docs/)
- [Checkov (IaC scanning)](https://www.checkov.io/)
- [ZAP baseline scan (Docker)](https://www.zaproxy.org/docs/docker/baseline-scan/)

## 2. Lab (25 min)

- [ ] Add .github/workflows/devsecops-demo.yml to a scratch repo with semgrep, gitleaks, checkov and trivy steps.
- [ ] Add a deliberately bad Terraform file (public S3 bucket) and a vulnerable code snippet and watch the jobs fail.
- [ ] Run a ZAP baseline scan against your local Juice Shop.

## 3. Explain it like an SME (5 min)

> A team complains the security scanners block every PR with noise. How do you fix that without losing coverage?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

Pipeline design is your home turf. Security teams desperately need people who can do this well.

## Deliverable

- [ ] Commit: `labs/devsecops-pipeline/ with the workflow and results.`
- [ ] Update the Notion tracker row for Day 55 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 54](../week-08/day-54-ci-cd-and-software-supply-chain-security.md) · [Roadmap](../../ROADMAP.md) · [Day 56 →](../week-08/day-56-threat-modeling.md)
