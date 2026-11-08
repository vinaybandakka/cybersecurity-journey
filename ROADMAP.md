# 60-day security fundamentals roadmap

60 days × 45 minutes = 45 focused hours. Every day follows the same rhythm:

| Block | Minutes | What you do |
|---|---|---|
| Learn | 15 | One video or reading from the day page. Take notes in your own words. |
| Lab | 25 | Hands-on work in your lab or on a free platform. Always produces evidence. |
| Explain | 5 | Answer the SME question out loud, then write 3 to 5 sentences. |

Every seventh day is a review and checkpoint against [sme/INTERVIEW_QUESTIONS.md](sme/INTERVIEW_QUESTIONS.md).

## Phases at a glance

| Phase | Days | Focus | Milestone |
|---|---|---|---|
| 1. Foundations and home lab | 1-7 | Think like a defender, speak the core vocabulary, and have a working lab. | Lab running, Bandit level 13 reached, risk register and CSF mapping committed. |
| 2. Networking for security | 8-14 | Read packets, map networks and explain where each network control sits. | Annotated packet captures, an Nmap write-up and a packet-journey diagram with controls. |
| 3. Systems and identity | 15-21 | Harden Linux and Windows, and explain authentication, authorization and federation. | Lynis before/after, Windows event ID table, least-privilege IAM and RBAC policies, first PortSwigger lab. |
| 4. Cryptography, PKI and web basics | 22-28 | Use crypto correctly, debug TLS, manage secrets, and proxy web traffic with Burp. | Local CA with mTLS, gitleaks finding a leaked key, Burp intercepting Juice Shop. |
| 5. Web and API security | 29-35 | Find, exploit (in labs) and fix the OWASP Top 10 and OWASP API Top 10 classes. | At least 12 PortSwigger labs and 10 Juice Shop challenges solved with write-ups. |
| 6. Offensive security and vulnerability management | 36-42 | Run a scoped test with a methodology, map to ATT&CK and prioritise vulns like a pro. | An ATT&CK Navigator layer and a mini pentest report. |
| 7. Defensive security operations | 43-49 | Collect logs, write detections, and lead an incident from triage to lessons learned. | Sigma and YARA rules in detections/, an IR playbook in playbooks/, a hunt write-up. |
| 8. Cloud, containers and DevSecOps | 50-56 | Secure AWS, containers, Kubernetes and CI/CD, which is where your DevOps edge is biggest. | flAWS levels 1-4, a hardened image, a secured kind cluster, a DevSecOps pipeline and a threat model. |
| 9. GRC, architecture and capstone | 57-60 | Talk risk and compliance with leadership, design secure systems, and prove it end to end. | Secure architecture doc, capstone report, recorded mock interview and a next-90-days plan. |

## Phase 1: Foundations and home lab (days 1-7)

**Goal:** Think like a defender, speak the core vocabulary, and have a working lab.

**Topics:** CIA triad and AAA, threats vulnerabilities and risk, control types, NIST CSF 2.0, CIS Controls, ISO 27001, Docker-based lab, Linux command line.

