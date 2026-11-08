# Sounding like a subject matter expert

Knowing a topic and sounding like an expert are two different skills. You practise the second one here.

## How an SME answers (use this structure every time)

1. **Define it in one sentence**, using the precise term. ("SSRF is when an attacker makes the server send requests on their behalf.")
2. **Explain the mechanism.** Why it happens, at the level of the protocol or code.
3. **Give a real example.** A breach, a CVE or your own lab. (Capital One 2019 for SSRF.)
4. **Say how to prevent it and how to detect it.** Experts always cover both.
5. **State the trade-off or nuance.** ("IMDSv2 helps, but the real fix is not letting user input choose URLs.")

Record yourself. If an answer runs past 2 minutes or you say "basically" more than twice, redo it.

## Week 1: foundations

1. Explain the CIA triad with an example of an attack on each.
2. What is the difference between a threat, a vulnerability and a risk?
3. What are preventive, detective and corrective controls? Give one of each from a CI/CD pipeline.
4. What are the six functions of NIST CSF 2.0?
5. What is defence in depth?
6. What is the difference between authentication, authorization and accounting?
7. Why is security a business risk problem and not only a technical one?

## Week 2: networking

1. Walk through what happens when you type a URL into a browser, including security controls.
2. Explain the TCP three-way handshake and what a SYN flood does to it.
3. TCP vs UDP: which protocols use which, and why does it matter for firewalls?
4. How does DNS resolution work, and name three DNS attacks.
5. What do open, closed and filtered mean in an Nmap scan?
6. Stateful vs stateless firewall vs WAF: what does each see and block?
7. What is zero trust, and how is it different from a VPN?
8. What would you look for first in a pcap from a suspected breach?

## Week 3: systems and identity

1. Five Linux hardening steps you would put in every base image.
2. What do Windows event IDs 4624, 4625, 4688 and 4720 mean?
3. Explain Kerberos at a high level and what Kerberoasting abuses.
4. How should passwords be stored, and why are salts and slow hashes important?
5. Why are passkeys phishing-resistant and SMS codes not?
6. RBAC vs ABAC: when would you use each?
7. OAuth vs OIDC vs SAML.
8. Name three common JWT vulnerabilities.
9. How would you implement least privilege across 200 engineers without blocking them?

## Week 4: cryptography and web basics

1. Symmetric vs asymmetric encryption, and why TLS uses both.
2. Hash vs HMAC vs digital signature.
3. Walk through a TLS 1.3 handshake.
4. What is a certificate chain and how does a client validate it?
5. What is mTLS and where would you use it?
6. A secret leaked in git. What do you do, in order?
7. Explain the same-origin policy and what CORS changes.
8. Which security headers would you set by default and why?
9. Encryption in transit vs at rest vs end to end.

## Week 5: web and API security

1. How does SQL injection work and why do parameterised queries fix it?
2. Reflected vs stored vs DOM XSS, and how CSP helps.
3. What is IDOR, and why do scanners rarely find it?
4. What is CSRF, and how do SameSite cookies change it?
5. Explain SSRF and how it led to a cloud breach.
6. What is BOLA in the OWASP API Top 10?
7. How would you run a secure code review on a pull request?
8. The OWASP Top 10: name them and pick one to go deep on.

## Week 6: offensive and vulnerability management

1. Vulnerability scan vs penetration test vs red team.
2. What must be in rules of engagement before any testing?
3. What is MITRE ATT&CK and how do defenders use it?
4. CVSS vs EPSS vs CISA KEV: how do you prioritise 4,000 findings?
5. Bind shell vs reverse shell, and how egress filtering helps.
6. Three common Linux privilege escalation paths and their fixes.
7. Explain SPF, DKIM and DMARC.
8. Password spraying vs credential stuffing vs brute force.

## Week 7: defensive operations

1. What makes a good security log entry?
2. How does a SIEM work, and what is correlation?
3. What makes a detection good? Talk about precision, recall and maintenance.
4. Walk through the incident response lifecycle.
5. Contain first or investigate first?
6. What is the order of volatility?
7. IOCs vs TTPs, and the Pyramid of Pain.
8. Detection vs threat hunting vs purple teaming.

## Week 8: cloud and DevSecOps

1. Explain the shared responsibility model for IaaS, PaaS and SaaS.
2. Top five AWS misconfigurations you would check first.
3. An IAM key is used from an unusual country. What do you do?
4. Why is mounting the Docker socket dangerous?
5. How do you secure a Kubernetes cluster? Give five controls.
6. What are the OWASP Top 10 CI/CD risks? Pick two and explain.
7. What is SLSA, and what is an SBOM good for?
8. SAST vs SCA vs DAST vs IaC scanning: what does each catch and miss?
9. How do you stop security tools from drowning developers in noise?
10. Walk me through a STRIDE threat model.

## Week 9: GRC and architecture

1. Policy vs standard vs procedure vs guideline.
2. What are the four ways to treat a risk?
3. ISO 27001 vs SOC 2: who needs which?
4. Compliant vs secure: give an example where they differ.
5. Name the secure design principles you rely on most.
6. Design a secure three-tier application in the cloud.

## Behavioural questions for a DevOps-to-security move

1. Tell me about yourself and why you moved to security.
2. Tell me about a time you found or fixed a security problem as a DevOps engineer.
3. How would you get developers to adopt a security control they see as friction?
4. What does a security team usually get wrong about engineering teams?
5. What have you built in the last 60 days? (Point to this repo.)
