# Lab setup

Your lab is a set of containers on one Docker network. You can rebuild it in a minute, break it on purpose, and throw it away. Set it up on day 4.

## What you need

| Tool | Why | Used from |
|---|---|---|
| Docker Desktop or Docker Engine with Compose v2 | Runs the whole lab | Day 4 |
| Wireshark | Packet analysis | Day 11 |
| Burp Suite Community Edition | Web proxy | Day 27 |
| A free PortSwigger account | Web Security Academy labs | Day 20 |
| A free TryHackMe account | Browser-based Windows, AD, Metasploit and SIEM rooms | Day 16 |
| kind and kubectl | Local Kubernetes | Day 53 |
| Python 3.10+ | Scripts, hashing labs, sigma-cli, the Notion sync | Throughout |
| Optional: a personal AWS account with billing alerts | Prowler and CloudTrail labs | Day 51 |

Downloads:

- Docker: https://docs.docker.com/get-started/get-docker/
- Wireshark: https://www.wireshark.org/download.html
- Burp Suite Community: https://portswigger.net/burp/communitydownload
- kind: https://kind.sigs.k8s.io/

## Start the lab

```bash
docker compose -f labs/docker-compose.yml up -d
docker compose -f labs/docker-compose.yml ps
```

| Service | URL from your machine | Hostname inside the lab |
|---|---|---|
| OWASP Juice Shop | http://localhost:3000 | `juice-shop:3000` |
| DVWA | http://localhost:8081 (login `admin` / `password`, then click **Create / Reset Database**) | `dvwa:80` |
| Ubuntu target | none | `target` |
| Kali attacker | none | `attacker` |

Get a shell on the attacker box and install the basics once:

```bash
docker compose -f labs/docker-compose.yml exec attacker bash
apt update && apt install -y nmap tcpdump netcat-traditional curl dnsutils iproute2 hydra john
```

Get a shell on the target:

```bash
docker compose -f labs/docker-compose.yml exec target bash
apt update && apt install -y openssh-server lynis nftables cron
```

## Safety rules

1. Published ports are bound to `127.0.0.1`, so nothing in the lab is reachable from your network. Keep it that way.
2. Only attack the lab, PortSwigger labs, TryHackMe machines, `scanme.nmap.org` (which Nmap's authors explicitly allow light scanning of), and flAWS. Anything else needs written permission, even "just a scan".
3. Malware samples and malicious pcaps go in a separate VM, never on your work laptop.
4. Never commit real passwords, keys or flags. Commit techniques and evidence.

## Reset

```bash
docker compose -f labs/docker-compose.yml down -v   # wipe everything, including databases
docker compose -f labs/docker-compose.yml up -d
```

## Why Docker and not a stack of VMs

You already think in containers, and a Compose file is reproducible, versioned and quick to reset. When a lab needs a full OS (Windows, Active Directory), the plan uses TryHackMe's browser VMs so you don't have to build them in week 3. If you want a full Kali VM later, see https://www.kali.org/get-kali/.
