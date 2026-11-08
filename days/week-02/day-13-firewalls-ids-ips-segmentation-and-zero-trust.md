# Day 13: Firewalls, IDS/IPS, segmentation and zero trust

**Phase 2: Networking for security** · Area: Networking · Planned: 2026-11-21 · Time: 45 min

## Outcome

By the end of today you can: Explain stateful firewalls, WAFs, IDS vs IPS, segmentation and the core zero trust tenets.

## 1. Learn (15 min)

- [Cloudflare Learning: What is a firewall?](https://www.cloudflare.com/learning/security/what-is-a-firewall/)
- [NIST SP 800-207, Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)

## 2. Lab (25 min)

- [ ] In a throwaway Ubuntu container or VM, install nftables or ufw.
- [ ] Default-deny inbound, allow only 22 from one IP, and allow established traffic.
- [ ] Prove it with nmap from the attacker box before and after.
- [ ] Write the rule set and the evidence into your notes.

## 3. Explain it like an SME (5 min)

> What does 'never trust, always verify' change compared with a VPN plus flat network?

Answer out loud first, then write a 3 to 5 sentence answer in your notes.

## DevOps bridge

Kubernetes NetworkPolicies and service meshes (mTLS) are zero trust in practice. You will meet them again on day 53.

## Deliverable

- [ ] Commit: `notes/day-13.md`
- [ ] Update the Notion tracker row for Day 13 (Status, Confidence 1-5, Minutes, Notes)

---

[← Day 12](../week-02/day-12-network-reconnaissance-with-nmap.md) · [Roadmap](../../ROADMAP.md) · [Day 14 →](../week-02/day-14-week-2-review-and-checkpoint.md)
