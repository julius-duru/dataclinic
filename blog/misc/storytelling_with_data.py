import streamlit as st
import pandas as pd

TITLE = "Storytelling with Data across Business Verticals"
CATEGORY = "misc"
KEYWORDS = ["data analytics", "business verticals", "executive storytelling", "KPIs", "healthcare analytics", "finance analytics", "marketing analytics", "retail analytics", "SaaS analytics", "public sector analytics", "business intelligence", "data strategy"]


def show():

    st.title("Storytelling with Data across Business Verticals")
    st.caption("Category: misc | Level: Beginner → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        This article is forAspiring analysts, Data scientists and Analytics leaders  
        The Core themes include executive storytelling, industry-specific project blueprints, KPIs that link data work to business value (revenue, cost, risk, efficiency, innovation) 
        
        **Why This Guide Matters**
        
        - **If you are a beginner analyst:** You will learn how to structure projects around business outcomes—not just queries or charts. You'll see how KPIs connect to real decisions.
        - **If you are an experienced data professional:** You will gain a reusable C-level storytelling framework, cross-industry benchmarking references, and language that turns technical 
          insights into strategic influence.
        
        > Winning organizations usually ask, "How quickly can we turn data into insights?"
        
        Below, we present six industry analytics portfolios, followed by a universal executive storytelling model—and the core skills required at every level.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 1: Healthcare Analytics
    # ============================================
    st.header("1. Healthcare Analytics")
    
    st.write(
        """
        **Strategic narrative:**  
        > "Healthcare saves more lives and reduces waste when decisions are driven by prediction, not reaction."
        """
    )
    
    healthcare_data = {
        "Project Feature": ["Early disease detection", "Preventive care insights", "Insurance claim risk profiling", "Resource optimization", "Patient outcome forecasting"],
        "Beginner Focus": [
            "Build a simple logistic regression for readmission risk",
            "Segment patients by age/chronic conditions",
            "Flag high-cost claims via thresholds",
            "Visualize bed occupancy trends",
            "Track mortality rates over time"
        ],
        "Advanced / Lead Focus": [
            "Deploy survival models or deep learning on EHR sequences",
            "Causal inference on intervention effectiveness",
            "Anomaly detection + fraud graph networks",
            "Simulate staffing needs via discrete-event simulation",
            "Build real-time risk prediction dashboards"
        ]
    }
    df_healthcare = pd.DataFrame(healthcare_data)
    st.dataframe(df_healthcare, use_container_width=True)
    
    st.write("**Executive KPIs (what leadership tracks):**")
    
    kpi_healthcare = {
        "Executive Concern": ["Quality of care", "Cost optimization", "Risk reduction", "Operational efficiency"],
        "Strategic KPI": [
            "Mortality rate, readmission rate, diagnostic accuracy",
            "Cost per patient, resource utilization %, claim leakage",
            "Fraudulent claims rate, infection spread forecast accuracy",
            "Appointment lead time, staff productivity index"
        ]
    }
    df_kpi_hc = pd.DataFrame(kpi_healthcare)
    st.dataframe(df_kpi_hc, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 2: Finance & Banking Analytics
    # ============================================
    st.header("2. Finance & Banking Analytics")
    
    st.write(
        """
        **Strategic narrative:**  
        > "Data turns lending and trading from instinct into automated, auditable advantage."
        """
    )
    
    finance_data = {
        "Project Feature": ["Credit scoring systems", "Fraud detection", "Loan approval automation", "Revenue & liquidity forecasting", "Portfolio optimization"],
        "Beginner Focus": [
            "Build a scorecard with logistic regression",
            "Rule-based flags + SQL joins",
            "Automate reporting of approval rates",
            "Time-series plots (ARIMA baseline)",
            "Calculate Sharpe ratio and basic diversification"
        ],
        "Advanced / Lead Focus": [
            "XGBoost + fairness constraints, regulatory explainability",
            "Real-time ML with graph features (transaction networks)",
            "End-to-end decision engine with A/B testing",
            "Multi-scenario ensemble + stress testing",
            "Factor models + Monte Carlo simulation"
        ]
    }
    df_finance = pd.DataFrame(finance_data)
    st.dataframe(df_finance, use_container_width=True)
    
    st.write("**Executive KPIs:**")
    
    kpi_finance = {
        "Concern": ["Risk", "Revenue", "Efficiency", "Customer value"],
        "KPI": [
            "Loan default rate, VaR, fraud detection rate",
            "Interest income forecast accuracy, cross-sell lift",
            "Loan approval turnaround time, cost-to-income ratio",
            "CLV, product penetration rate"
        ]
    }
    df_kpi_fin = pd.DataFrame(kpi_finance)
    st.dataframe(df_kpi_fin, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 3: Technology & SaaS Analytics
    # ============================================
    st.header("3. Technology & SaaS Analytics")
    
    st.write(
        """
        **Strategic narrative:**  
        > "Usage patterns predict revenue. Analytics drives stickiness and recurring growth."
        """
    )
    
    saas_data = {
        "Project Feature": ["Real-time user behavior tracking", "Subscription lifecycle analytics", "Churn prediction models", "A/B testing for product features", "Error detection and stability monitoring"],
        "Beginner Focus": [
            "Event funnels in Amplitude/Mixometer",
            "Cohort retention tables",
            "Build a binary classifier (random forest)",
            "T-test on conversion rates",
            "Dashboard for 5xx errors"
        ],
        "Advanced / Lead Focus": [
            "Real-time feature stores + cohort retention matrices",
            "Survival analysis + uplift modeling for interventions",
            "Sequential testing / CUPED for variance reduction",
            "Anomaly detection ",
            "Root cause clustering"
        ]
    }
    df_saas = pd.DataFrame(saas_data)
    st.dataframe(df_saas, use_container_width=True)
    
    st.write("**Executive KPIs:**")
    
    kpi_saas = {
        "Objective": ["Growth", "Customer health", "Operational excellence", "Profitability"],
        "KPI": [
            "MRR, ARR, net revenue retention (NRR)",
            "Churn rate, DAU/MAU ratio, feature adoption",
            "Server error rate, app latency, release stability index",
            "Gross margin, user acquisition cost efficiency"
        ]
    }
    df_kpi_saas = pd.DataFrame(kpi_saas)
    st.dataframe(df_kpi_saas, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 4: E-Commerce & Retail Analytics
    # ============================================
    st.header("4. E-Commerce & Retail Analytics")
    
    st.write(
        """
        **Strategic narrative:**  
        > "Browsing behavior becomes revenue and loyalty when analytics connects every click to a business lever."
        """
    )
    
    retail_data = {
        "Project Feature": ["Price elasticity tracking", "Market basket analysis", "Customer segmentation & CLV prediction", "Personalization engines", "Supply chain demand forecasting"],
        "Beginner Focus": [
            "Linear regression on log(price) vs. units",
            "Association rules (Apriori)",
            "RFM segmentation",
            "Simple collaborative filtering",
            "Moving averages / ETS"
        ],
        "Advanced / Lead Focus": [
            "Bayesian structural time series for causal impact",
            "Next-best-action models with sequence-aware networks",
            "Probabilistic BG/NBD + Gamma-Gamma",
            "Multi-armed bandits for real-time personalization",
            "Hierarchical forecasting with exogenous regressors"
        ]
    }
    df_retail = pd.DataFrame(retail_data)
    st.dataframe(df_retail, use_container_width=True)
    
    st.write("**Executive KPIs:**")
    
    kpi_retail = {
        "Focus": ["Revenue", "Customer loyalty", "Efficiency", "Digital experience"],
        "KPI": [
            "AOV, conversion rate, promotion ROI",
            "Repeat purchase rate, return rate, CLV",
            "Inventory turnover, logistics cost ratio",
            "Cart abandonment, checkout time, UX performance index"
        ]
    }
    df_kpi_ret = pd.DataFrame(kpi_retail)
    st.dataframe(df_kpi_ret, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 5: Marketing Analytics
    # ============================================
    st.header("5. Marketing Analytics")
    
    st.write(
        """
        **Strategic narrative:**  
        > "Marketing becomes a profit center when every dollar's journey is quantified and optimized."
        """
    )
    
    marketing_data = {
        "Project Feature": ["Attribution modeling across channels", "Budget optimization models", "Predictive lead scoring", "Campaign performance intelligence", "Sentiment analysis"],
        "Beginner Focus": [
            "Last-click or linear attribution",
            "Excel solver for channel spend",
            "Logistic regression on CRM data",
            "ROI calculation per channel",
            "VADER or TextBlob"
        ],
        "Advanced / Lead Focus": [
            "Markov chains / Shapley value / MTA",
            "Multi-touch optimization with ROAS constraints",
            "Gradient boosting + calibration for probability outputs",
            "Media mix modeling (MMM) with Bayesian priors",
            "Fine-tuned BERT for brand-specific language"
        ]
    }
    df_marketing = pd.DataFrame(marketing_data)
    st.dataframe(df_marketing, use_container_width=True)
    
    st.write("**Executive KPIs:**")
    
    kpi_marketing = {
        "Priority": ["Profitability", "Audience insights", "Customer value", "Brand health"],
        "KPI": [
            "ROAS, CAC, marketing efficiency ratio",
            "Segmentation precision, engagement score",
            "Retention rate, CLV expansion",
            "NPS, sentiment index"
        ]
    }
    df_kpi_mkt = pd.DataFrame(kpi_marketing)
    st.dataframe(df_kpi_mkt, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 6: Government & Public Sector
    # ============================================
    st.header("6. Government & Public Sector Analytics")
    
    st.write(
        """
        **Strategic narrative:**  
        > "Data makes public services fairer, faster, and more effective—without increasing budgets."
        """
    )
    
    govt_data = {
        "Project Feature": ["Crime pattern modeling", "Infrastructure planning via geospatial analytics", "Housing affordability forecasting", "Budget allocation optimization", "Loan and welfare management systems"],
        "Beginner Focus": [
            "Hotspot maps (time of day / location)",
            "Population density overlays",
            "Linear regression on economic indicators",
            "Variance reports vs. plan",
            "Eligibility dashboards"
        ],
        "Advanced / Lead Focus": [
            "Spatiotemporal forecasting + intervention evaluation",
            "Geospatial optimization for school/hospital placement",
            "Hedonic pricing models + policy simulation",
            "Zero-based budgeting with outcome prediction",
            "Fraud/error detection + equitable distribution algorithms"
        ]
    }
    df_govt = pd.DataFrame(govt_data)
    st.dataframe(df_govt, use_container_width=True)
    
    st.write("**Executive KPIs:**")
    
    kpi_govt = {
        "Priority": ["Safety", "Budget", "Social impact", "Policy outcomes"],
        "KPI": [
            "Crime reduction %, response time efficiency",
            "Utilization accuracy, cost savings from optimization",
            "Homelessness reduction, benefit distribution accuracy",
            "Housing index stability, program adoption rate"
        ]
    }
    df_kpi_gov = pd.DataFrame(kpi_govt)
    st.dataframe(df_kpi_gov, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 7: The 5-Step Storytelling Framework
    # ============================================
    st.header("7. The 5-Step Storytelling Framework for Any Analyst")
    
    st.write(
        """
        *To influence leadership, you must translate technical work into business narratives.*
        """
    )
    
    storytelling_data = {
        "Step": [
            "1. Define the business challenge",
            "2. Show financial or strategic impact",
            "3. Use metaphors & simple visuals",
            "4. Recommend clear actions",
            "5. Communicate risks & ROI"
        ],
        "Beginner Do's": [
            " 'I built a churn model.'  'We found 18% of customers show early churn signs within 30 days.'",
            "Use simple multipliers: '5% retention lift = $75k recovered.'",
            "'Customers behave like subway riders – when one leaves, others follow.'",
            "List 2–3 business actions (e.g., improve onboarding, fix mobile checkout).",
            "Note data gaps or model accuracy limits."
        ],
        "Advanced Do's": [
            "Add context: 'This costs us ~$2.2M annually in lost MRR.'",
            "Build a unit‑economic model; show confidence intervals.",
            "Create a single, board‑ready visual that replaces 10 slides.",
            "Prioritize actions by expected ROI and implementation effort.",
            "Quantify risk (e.g., '10% false positive rate costs $50k'). Show timeline and budget."
        ]
    }
    df_story = pd.DataFrame(storytelling_data)
    st.dataframe(df_story, use_container_width=True)
    
    st.write(
        """
        > Executives remember stories and money, not p‑values or joins.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 8: Core Skills Progression
    # ============================================
    st.header("8. Core Skills Progression: Beginner → Advanced")
    
    skills_data = {
        "Skill Area": ["Storytelling", "Business acumen", "Analytics modeling", "Data engineering basics", "Experimentation", "Tools"],
        "Beginner": [
            "Reports what happened",
            "Knows the KPI definition",
            "Builds a logistic regression",
            "Writes SELECT / JOIN / GROUP BY",
            "Compares two means (A/B test)",
            "SQL, Excel, one of Python/R"
        ],
        "Advanced / Lead": [
            "Predicts what will happen and recommends what to do",
            "Maps KPIs to P&L, cash flow, or strategic initiatives",
            "Designs experiments, causal inference, or production ML",
            "Optimizes queries, understands partitioning and idempotency",
            "Designs stratified or adaptive trials; checks for interference",
            "Python + SQL + orchestration (Airflow/dbt) + BI"
        ]
    }
    df_skills = pd.DataFrame(skills_data)
    st.dataframe(df_skills, use_container_width=True)
    
    st.write(
        """
        **Most important universal skill:**  
        *The ability to ask "So what?" to your own analysis before anyone else does.*
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 9: Best Practices Summary Table
    # ============================================
    st.header("9. Methods at a Glance by Industry")
    
    summary_data = {
        "Industry": ["Healthcare", "Finance/Banking", "Technology/SaaS", "E-Commerce/Retail", "Marketing", "Public Sector"],
        "Primary KPIs": [
            "Mortality rate, readmissions, cost per patient",
            "Default rate, VaR, fraud detection, CLV",
            "MRR, NRR, churn rate, gross margin",
            "AOV, conversion rate, CLV, inventory turnover",
            "ROAS, CAC, retention rate, NPS",
            "Crime reduction, budget accuracy, program adoption"
        ],
        "Key Beginner Technique": [
            "Logistic regression + median imputation",
            "Scorecard + rule-based fraud flags",
            "Cohort analysis + random forest churn",
            "RFM segmentation + moving averages",
            "Last-click attribution + logistic lead scoring",
            "Hotspot mapping + variance reports"
        ],
        "Key Advanced Technique": [
            "Survival models + causal inference",
            "XGBoost fairness + graph fraud networks",
            "Survival analysis + uplift modeling",
            "BG/NBD + hierarchical forecasting",
            "MTA/Shapley + MMM with Bayesian priors",
            "Spatiotemporal forecasting + zero-based budgeting"
        ]
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")
    
    st.write(
        """
        **For beginners:** Start with one industry section above. Replicate the KPIs and project structure with public datasets. Practice the 5-step story on every output.
        
        **For advanced professionals:** Use this guide as a toolkit to reframe your work for C-level audiences. Benchmark your projects against cross-industry patterns. Teach the storytelling framework to junior peers.
        
        > Data analytics is not an IT project. It is a business transformation strategy—and a career accelerator for those who speak both data and decisions.
        
        ---
        
        **Next actions for you:**  
        1. Choose one industry. Write a one-paragraph narrative (Step 1).  
        2. Identify the top 2 KPIs a leader in that industry wakes up worrying about.  
        3. Build a single chart + three bullet recommendations. That's your executive summary.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Tools Mentioned:**
        - [SQL](https://www.w3schools.com/sql/): Data extraction and aggregation
        - [GitHub](https://github.com/): Version control and collaboration
        
        **Further Reading:**
        - [Measure What Matters](https://www.whatmatters.com/) by John Doerr (OKRs and KPIs)
        
        **Public Datasets to Practice:**
        - Healthcare: MIMIC-III, NHANES
        - Finance: LendingClub loan data, FRED economic data
        - SaaS: Kaggle SaaS subscription datasets
        - Retail: UCI Online Retail, Instacart orders
        - Marketing: Google Analytics sample data
        - Public: US Census, Data.gov
        """
    )