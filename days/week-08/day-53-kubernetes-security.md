# Day 53: Kubernetes security

**Phase 8: Cloud, containers and DevSecOps** · Area: Cloud · Planned: 2026-12-31 · Time: 45 min

## Outcome

By the end of today you can: Secure a cluster with RBAC, Pod Security Standards, network policies and secrets handling.

## 1. Learn (15 min)

- [Kubernetes: Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [OWASP Kubernetes Top 10](https://owasp.org/www-project-kubernetes-top-ten/)
- [kube-bench](https://github.com/aquasecurity/kube-bench)

## 2. Lab (25 min)

- [ ] Create a cluster with kind (https://kind.sigs.k8s.io/).
- [ ] Label a namespace with pod-security.kubernetes.io/enforce=restricted and try deploying a privileged pod.
- [ ] Add a default-deny NetworkPolicy and prove it blocks traffic (kind needs a CNI such as Calico for policies).
- [ ] Run kube-bench as a Job and review the failures.

## 3. Explain it like an SME (5 min)

> Name five things you check first when reviewing a Kubernetes cluster's security.

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `labs/k8s-security/ with manifests and findings.`
- [ ] Update the Notion tracker row for Day 53 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 52](../week-08/day-52-container-security.md) · [Roadmap](../../ROADMAP.md) · [Day 54 →](../week-08/day-54-ci-cd-and-software-supply-chain-security.md)
