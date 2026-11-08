# Day 51: AWS security services and cloud detection

**Phase 8: Cloud, containers and DevSecOps** · Area: Cloud · Planned: 2026-12-29 · Time: 45 min

## Outcome

By the end of today you can: Explain CloudTrail, GuardDuty, Security Hub, SCPs and how to investigate in AWS.

## 1. Learn (15 min)

- [AWS CloudTrail user guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Amazon GuardDuty: what is GuardDuty?](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Prowler (open source cloud security scanner)](https://github.com/prowler-cloud/prowler)

## 2. Lab (25 min)

- [ ] Solve flAWS levels 3 and 4 (secrets in git history, public snapshots).
- [ ] If you have a personal AWS account: run Prowler with read-only credentials and review the top 10 failed checks.
- [ ] Write a CloudTrail query (Athena or CLI) that finds who created an access key in the last 24 hours.

## 3. Explain it like an SME (5 min)

> An IAM key was used from an unusual country. What do you check, in what order?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## Deliverable

- [ ] Commit: `notes/day-51.md`
- [ ] Update the Notion tracker row for Day 51 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 50](../week-08/day-50-cloud-security-fundamentals.md) · [Roadmap](../../ROADMAP.md) · [Day 52 →](../week-08/day-52-container-security.md)
