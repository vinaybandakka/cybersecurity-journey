# Capstone: attack, detect, respond, fix

Day 59. One exercise that touches every phase. It becomes the story you tell in interviews.

## Scenario

You are the only security engineer at a small company that runs OWASP Juice Shop in production. Someone reports that an attacker logged in as the administrator.

## Steps (45 minutes, plus extra time if you want to polish)

### 1. Attack (10 min), in your lab only

- Start the lab: `docker compose -f labs/docker-compose.yml up -d`.
- Use Burp to log in as the Juice Shop admin with a SQL injection in the email field.
- Save the request and response as evidence.

### 2. Detect (10 min)

- Pull the logs: `docker compose -f labs/docker-compose.yml logs juice-shop > capstone/juice-shop.log`.
- Find the malicious login attempt with grep or jq.
- Write a Sigma rule in `detections/juice-shop-sqli-login.yml` that would flag SQL metacharacters in login requests.

### 3. Respond (10 min)

Use [labs/templates/ir-playbook.md](../labs/templates/ir-playbook.md) to write a short incident report in `capstone/REPORT.md`:

- Timeline, scope, ATT&CK technique IDs (T1190 Exploit Public-Facing Application, T1078 Valid Accounts).
- Containment: what you would do in the first hour (rotate admin credentials, invalidate sessions, temporary WAF rule).
- Evidence collected.

### 4. Fix (10 min)

- Find the vulnerable login query in the Juice Shop source (`routes/login.ts`) and write the parameterised fix.
- Describe the pipeline control that would have caught it (a Semgrep rule for string-built SQL, plus a ZAP baseline scan).

### 5. Present (5 min)

Record a 5-minute walkthrough: what happened, how you found it, what you fixed, and what you changed so it can't happen again.

## What "done" looks like

- [ ] `capstone/REPORT.md` with timeline, impact, root cause, containment, fix and lessons learned
- [ ] `detections/juice-shop-sqli-login.yml`
- [ ] The code fix and pipeline control described
- [ ] A recorded walkthrough (keep the file outside git if it's large)
