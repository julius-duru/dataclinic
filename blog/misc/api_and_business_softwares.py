import streamlit as st
import pandas as pd

TITLE = "APIs & Business Software Integration"
CATEGORY = "misc"
KEYWORDS = [
    "APIs", "business software", "REST", "GraphQL", "API gateways",
    "integration patterns", "API security", "CRM", "ERP", "Accounting", "HR", "Supply Chain",  "open source", "SaaS"
]

def show():
    st.title(TITLE)
    st.caption("Category: misc | Level: Beginner to Advanced | Real‑world stories, trade‑offs, and actionable advice")
    st.markdown("---")

    # INTRODUCTION – conversational
    st.write(
        """
        You’ve probably heard “API”  – but maybe you’re still wondering: *Is it just a fancy way for apps to talk?*  
        Or you’re an experienced dev who’s tired of yet another “what is REST” tutorial.

        Either way, this guide is for you. We’ll cover why APIs are the secret sauce of modern business,  
        how to choose between REST, GraphQL, and gRPC, when to reach for an API gateway, and real‑world patterns that actually work.  
        I’ve packed in war stories, honest trade‑offs, and a decision framework that respects your time.

        """
    )
    st.markdown("---")

    # 1. WHAT ARE APIS? (short, conversational)
    st.header("What is API?")
    st.write(
        """
        Imagine you are at a restaurant. You don’t walk into the kitchen and grab ingredients.  
        You tell a waiter (the API) what you want, and the waiter brings it from the kitchen (the server).  
        The menu is the documentation, and the waiter’s rules are the protocol.

        In business terms: an API is a contract. “If you ask me this way, I promise to give you that result – or a clear error.”  
        APIs let your CRM talk to your email marketing tool, your payment gateway, your warehouse – all without human copy‑paste.

        **Why should you care?** Because APIs automate the boring stuff. And automation saves money.
        """
    )
    st.markdown("---")

    # 2. TYPES OF APIS – with trade‑offs table
    st.header("Types of APIs – Who Gets to Play?")
    st.write(
        """
        Not all APIs are created equal. Some are free for the world, others are locked inside a company.
        """
    )
    api_types_df = pd.DataFrame({
        "Type": ["Open (Public)", "Internal (Private)", "Partner", "Composite"],
        "Access": ["Anyone", "Only within your org", "Approved business partners", "Your own backend"],
        "Example": ["OpenWeatherMap, Pokémon API", "HR system → payroll", "Stripe for payment processors", "Checkout that bundles price + tax + shipping"],
        "Typical Use": ["Learning, prototyping", "Internal automation", "B2B integrations", "Reduce round trips"]
    })
    st.dataframe(api_types_df, use_container_width=True, hide_index=True)
    st.markdown("---")

    # 3. PROTOCOLS & ARCHITECTURE – REST vs GraphQL vs gRPC vs SOAP
    st.header("Protocols: The Language of APIs")
    st.write(
        """
        You don’t need to master all of them. But knowing the trade‑offs will save you from painful rewrites.
        """
    )
    protocol_df = pd.DataFrame({
        "Protocol": ["REST", "GraphQL", "gRPC", "SOAP"],
        "Style": ["Resource‑oriented", "Query language", "RPC (Remote Procedure Call)", "XML‑based"],
        "Best for": ["80% of web APIs", "Dashboards / mobile (over‑fetching pain)", "Microservices ↔ microservices", "Legacy enterprise / banking"],
        "Learning curve": ["Low", "Medium", "High", "High"],
        "Vibe": ["The reliable default", "The precise surgeon", "The speed demon", "The old gentleman"]
    })
    st.dataframe(protocol_df, use_container_width=True, hide_index=True)

    with st.expander("War story: GraphQL saved their mobile app", expanded=False):
        st.info(
            "A travel app’s REST endpoint returned 50 fields – but the mobile app only needed 3. Users waited 2 seconds for useless data. "
            "Switching to GraphQL cut latency to 300ms and data usage by 90%. The team slept better."
        )
    st.markdown("---")

    # 4. BUSINESS SOFTWARE LANDSCAPE
    st.header("Business Software – The Islands You Need to Connect")
    st.write(
        """
        Every business runs on a zoo of software: CRM, ERP, accounting, HR, supply chain.  
        Without APIs, these are islands. With APIs, they become a connected archipelago.
        """
    )
    biz_software_df = pd.DataFrame({
        "Category": ["CRM", "ERP", "Accounting", "HR", "Supply Chain"],
        "What it does": ["Sales, support, leads", "Finance + HR + ops", "Invoices, expenses", "Payroll, recruiting", "Inventory, logistics"],
        "Popular examples": ["Salesforce, HubSpot", "SAP, Oracle NetSuite", "QuickBooks, Xero", "BambooHR, Workday", "Blue Yonder, Manhattan"]
    })
    st.dataframe(biz_software_df, use_container_width=True, hide_index=True)
    st.markdown("---")

    # 5. ROLE OF APIS – automation, sync, customer experience
    st.header("Why APIs Matter in Business (Not Just Tech)")
    st.write(
        """
        APIs aren’t a “nice to have”. They directly affect your bottom line:

        - **Automation** – Invoice paid → API triggers warehouse shipment → API updates inventory → API marks order complete. No human touches it.
        - **Data sync** – Customer changes address on your website → API updates CRM, ERP, and shipping provider – all at once.
        - **Customer experience** – Real‑time delivery tracking (DoorDash, Uber) is just APIs talking to each other.
        - **Digital transformation** – A 1980s bank can expose an API and suddenly become a fintech.

        > If your business software doesn’t have an API, you’re living in the dark ages.
        """
    )
    st.markdown("---")

    # 6. INTEGRATION PATTERNS (point‑to‑point, ESB, iPaaS, API gateway)
    st.header("Integration Patterns – How to Glue Everything Together")
    st.write(
        """
        You have four main options. The right one depends on your size, budget, and patience.
        """
    )
    patterns_df = pd.DataFrame({
        "Pattern": ["Point‑to‑point", "ESB (Enterprise Service Bus)", "iPaaS (Zapier, MuleSoft)", "API Gateway"],
        "When it works": ["2‑3 apps only", "Large on‑prem enterprises", "Cloud‑native SMEs", "Any size, especially microservices"],
        "Downside": ["Spaghetti after 4 apps", "Heavy, expensive", "Can get pricey at scale", "One more thing to manage"],
        "Example": ["QuickBooks → Salesforce direct", "IBM Integration Bus", "Zapier connecting 50 SaaS tools", "Kong / Apigee"]
    })
    st.dataframe(patterns_df, use_container_width=True, hide_index=True)

    st.subheader("War story: The 12‑way point‑to‑point nightmare")
    st.info(
        "A mid‑sized retailer connected 12 SaaS tools directly. When the CRM changed a field name, 5 integrations broke. "
        "They spent a week debugging. After moving to an iPaaS (Workato), changes took hours, not days."
    )
    st.markdown("---")

    # 7. API SECURITY – auth methods, common pitfalls
    st.header("API Security: Don’t Be the Next Headline")
    st.write(
        """
        APIs are a favourite attack vector. The **OWASP API Top 10** is your must‑read checklist.
        """
    )
    auth_df = pd.DataFrame({
        "Method": ["API Key", "OAuth 2.0", "JWT"],
        "How it works": ["Shared secret in header", "User delegates access", "Self‑contained token"],
        "Best for": ["Low‑risk public APIs", "Third‑party apps (Login with Google)", "Microservices, stateless auth"],
        "Risk": ["Can be leaked", "Complex flow", "Token revocation is hard"]
    })
    st.dataframe(auth_df, use_container_width=True, hide_index=True)

    st.subheader("Common vulnerabilities (quick & practical)")
    st.markdown(
        """
        - **Broken object level authorisation** – User A sees User B’s data because you forgot to check `user_id`.  
        - **Excessive data exposure** – Returning the whole database row when the client only needs a name.  
        - **Lack of rate limiting** – One bad actor can DDoS your API. Use `429 Too Many Requests`.

        **Rule of thumb**: Never trust the client. Validate everything. Use HTTPS everywhere.
        """
    )
    st.markdown("---")

    # 8. API MANAGEMENT – gateways, monitoring, developer portals
    st.header("API Management – The Grown‑Up Stuff")
    st.write(
        """
        Once you have more than a handful of APIs, you need a control plane. Enter **API gateways**.
        """
    )
    gateways_df = pd.DataFrame({
        "Gateway": ["Kong", "Apigee", "AWS API Gateway", "Tyk"],
        "Strengths": ["Open‑source, plugin‑rich", "Enterprise analytics", "Serverless tight integration", "Dev‑friendly, self‑hostable"],
        "Typical user": ["Startups to enterprises", "Large enterprises", "AWS shops", "Kubernetes teams"]
    })
    st.dataframe(gateways_df, use_container_width=True, hide_index=True)

    st.write(
        """
        A gateway handles **authentication, rate limiting, logging, and routing**.  
        Plus, you’ll want a **developer portal** (SwaggerHub, ReadMe) so partners can discover and test your API.
        """
    )
    st.markdown("---")

    # 9. REAL‑WORLD USE CASES + SPECIALISED APIS (Music, Video, Stock, Aviation, Marine, Language)
    st.header("Real‑World APIs You Can Use Today")
    st.write(
        """
        APIs aren’t just for payments and CRM. Here are specialised APIs that power amazing products – many with free tiers.
        """
    )

    with st.expander(" Music APIs", expanded=False):
        st.markdown("Spotify Web API, Deezer, SoundCloud, AcoustID – build your own playlist app, identify songs, or fetch metadata.")
    with st.expander(" Video APIs", expanded=False):
        st.markdown("YouTube Data API, Mux, api.video – upload, transcode, and stream video programmatically.")
    with st.expander(" Stock & Financial APIs", expanded=False):
        st.markdown("Alpha Vantage (free tier), FCS API (500 calls/day free), iTick (unlimited free basic data), Finnhub.")
    with st.expander(" Aviation APIs", expanded=False):
        st.markdown("AviationStack (flight status), OpenSky Network (live aircraft positions, free for research).")
    with st.expander(" Marine APIs", expanded=False):
        st.markdown("Marinesia (AIS vessel tracking), aisstream.io (free WebSocket AIS data).")
    with st.expander(" Language APIs", expanded=False):
        st.markdown("DeepL (great free tier), Google Cloud Translation, LibreTranslate (open source), Azure AI Language.")

    st.subheader("Use case: Payment Integration (FinTech)")
    st.info(
        "An e‑commerce startup used Paystack API + Sendchamp SMS API + Shippo logistics API with Zapier. "
        "Order‑to‑delivery dropped from 48 hours to 6 hours. They now handle 10x orders with the same staff."
    )
    st.markdown("---")

    # 10. DECISION FRAMEWORK (like the pipeline guide)
    st.header("Decision Framework: Which API Pattern / Tool Should You Choose?")
    st.write(
        """
        Ask these questions – they have saved teams from over‑engineering (and under‑engineering).

        1. **How many apps do you need to connect?**  
           - 2–3 → Point‑to‑point is fine.  
           - 4–10 → Consider an iPaaS (Zapier, Make).  
           - 10+ microservices → API gateway + maybe ESB.

        2. **What’s your team’s skill set?**  
           - Mostly business users → No‑code iPaaS (Zapier).  
           - Developers who know HTTP → REST + OpenAPI.  
           - Hardcore backend engineers → gRPC, Kafka, event‑driven.

        3. **Do you need real‑time sync?**  
           - No (nightly batch is fine) → REST + scheduled jobs.  
           - Yes (under 1 second) → WebSockets or gRPC streaming.

        4. **How sensitive is your data?**  
           - Low → API key auth.  
           - High (PII, payments) → OAuth 2.0 + mTLS + rate limiting.

        5. **What’s your budget?**  
           - $0 → Free tiers of public APIs + cURL.  
           - $50/month → Zapier / Make.  
           - Enterprise → MuleSoft, Apigee, dedicated gateway team.

        **Way to go:**  
        - Start with REST + OpenAPI. It’s the most forgiving.  
        - Use an iPaaS for internal glue (it beats writing custom connectors).  
        - Add authentication early – retrofitting OAuth is painful.  
        - Document as you build – your future self will thank you.
        """
    )
    st.markdown("---")

    # 11. SUMMARY TABLE (patterns at a glance)
    st.header("Patterns & Tools at a Glance")
    summary_api_df = pd.DataFrame({
        "Scenario": ["Learning / Prototyping", "Internal automation (few apps)", "Cloud‑native SME", "Enterprise / Microservices", "Real‑time data"],
        "Recommended pattern": ["Public REST APIs", "iPaaS (Zapier)", "ELT + REST APIs", "API Gateway + OpenAPI", "WebSocket / gRPC"],
        "Example tools": ["OpenWeatherMap, Pokémon API", "Zapier, Make", "Stripe, Salesforce API", "Kong, Apigee", "Socket.IO, gRPC"]
    })
    st.dataframe(summary_api_df, use_container_width=True, hide_index=True)
    st.markdown("---")

    # 12. RESOURCES – training, books, communities
    st.header("Top Resources ")
    st.write(
        """
        Here are API resources that respect your time – for beginners and advanced.
        """
    )
    resources_api_df = pd.DataFrame({
        "Category": ["Free Courses", "Books", "Interactive Tools", "Communities", "Documentation Standards"],
        "Recommendations": [
            "Postman API Fundamentals (Student Expert), freeCodeCamp's 'APIs for Beginners' (YouTube)\nCoursera: API Design (Google Cloud)",
            "Designing Web APIs – Brail & Goldberg\nThe Design of Web APIs – Arnaud Lauret",
            "Postman, Insomnia, reqbin.com, RapidAPI Hub",
            "r/api (Reddit), API‑related Slack groups (Postman community)\nAPIs You Won't Hate (newsletter)",
            "OpenAPI Specification (Swagger)\nJSON:API, RESTful API guidelines by Microsoft"
        ]
    })
    st.dataframe(resources_api_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown(
        """
        **Summary**  

        Right use and integration of APIs is business strategy.  
        The companies that win in the next decade will be those that treat APIs as products – with documentation, versioning, and a developer experience that doesn't suck.

        **Insight:**  
        - Start small. A single public API call (weather, stock, or cat facts) is enough to learn.  
        - Always handle errors. Your users will see a blank screen if you don't.  
        - Rate limit everything. One bad bot can ruin your month.  
        - Don't build a custom integration if a $20/month iPaaS exists.

        You now have the framework to navigate the API development. Go build something that connects.

        """
    )
    st.markdown("---")
    st.caption("APIs & Business Software | Conversational guide for newbies and pros")