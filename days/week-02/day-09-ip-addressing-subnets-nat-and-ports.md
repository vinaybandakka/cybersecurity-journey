# Day 09: IP addressing, subnets, NAT and ports

**Phase 2: Networking for security** · Area: Networking · Planned: 2026-11-17 · Time: 45 min

## Outcome

By the end of today you can: Subnet quickly, explain NAT, and know the 20 most common ports and what runs on them.

## 1. Learn (15 min)

- [Subnetting practice](https://subnettingpractice.com/)
- [Cloudflare Learning: What is a computer port?](https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)

## 2. Lab (25 min)

- [ ] Do 10 subnetting questions until you can answer each in under 60 seconds.
- [ ] Run `ss -tulpn` on your machine and in the lab containers and map each listening port to a service.
- [ ] Write the common ports table from memory (22, 25, 53, 80, 88, 135, 139, 389, 443, 445, 636, 1433, 3306, 3389, 5432, 5985, 6379, 8080, 9200, 27017), then check it.

## 3. Explain it like an SME (5 min)

> Why is 0.0.0.0/0 on port 22 in a security group a finding, and what would you replace it with?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

VPC CIDRs, security groups and NAT gateways are this exact topic. You will review them as an auditor now.

## Deliverable

- [ ] Commit: `notes/day-09.md with your ports table.`
- [ ] Update the Notion tracker row for Day 09 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 08](../week-02/day-08-osi-and-tcp-ip-models-tcp-handshake.md) · [Roadmap](../../ROADMAP.md) · [Day 10 →](../week-02/day-10-dns-and-http-through-a-security-lens.md)
