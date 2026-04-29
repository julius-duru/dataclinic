import streamlit as st
import pandas as pd

TITLE = "API‑First Automation & Security: A Practical Guide for Businesses"
CATEGORY = "misc"
KEYWORDS = [
    "Paystack", "Sendchamp", "Shippo", "Zapier",
    "API security", "CVE scanning", "API gateway", "WAF",
    "automation", "webhooks", "SMS notifications"
]

def show():
    st.title(TITLE)
    st.caption("Category: misc | Level: Beginner to Advanced | Real automation + actionable security")
    st.markdown("---")

    # INTRODUCTION – conversational hook
    st.write(
        """
       
        Its either that you run a business – or you’re building one. I am cock sure that you have heard about **APIs**, **webhooks**, and **automation**.
        Maybe you’ve even tried connecting Paystack, SMS, and shipping together.

        But then someone asks: *“What about API security? How do I protect against the latest CVEs?”*

        This guide answers both:  
        - **How to automate** order processing with Paystack, Sendchamp, Shippo & Zapier (using free tiers).  
        - **Which cybersecurity tools** actually protect APIs from real vulnerabilities and exploits.

        Just patterns, tool names, and a working end‑to‑end guide.
        """
    )
    st.markdown("---")

    # 1. THE BUSINESS PROBLEM: manual order processing
    st.header("The Old Way: Copy‑Paste Hell")
    st.write(
        """
        Imagine a small e‑commerce store, **XYZ Limited**.  
        Every time a customer pays via Paystack, someone manually:

        1. Checks Paystack dashboard for payment confirmation.  
        2. Types an SMS (“Thank you, we’re processing”).  
        3. Logs into Shippo to create a shipping label.  
        4. Copies the tracking number and sends another SMS.

        This takes **5–10 minutes per order**. At 50 orders/day, that’s a full person’s job – and mistakes happen.

        **The API‑first solution** → automate the whole thing. Paystack talks to Zapier, Zapier talks to Sendchamp and Shippo.  
        No human touches it unless something breaks.
        """
    )
    st.markdown("---")

    # 2. THE SOLUTION ARCHITECTURE (visual description)
    st.header("The Automated Flow (How APIs Talk to Applications)")
    st.write(
        """
        1. **Customer pays** → Paystack triggers a **webhook** (HTTP POST).  
        2. Zapier catches the webhook (free “Catch Hook” trigger).  
        3. Zapier calls Paystack API to **verify** the transaction (`/transaction/verify`).  
        4. **Filter** – only proceed if `status == "success"`.  
        5. Zapier calls **Sendchamp API** → sends order confirmation SMS.  
        6. Zapier calls **Shippo API** → creates a shipping label.  
        7. Zapier calls **Sendchamp again** → sends tracking number SMS.

        All steps finish in **< 10 seconds**.  
        The free tiers of Paystack (test mode), Sendchamp (sandbox), Shippo (test API), and Zapier (100 tasks/month) cover the pilot.
        """
    )
    st.markdown("---")

    # 3. CONFIGURATION SNAPSHOT (Zapier steps as a table)
    st.header("Zapier Steps – Your “No‑Code” Glue")
    st.write(
        "Below is the exact configuration for the Zap named `OAP – Paystack to Shippo + SMS`. "
        "Each action uses **Webhooks by Zapier** (POST requests)."
    )
    zap_steps_df = pd.DataFrame({
        "Step": ["1. Trigger", "2. Verify payment", "3. Filter", "4. SMS confirmation", "5. Create shipment", "6. SMS tracking"],
        "App/Method": ["Webhook (Catch Hook)", "POST to Paystack", "Filter by Zapier", "POST to Sendchamp", "POST to Shippo", "POST to Sendchamp"],
        "Key data extracted": ["reference, amount, phone", "status, customer_name", "status == success", "–", "tracking_number, carrier", "tracking_url"],
        "Free tier available?": ["Yes (Catch Hook)", "Yes (Paystack test keys)", "Yes", "Yes (Sendchamp sandbox)", "Yes (Shippo test token)", "Yes"]
    })
    st.dataframe(zap_steps_df, use_container_width=True, hide_index=True)

    with st.expander(" Real JSON payload to Sendchamp (SMS)", expanded=False):
        st.code(
            """
            {
              "to": "{{customer_phone}}",
              "message": "Hello {{customer_name}}, your payment of ₦{{amount}} was successful. Your order is being processed.",
              "sender_name": "XYZMart"
            }
            """,
            language="json"
        )
    st.markdown("---")

    # 4. API SECURITY VULNERABILITIES (OWASP Top 10 for APIs)
    st.header("API Security: Why It’s Not Optional")
    st.write(
        """
        APIs are now a **primary attack vector**. The OWASP API Security Top 10 (2023) lists the most common risks:

        - **API1: Broken Object Level Authorization (BOLA)** – User A sees User B’s data.  
        - **API2: Broken Authentication** – Weak API keys, missing token checks.  
        - **API3: Excessive Data Exposure** – Returning full database rows when only a name is needed.  
        - **API4: Lack of Rate Limiting** – One bot can DDoS your endpoint.  
        - **API5: Broken Function Level Authorization** – Regular user calling admin endpoints.  
        - **API6: Mass Assignment** – Attacker adds unexpected fields (e.g., `"is_admin": true`).  
        - **API7: Security Misconfiguration** – Default credentials, debug mode left on.  
        - **API8: Injection** – SQL, NoSQL, command injection via API parameters.  
        - **API9: Improper Inventory Management** – Old API versions still exposed.  
        - **API10: Unsafe Consumption of APIs** – Trusting third‑party APIs without validation.

        > **Key takeaway**: An API gateway or WAF alone won’t save you – you need specialised tools.
        """
    )
    st.markdown("---")

    # 5. CYBERSECURITY SOFTWARE FOR APIs (the requested list)
    st.header("Adequate Cybersecurity Software to Protect APIs from CVEs & Vulnerabilities")
    st.write(
        """
        The market is flooded. Here are **proven, production‑ready tools** categorised by what they do.  
        I’ve included both open‑source and commercial options – choose based on your budget and team size.
        """
    )

    # 5.1 API Gateways with built‑in security policies
    st.subheader(" API Gateways (Security-First)")
    security_gateways_df = pd.DataFrame({
        "Tool": ["Kong Gateway", "Tyk", "Apache APISIX", "Gravitee", "AWS API Gateway"],
        "Key Security Features": ["Plugin for WAF, OAuth2, JWT, rate limiting, CVE scanning (with Enterprise)", "OpenID Connect, mTLS, IP whitelisting, audit logs", "Plugin: Bot detection, ModSecurity, JWT", "WAF integration, anomaly detection, CSP headers", "AWS WAF + Shield, usage plans, resource policies"],
        "Open Source?": ["Yes (Core)", "Yes (Gateway OSS)", "Yes", "Yes (Community)", "No"],
        "Typical CVE Protection": ["Blocks known exploit patterns via ModSecurity CRS", "Rejects malformed tokens, rate‑limits CVEs' scanning activity", "Real‑time traffic inspection against OWASP rules", "Automatic signature updates", "Managed WAF rules cover many API CVEs"]
    })
    st.dataframe(security_gateways_df, use_container_width=True, hide_index=True)

    # 5.2 Dedicated API Security Scanners / SAST / DAST
    st.subheader(" API Security Testing & Vulnerability Scanners")
    sec_scanners_df = pd.DataFrame({
        "Tool": ["Postman + Postman Security Assistant", "Burp Suite (Professional)", "OWASP ZAP", "StackHawk", "Insomnia (with plugins)"],
        "Primary Use": ["Scan collections for common API vulns (BOLA, excess data)", "Manual & automated DAST, API fuzzing", "Open‑source API scanner, CI/CD integration", "Automated DAST for GraphQL/REST", "Local testing + custom scripts"],
        "CVE / Vuln Coverage": ["Detects API5, API6, API3", "Extensive (custom active scans for known CVEs)", "Community rules include OWASP Top 10", "Scans against known CVE patterns in API responses", "Manual – relies on user scripts"],
        "Free Tier?": ["Free for small collections", "Paid", "Yes (fully open source)", "Paid (trial available)", "Yes"]
    })
    st.dataframe(sec_scanners_df, use_container_width=True, hide_index=True)

    # 5.3 Web Application Firewalls (WAF) with API‑specific rules
    st.subheader(" Web Application Firewalls (API‑Aware WAFs)")
    waf_df = pd.DataFrame({
        "Tool": ["Cloudflare WAF (API Shield)", "ModSecurity (with CRS)", "AWS WAF", "Wallarm API Security", "Imperva API Security"],
        "Strength for APIs": ["JSON deep inspection, rate limiting, schema validation", "Open‑source, supports custom rules for API paths", "Managed rules for API protocols, bot control", "Built for APIs – BOLA detection, GraphQL parsing", "API discovery, CVE‑specific threat research"],
        "Deployment": ["Cloud (CDN)", "On‑prem / reverse proxy", "Cloud (AWS)", "Cloud, K8s sidecar", "Cloud or appliance"],
        "CVE Protection": ["Blocks attempts to exploit known API CVEs (e.g., CVE‑2023‑44487 – HTTP/2 Rapid Reset)", "Community CRS includes many API‑related CVEs", "AWS Shield Advanced handles zero‑day", "Threat research team updates rules within hours", "Global threat intelligence"]
    })
    st.dataframe(waf_df, use_container_width=True, hide_index=True)

    # 5.4 Runtime API Protection / RASP
    st.subheader(" Runtime API Protection (RASP / Active Defense)")
    runtime_df = pd.DataFrame({
        "Tool": ["Traceable AI", "Noname Security", "Salt Security", "Cequence Security", "DataDog API Security"],
        "How it works": ["eBPF + ML to detect BOLA, API abuse", "Passive traffic analysis + active testing", "ML models on API behaviour", "Unified API protection platform", "Integration with DataDog APM"],
        "CVE Focus": ["Detects exploitation of known CVEs via behavioural anomalies", "Compares traffic against known exploit signatures", "Discovers shadow APIs, alerts on CVSS≥7 activity", "Blocks automated scanners looking for CVEs", "Correlates CVE database with API calls"]
    })
    st.dataframe(runtime_df, use_container_width=True, hide_index=True)

    # 5.5 CVE‑specific API vulnerability databases & alerting
    st.subheader(" CVE Feeds & API‑Specific Alerting")
    st.markdown(
        """
        - **NVD (National Vulnerability Database)** – free, but slow.  
        - **CVE.org** – raw data.  
        - **Snyk** – scans your API dependencies (Node, Python, Java) for known CVEs in HTTP libraries.  
        - **GitHub Dependabot** – alerts when your API framework (Express, FastAPI, etc.) has a security advisory.  
        - **Rapid7 VulnDB** – commercial, but faster than NVD for zero‑days.  
        - **Wiz / Orca** – cloud‑native API scanners that correlate CVEs with deployed API gateways.
        """
    )
    st.markdown("---")

    # 6. REAL‑WORLD CASE STUDY: Securing the Paystack + Zapier automation
    st.header("Applying Security to Our Automation Example")
    st.write(
        """
        Let’s harden the Paystack → Zapier → Sendchamp → Shippo pipeline using real tools from above.
        """
    )
    security_actions_df = pd.DataFrame({
        "Layer": ["Incoming webhook", "Zapier itself", "Outbound API calls", "Customer data at rest", "Monitoring"],
        "Risk": ["Fake Paystack webhook (spoofed signature)", "Zapier account takeover", "API keys leaked in logs", "Customer PII (phone, address) exposed", "Slow detection of exploitation"],
        "Recommended Tool/Method": [
            "Verify `x-paystack-signature` using a Code step (HMAC‑SHA512) – prevents CVE‑202x‑any spoofing.",
            "Enable MFA on Zapier account; limit team access (least privilege).",
            "Store API keys in Zapier’s encrypted environment variables (paid plan) or use a secret manager (HashiCorp Vault + 'Webhook' action).",
            "Use DataDog API Security or Traceable AI to monitor data exfiltration patterns.",
            "Deploy OWASP ZAP in a weekly cron job to scan the Zapier webhook URL for BOLA / SQLi."
        ]
    })
    st.dataframe(security_actions_df, use_container_width=True, hide_index=True)

    st.info(
        "**Pro tip**: Even on a budget, you can use **OWASP ZAP** (free) to scan your webhook endpoint for common CVEs. "
        "And always, always validate webhook signatures – many breaches start with forged webhooks."
    )
    st.markdown("---")

    # 7. DECISION FRAMEWORK: Which security tool fits your stage?
    st.header("Decision Framework – API Security Tools by Company Stage")
    st.write(
        """
        | Stage | Typical API Volume | Recommended Tools (Lowest cost / highest ROI) |
        |-------|--------------------|------------------------------------------------|
        | **Startup / MVP** | < 10 API calls/day | OWASP ZAP (scan every release), API key + rate limiting (manual), GitHub Dependabot |
        | **Growing SME** | 100–10k calls/day | Cloudflare WAF (free tier), Kong OSS + ModSecurity, Postman Security Assistant |
        | **Enterprise** | 1M+ calls/day | Apigee / AWS WAF, Traceable AI, Noname Security, dedicated CVE scanning pipeline |
        """
    )
    st.markdown("---")

    # 8. RESOURCES & NEXT STEPS
    st.header("Resources")
    st.write(
        """
        - **Learn API Security** → [OWASP API Security Project](https://owasp.org/www-project-api-security/)  
        - **CVE database for APIs** → [Snyk Vulnerability DB](https://security.snyk.io/) (filter by “API”)  
        - **Automate your Zapier security** → [Zapier’s security best practices](https://zapier.com/learn/security/)  
        """
    )
    st.markdown("---")

    # CONCLUSION
    st.markdown(
        """
        **Final Takeaway**

        APIs are the engines of modern business – but without proper security, they’re unlocked doors.  
        You don’t need a six‑figure budget. Start with **OWASP ZAP** + **API key rotation** + **webhook signature verification**.  
        Then add a free WAF (Cloudflare) and a dependency scanner (Dependabot). That covers 80% of CVEs targeting APIs.

        And remember: automation without security is just faster chaos.  
        Build smart. Build secure.

        """
    )
    st.markdown("---")
    st.caption("API‑First Automation & Security | Real tools, real stories ")