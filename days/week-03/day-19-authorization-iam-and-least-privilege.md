# Day 19: Authorization, IAM and least privilege

**Phase 3: Systems and identity** · Area: Identity · Planned: 2026-11-27 · Time: 45 min

## Outcome

By the end of today you can: Compare RBAC and ABAC, write least-privilege policies, and explain privileged access management.

## 1. Learn (15 min)

- [AWS IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

## 2. Lab (25 min)

- [ ] Take an over-broad IAM policy (s3:* on *) and rewrite it to read one bucket prefix only.
- [ ] Write a Kubernetes Role and RoleBinding that only lets a CI service account update one Deployment.
- [ ] List three ways a role can be escalated (iam:PassRole, wildcard actions, bind/escalate verbs in RBAC).

## 3. Explain it like an SME (5 min)

> What is least privilege, and how do you actually achieve it at scale without slowing engineers down?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

You have written IAM and RBAC for pipelines. Now review them asking 'what is the worst thing this identity can do?'

## Deliverable

- [ ] Commit: `notes/day-19.md with both policies.`
- [ ] Update the Notion tracker row for Day 19 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 18](../week-03/day-18-authentication-passwords-mfa-and-passkeys.md) · [Roadmap](../../ROADMAP.md) · [Day 20 →](../week-03/day-20-federation-with-oauth-2-0-oidc-saml-and-jwt.md)
