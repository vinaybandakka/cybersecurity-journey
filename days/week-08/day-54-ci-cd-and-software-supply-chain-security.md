# Day 54: CI/CD and software supply chain security

**Phase 8: Cloud, containers and DevSecOps** · Area: DevSecOps · Planned: 2027-01-01 · Time: 45 min

## Outcome

By the end of today you can: Explain the OWASP CI/CD Top 10, SLSA, SBOMs and how to harden GitHub Actions.

## 1. Learn (15 min)

- [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/)
- [SLSA framework](https://slsa.dev/)
- [GitHub Docs: Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

## 2. Lab (25 min)

- [ ] Generate an SBOM for a container image with syft (https://github.com/anchore/syft).
- [ ] Review a GitHub Actions workflow you know for pull_request_target misuse, unpinned actions and over-broad GITHUB_TOKEN permissions.
- [ ] Fix it (pin actions by SHA, set permissions to read-only by default, use OIDC instead of long-lived cloud keys).

## 3. Explain it like an SME (5 min)

> Explain the SolarWinds or the tj-actions/changed-files compromise and the controls that would have limited it.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

This is your strongest day. Pipelines you used to build are now an attack surface you defend.

## Deliverable

- [ ] Commit: `notes/day-54.md with the before/after workflow.`
- [ ] Update the Notion tracker row for Day 54 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 53](../week-08/day-53-kubernetes-security.md) · [Roadmap](../../ROADMAP.md) · [Day 55 →](../week-08/day-55-appsec-tooling-in-the-pipeline-sast-sca-dast-iac-s.md)