**Milestone:** Lab running, Bandit level 13 reached, risk register and CSF mapping committed.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [01](days/week-01/day-01-the-security-mindset-cia-and-aaa.md) | The security mindset, CIA and AAA | Explain confidentiality, integrity, availability, authentication, authorization and accounting with a real example of each. | ▶️ [link](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv) |
| [02](days/week-01/day-02-threats-vulnerabilities-risk-and-controls.md) | Threats, vulnerabilities, risk and controls | Define threat, vulnerability, exploit, risk and impact precisely, and classify controls by type and function. | ▶️ [link](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv) |
| [03](days/week-01/day-03-security-frameworks-nist-csf-2-0-and-cis-controls.md) | Security frameworks, NIST CSF 2.0 and CIS Controls | Name the six NIST CSF 2.0 functions and explain how CIS Controls and ISO 27001 relate to it. | [link](https://www.nist.gov/cyberframework) |
| [04](days/week-01/day-04-build-your-home-lab-with-docker.md) | Build your home lab with Docker | Run an isolated, disposable lab with vulnerable apps and an attacker toolbox. | [link](https://owasp.org/www-project-juice-shop/) |
| [05](days/week-01/day-05-linux-command-line-for-security-part-1.md) | Linux command line for security, part 1 | Move around Linux, read files in awkward ways, and use ssh comfortably under pressure. | [link](https://overthewire.org/wargames/bandit/) |
| [06](days/week-01/day-06-linux-command-line-for-security-part-2.md) | Linux command line for security, part 2 | Use find, grep, sort, uniq, base64, tr and tar/gzip to dig through data fast. | [link](https://overthewire.org/wargames/bandit/) |
| [07](days/week-01/day-07-week-1-review-and-checkpoint.md) | Week 1 review and checkpoint | Explain week 1 concepts without notes and fill your gaps. | [link](https://roadmap.sh/cyber-security) |

## Phase 2: Networking for security (days 8-14)

**Goal:** Read packets, map networks and explain where each network control sits.

**Topics:** OSI and TCP/IP, TCP/UDP, subnetting and NAT, common ports, DNS and DNS attacks, HTTP, Wireshark, Nmap, firewalls, IDS/IPS, segmentation, zero trust.

**Milestone:** Annotated packet captures, an Nmap write-up and a packet-journey diagram with controls.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [08](days/week-02/day-08-osi-and-tcp-ip-models-tcp-handshake.md) | OSI and TCP/IP models, TCP handshake | Walk through encapsulation layer by layer and spot a TCP three-way handshake in a capture. | [link](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/) |
| [09](days/week-02/day-09-ip-addressing-subnets-nat-and-ports.md) | IP addressing, subnets, NAT and ports | Subnet quickly, explain NAT, and know the 20 most common ports and what runs on them. | [link](https://subnettingpractice.com/) |
| [10](days/week-02/day-10-dns-and-http-through-a-security-lens.md) | DNS and HTTP through a security lens | Trace a DNS resolution, read every part of an HTTP request and response, and name DNS attacks. | [link](https://www.cloudflare.com/learning/dns/what-is-dns/) |
| [11](days/week-02/day-11-packet-analysis-with-wireshark.md) | Packet analysis with Wireshark | Filter, follow streams and pull evidence (credentials, files, hostnames) out of a pcap. | [link](https://www.wireshark.org/docs/wsug_html_chunked/) |
| [12](days/week-02/day-12-network-reconnaissance-with-nmap.md) | Network reconnaissance with Nmap | Choose the right Nmap scan for the job and interpret open, closed and filtered results. | [link](https://nmap.org/book/man.html) |
| [13](days/week-02/day-13-firewalls-ids-ips-segmentation-and-zero-trust.md) | Firewalls, IDS/IPS, segmentation and zero trust | Explain stateful firewalls, WAFs, IDS vs IPS, segmentation and the core zero trust tenets. | [link](https://www.cloudflare.com/learning/security/what-is-a-firewall/) |
| [14](days/week-02/day-14-week-2-review-and-checkpoint.md) | Week 2 review and checkpoint | Draw a packet's journey with every security control on the path. | [link](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/) |

## Phase 3: Systems and identity (days 15-21)

**Goal:** Harden Linux and Windows, and explain authentication, authorization and federation.

**Topics:** Linux hardening, Linux logs, Windows accounts and event IDs, Sysmon, Active Directory, Kerberos, password storage, MFA and passkeys, RBAC and ABAC, cloud IAM, OAuth 2.0, OIDC, SAML, JWT.

**Milestone:** Lynis before/after, Windows event ID table, least-privilege IAM and RBAC policies, first PortSwigger lab.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [15](days/week-03/day-15-linux-hardening-and-logging.md) | Linux hardening and logging | Audit and harden a Linux host, and know where its security logs live. | [link](https://cisofy.com/lynis/) |
| [16](days/week-03/day-16-windows-security-fundamentals.md) | Windows security fundamentals | Explain Windows accounts, UAC, the registry, and the event IDs every analyst knows. | [link](https://tryhackme.com/room/windowsfundamentals1xbx) |
| [17](days/week-03/day-17-active-directory-and-kerberos-basics.md) | Active Directory and Kerberos basics | Explain domains, OUs, GPOs, Kerberos tickets and the classic AD attacks at concept level. | [link](https://tryhackme.com/room/winadbasics) |
| [18](days/week-03/day-18-authentication-passwords-mfa-and-passkeys.md) | Authentication, passwords, MFA and passkeys | Explain modern password guidance, how passwords should be stored, and why phishing-resistant MFA matters. | [link](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) |
| [19](days/week-03/day-19-authorization-iam-and-least-privilege.md) | Authorization, IAM and least privilege | Compare RBAC and ABAC, write least-privilege policies, and explain privileged access management. | [link](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) |
| [20](days/week-03/day-20-federation-with-oauth-2-0-oidc-saml-and-jwt.md) | Federation with OAuth 2.0, OIDC, SAML and JWT | Explain the OAuth authorization code flow with PKCE, how OIDC adds identity, and common JWT mistakes. | ▶️ [link](https://www.youtube.com/watch?v=996OiexHze0) |
| [21](days/week-03/day-21-week-3-review-and-checkpoint.md) | Week 3 review and checkpoint | Defend a host and an identity design in front of a reviewer. | [link](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview) |

## Phase 4: Cryptography, PKI and web basics (days 22-28)

**Goal:** Use crypto correctly, debug TLS, manage secrets, and proxy web traffic with Burp.

**Topics:** AES and block modes, RSA/ECC, Diffie-Hellman, hashing, HMAC, signatures, artifact signing, PKI, TLS 1.3, mTLS, secrets management, browser security model, CORS, security headers, OWASP Top 10, Burp Suite.

**Milestone:** Local CA with mTLS, gitleaks finding a leaked key, Burp intercepting Juice Shop.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [22](days/week-04/day-22-symmetric-and-asymmetric-crypto-key-exchange.md) | Symmetric and asymmetric crypto, key exchange | Explain AES, block modes, RSA/ECC and Diffie-Hellman, and when each is used. | ▶️ [link](https://www.youtube.com/watch?v=GSIDS_lvRv4) |
| [23](days/week-04/day-23-hashing-macs-and-digital-signatures.md) | Hashing, MACs and digital signatures | Distinguish hash, HMAC and signature, and sign and verify artifacts. | ▶️ [link](https://www.youtube.com/watch?v=b4b8ktEV4Bg) |
| [24](days/week-04/day-24-pki-and-tls.md) | PKI and TLS | Read a certificate chain, explain the TLS 1.3 handshake and debug common TLS failures. | [link](https://tls13.xargs.org/) |
| [25](days/week-04/day-25-secrets-management-and-crypto-failures.md) | Secrets management and crypto failures | Explain why secrets leak, how to rotate them, and run a secrets manager and a secrets scanner. | [link](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) |
| [26](days/week-04/day-26-browser-security-model-and-security-headers.md) | Browser security model and security headers | Explain same-origin policy, CORS, cookie flags and the main security headers. | [link](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) |
| [27](days/week-04/day-27-owasp-top-10-overview-and-burp-suite.md) | OWASP Top 10 overview and Burp Suite | Name the OWASP Top 10 categories and intercept, modify and replay requests in Burp. | [link](https://owasp.org/Top10/) |
| [28](days/week-04/day-28-week-4-review-and-checkpoint.md) | Week 4 review and checkpoint | Explain crypto and web basics with confidence and fix your weakest topic. | [link](https://cryptopals.com/) |

## Phase 5: Web and API security (days 29-35)

**Goal:** Find, exploit (in labs) and fix the OWASP Top 10 and OWASP API Top 10 classes.

**Topics:** SQL injection, XSS, CSP, broken access control and IDOR, authentication flaws, CSRF, SSRF, command injection, path traversal, OWASP API Top 10, secure code review.

**Milestone:** At least 12 PortSwigger labs and 10 Juice Shop challenges solved with write-ups.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [29](days/week-05/day-29-sql-injection.md) | SQL injection | Find and exploit SQLi in labs, and fix it with parameterised queries. | [link](https://portswigger.net/web-security/sql-injection) |
| [30](days/week-05/day-30-cross-site-scripting-xss.md) | Cross-site scripting (XSS) | Explain reflected, stored and DOM XSS, exploit each in labs, and prevent them with encoding and CSP. | [link](https://portswigger.net/web-security/cross-site-scripting) |
| [31](days/week-05/day-31-broken-access-control-and-idor.md) | Broken access control and IDOR | Find horizontal and vertical privilege escalation and explain server-side authorization checks. | [link](https://portswigger.net/web-security/access-control) |
| [32](days/week-05/day-32-authentication-flaws-sessions-and-csrf.md) | Authentication flaws, sessions and CSRF | Attack weak login and session handling in labs and explain CSRF and its defences. | [link](https://portswigger.net/web-security/authentication) |
| [33](days/week-05/day-33-ssrf-command-injection-and-path-traversal.md) | SSRF, command injection and path traversal | Exploit server-side injection classes in labs and explain why SSRF is critical in the cloud. | [link](https://portswigger.net/web-security/ssrf) |
| [34](days/week-05/day-34-api-security.md) | API security | Explain the OWASP API Security Top 10 and test an API for BOLA and mass assignment. | [link](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) |
| [35](days/week-05/day-35-week-5-review-and-secure-code-review.md) | Week 5 review and secure code review | Spot vulnerabilities in code and explain the fix like an AppSec engineer. | [link](https://owasp.org/www-project-code-review-guide/) |

## Phase 6: Offensive security and vulnerability management (days 36-42)

**Goal:** Run a scoped test with a methodology, map to ATT&CK and prioritise vulns like a pro.

**Topics:** ethics and rules of engagement, pentest methodology, Cyber Kill Chain, MITRE ATT&CK, CVE, CVSS, EPSS, CISA KEV, Metasploit, shells, Linux privilege escalation, phishing, SPF/DKIM/DMARC, password attacks, reporting.

**Milestone:** An ATT&CK Navigator layer and a mini pentest report.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [36](days/week-06/day-36-ethics-rules-of-engagement-and-pentest-methodology.md) | Ethics, rules of engagement and pentest methodology | Explain legal boundaries, scoping and the phases of a penetration test and the kill chain. | [link](https://csrc.nist.gov/pubs/sp/800/115/final) |
| [37](days/week-06/day-37-mitre-att-ck.md) | MITRE ATT&CK | Navigate ATT&CK, map a real intrusion to techniques, and use it to find detection gaps. | [link](https://attack.mitre.org/) |
| [38](days/week-06/day-38-vulnerability-management-cve-cvss-epss-and-kev.md) | Vulnerability management, CVE, CVSS, EPSS and KEV | Score and prioritise vulnerabilities using severity, exploitability and exposure, not just CVSS. | [link](https://www.first.org/cvss/calculator/3.1) |
| [39](days/week-06/day-39-exploitation-basics-and-metasploit.md) | Exploitation basics and Metasploit | Explain payloads, bind vs reverse shells and run a controlled exploit in a lab. | [link](https://tryhackme.com/room/metasploitintro) |
| [40](days/week-06/day-40-linux-privilege-escalation.md) | Linux privilege escalation | Enumerate a Linux box for privilege escalation paths and know the defence for each. | [link](https://tryhackme.com/room/linprivesc) |
| [41](days/week-06/day-41-phishing-email-security-and-password-attacks.md) | Phishing, email security and password attacks | Analyse a phishing email and explain SPF, DKIM, DMARC, password spraying and credential stuffing. | [link](https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/) |
| [42](days/week-06/day-42-week-6-review-and-mini-pentest-report.md) | Week 6 review and mini pentest report | Communicate findings in a report a developer can fix and an executive can understand. | [link](https://github.com/juliocesarfort/public-pentesting-reports) |

## Phase 7: Defensive security operations (days 43-49)

**Goal:** Collect logs, write detections, and lead an incident from triage to lessons learned.

**Topics:** security logging, SIEM, detection engineering, Sigma, incident response lifecycle, forensics basics, traffic analysis, malware types, threat intelligence, Pyramid of Pain, YARA, threat hunting, Atomic Red Team, tabletop exercises.

**Milestone:** Sigma and YARA rules in detections/, an IR playbook in playbooks/, a hunt write-up.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [43](days/week-07/day-43-security-logging-and-siem-fundamentals.md) | Security logging and SIEM fundamentals | Explain what to log, how a SIEM normalises and correlates data, and investigate raw logs. | [link](https://tryhackme.com/room/introtosiem) |
| [44](days/week-07/day-44-detection-engineering-with-sigma.md) | Detection engineering with Sigma | Write a Sigma rule, convert it to a SIEM query and treat detections as code. | [link](https://github.com/SigmaHQ/sigma) |
| [45](days/week-07/day-45-incident-response-lifecycle.md) | Incident response lifecycle | Lead an incident through preparation, detection, containment, eradication, recovery and lessons learned. | [link](https://csrc.nist.gov/pubs/sp/800/61/r3/final) |
| [46](days/week-07/day-46-digital-forensics-and-traffic-analysis.md) | Digital forensics and traffic analysis | Explain order of volatility and chain of custody, and analyse a malicious traffic capture. | [link](https://www.malware-traffic-analysis.net/training-exercises.html) |
| [47](days/week-07/day-47-malware-basics-threat-intelligence-and-yara.md) | Malware basics, threat intelligence and YARA | Explain malware families, IOCs vs TTPs, the Pyramid of Pain, and write a YARA rule. | [link](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) |
| [48](days/week-07/day-48-threat-hunting-and-purple-teaming.md) | Threat hunting and purple teaming | Run a hypothesis-driven hunt and test a detection with an Atomic Red Team test. | [link](https://github.com/redcanaryco/atomic-red-team) |
| [49](days/week-07/day-49-week-7-review-and-tabletop-exercise.md) | Week 7 review and tabletop exercise | Run a tabletop and explain the SOC workflow end to end. | [link](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages) |

## Phase 8: Cloud, containers and DevSecOps (days 50-56)

**Goal:** Secure AWS, containers, Kubernetes and CI/CD, which is where your DevOps edge is biggest.

**Topics:** shared responsibility, AWS IAM, CloudTrail, GuardDuty, S3 security, IMDSv2, container hardening, image scanning, Kubernetes RBAC, Pod Security Standards, network policies, OWASP CI/CD Top 10, SLSA, SBOM, signing, SAST/SCA/DAST/IaC/secrets scanning, threat modeling with STRIDE.

**Milestone:** flAWS levels 1-4, a hardened image, a secured kind cluster, a DevSecOps pipeline and a threat model.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [50](days/week-08/day-50-cloud-security-fundamentals.md) | Cloud security fundamentals | Explain the shared responsibility model and the top cloud misconfigurations. | [link](https://aws.amazon.com/compliance/shared-responsibility-model/) |
| [51](days/week-08/day-51-aws-security-services-and-cloud-detection.md) | AWS security services and cloud detection | Explain CloudTrail, GuardDuty, Security Hub, SCPs and how to investigate in AWS. | [link](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) |
| [52](days/week-08/day-52-container-security.md) | Container security | Harden images and runtime, and explain container escape risks. | [link](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) |
| [53](days/week-08/day-53-kubernetes-security.md) | Kubernetes security | Secure a cluster with RBAC, Pod Security Standards, network policies and secrets handling. | [link](https://kubernetes.io/docs/concepts/security/pod-security-standards/) |
| [54](days/week-08/day-54-ci-cd-and-software-supply-chain-security.md) | CI/CD and software supply chain security | Explain the OWASP CI/CD Top 10, SLSA, SBOMs and how to harden GitHub Actions. | [link](https://owasp.org/www-project-top-10-ci-cd-security-risks/) |
| [55](days/week-08/day-55-appsec-tooling-in-the-pipeline-sast-sca-dast-iac-s.md) | AppSec tooling in the pipeline (SAST, SCA, DAST, IaC, secrets) | Build a security pipeline and explain what each tool class finds and misses. | [link](https://semgrep.dev/docs/) |
| [56](days/week-08/day-56-threat-modeling.md) | Threat modeling | Run a STRIDE threat model on a data flow diagram and turn threats into backlog items. | [link](https://www.threatmodelingmanifesto.org/) |

## Phase 9: GRC, architecture and capstone (days 57-60)

**Goal:** Talk risk and compliance with leadership, design secure systems, and prove it end to end.

**Topics:** risk management and RMF, policies standards and procedures, ISO 27001, SOC 2, PCI DSS, GDPR, secure design principles, security architecture, capstone, mock interview.

**Milestone:** Secure architecture doc, capstone report, recorded mock interview and a next-90-days plan.

| Day | Topic | You will be able to | Key resource |
|---|---|---|---|
| [57](days/week-09/day-57-governance-risk-and-compliance-grc.md) | Governance, risk and compliance (GRC) | Explain risk treatment, policies vs standards vs procedures, and what ISO 27001, SOC 2, PCI DSS and GDPR require. | [link](https://csrc.nist.gov/projects/risk-management/about-rmf) |
| [58](days/week-09/day-58-security-architecture-and-secure-design-principles.md) | Security architecture and secure design principles | Design a secure cloud architecture using defence in depth and secure design principles. | [link](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) |
| [59](days/week-09/day-59-capstone-attack-detect-respond-fix.md) | Capstone, attack, detect, respond, fix | Prove the fundamentals end to end in one exercise you can show in interviews. | [link](https://pwning.owasp-juice.shop/) |
| [60](days/week-09/day-60-sme-readiness-mock-interview-and-next-90-days.md) | SME readiness, mock interview and next 90 days | Answer fundamentals questions confidently and have a clear plan for the next level. | [link](https://www.comptia.org/en-us/certifications/security/) |

## After day 60

See [resources/RESOURCES.md](resources/RESOURCES.md) for certifications and specialisation paths, and write your plan on day 60.
