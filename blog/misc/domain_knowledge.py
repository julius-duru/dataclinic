import streamlit as st
import pandas as pd

TITLE = "Why Domain Knowledge is the Real Driver of Success in AI / Data Science"
CATEGORY = "misc"
KEYWORDS = ["domain knowledge", "data science", "machine learning", "artificial intelligence", "feature engineering", "model interpretability", "data analytics", "AI strategy"]


def show():

    st.title("Why Domain Knowledge is the Real Driver of AI and Data Science Success")
    st.caption("Category: Misc | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        In data science, machine learning (ML), and artificial intelligence (AI), it is easy to get lost trying to keep up with lots 
        of details including choice of algorithms, model selection, data preprocessing and other aspects.  
        We often obsess over model accuracy, hyperparameter tuning, and the latest neural network architectures. 
        
        But ask any seasoned data scientist, and they will tell you: the difference between a model that looks good on paper and one that 
        delivers real business value often comes down to one critical factor—**domain knowledge**.
        
        Domain knowledge is the deep understanding of the context, industry, or problem space where your data lives. 
        While algorithms provide the engine, domain expertise provides the steering wheel. Without it, you might be just **a highly skilled 
        technician driving in the dark**.
        
        Let's explore how this specialized knowledge shapes and elevates the three pillars of the analytics world: 
        Data Science, Data Analytics, and Machine Learning/AI.
        """
    )

    # ============================================
    # SECTION: Why Domain Knowledge Matters
    # ============================================
    st.header("Why Domain Knowledge Matters")
    
    st.write(
        """
        Raw data is inherently meaningless. It is just a collection of bytes, numbers, and text until we apply context.
        
        - **Context is King:** A spike in transaction volume could indicate fraud in a bank, a flash sale in e-commerce, 
          or a sensor malfunction in a factory. Without understanding *where* the data comes from, you cannot interpret *what* it means.
        
        - **Relevance over Volume:** Domain experts help distinguish signal from noise. They know which data points are relevant 
          and which are just "interesting but useless" artifacts.
        """
    )
    
    st.divider()

    # ============================================
    # SECTION 1: IMPACT IN DATA SCIENCE
    # ============================================
    st.header("Impact in Data Science")
    
    st.write(
        """
        Data Science sits at the intersection of computer science, statistics, and business strategy. 
        Domain knowledge acts as the bridge between raw code and actionable insights.
        """
    )
    
    st.subheader("1. Problem Framing")
    st.write(
        """
        The most difficult part of a data scientist's job isn't building the model; it is mainly defining the problem and deriving 
        the right analytical approach and getting insights. 
        
        Domain experts translate vague business challenges (e.g., "we need to retain customers") into precise analytical targets 
        (e.g., "predict the probability of churn within 30 days based on support ticket sentiment").
        """
    )
    
    st.subheader("2. Feature Engineering")
    st.write(
        """
        Algorithms are hungry for data, but domain knowledge tells you what to feed them. 
        The most predictive features often are not the raw columns in a database, but the derived metrics born from industry insight.
        
        | Industry | Domain-Driven Feature |
        |----------|----------------------|
        | Finance | Debt-to-income ratio |
        | Manufacturing | Mean time between failures (MTBF) |
        | Telecom | Tenure-to-usage ratio |
        | Healthcare | Patient risk scores based on comorbidity |
        """
    )
    
    st.subheader("3. Intelligent Data Cleaning")
    st.write(
        """
        Good domain knowledge prevents you from throwing out the "golden nuggets" hidden in dirty data.
        A temperature reading of 150°C is an error in a weather dataset, but it is a critical signal in an industrial furnace sensor dataset. 
        Domain expertise helps you distinguish between noise that needs filtering and rare events that need flagging.
        """
    )
    
    st.subheader("4. Choosing Appropriate Models")
    st.write(
        """
        Domain constraints shape model decisions:
        - **Time-series forecasting** for energy demand
        - **Probabilistic models** for risk assessment
        - **Clustering** for customer segmentation
        - **Explainable models (e.g., Logistic Regression, XGBoost)** for regulated industries like finance and healthcare
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 2: IMPACT IN DATA ANALYTICS
    # ============================================
    st.header("Impact in Data Analytics")
    
    st.write(
        """
        While Data Science focuses on prediction, Data Analytics focuses on interpretation. 
        Domain knowledge ensures that historical data actually drives better decisions.
        """
    )
    
    st.subheader("1. Asking the Right Questions")
    st.write(
        """
        Without domain expertise, analysts often fall into the trap of "vanity metrics"—numbers that look good but do not support good decision-making. 
        A marketing analyst with domain knowledge knows to prioritize **Customer Lifetime Value (CLV)** over simply counting clicks or impressions.
        """
    )
    
    st.subheader("2. Insight Generation")
    st.write(
        """
        Patterns don't exist in a vacuum. If sales drop on a Tuesday, a junior analyst might just report the drop. 
        A domain-savvy analyst investigates whether it correlates with a competitor's product launch, a recent software update, 
        or a seasonal holiday.
        """
    )
    
    st.subheader("3. Effective Communication")
    st.write(
        """
        The best insights are worthless if they cannot be interpreted and actioned. Analysts with industry knowledge speak the language 
        of the stakeholders — be it clinicians, logistics managers, or CFOs. It allows them to translate complex findings on data
        into actionable business recommendations.
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 3: IMPACT IN MACHINE LEARNING & AI
    # ============================================
    st.header("Impact in Machine Learning & AI")
    
    st.write(
        """
        In ML and AI, domain knowledge is what separates a "toy model" from a production-ready, trustworthy system.
        """
    )
    
    st.subheader("1. Model Design and Selection")
    st.write(
        """
        Domain dynamics dictate algorithm choice. You wouldn't use a linear regression to forecast chaotic energy grid loads, 
        nor would you use a black-box neural network for a credit risk model where regulatory explainability is required.
        """
    )
    
    st.subheader("2. Avoiding Misinterpretation")
    st.write(
        """
        A model can be mathematically accurate but contextually wrong. Domain knowledge helps prevent these pitfalls:
        
        - **Healthcare:** Recognizing that correlation (e.g., shoe size vs. reading ability) does not contribute to health outcomes.
        - **Cybersecurity:** Understanding that a spike in login attempts is normal during a marketing campaign but malicious during off-hours.
        """
    )
    
    st.subheader("3. AI Explainability and Ethics")
    st.write(
        """
        Domain experts are the "human-in-the-loop" who validate that a model makes logical sense. They ensure the model is not relying 
        on spurious correlations and that it adheres to fairness and compliance standards.
        """
    )
    
    st.subheader("4. Operationalizing ML Systems")
    st.write(
        """
        When ML models get into production, domain knowledge defines the boundaries of success. It helps engineers:
        - Set acceptable error thresholds
        - Define risk scores
        - Detect **concept drift**—when the real-world environment changes and model performance degrades
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 4: CRITICAL INDUSTRIES
    # ============================================
    st.header("When Domain Knowledge Becomes Critical")
    
    st.write(
        """
        Domain knowledge is always valuable, it is absolutely non-negotiable in specific industries where mistakes have high stakes:
                
        - Healthcare : Misclassification can affect patient lives, hence models must align with clinical workflows
        - Finance and Banking : Strict regulatory constraints require models to be explainable and fair
        - Manufacturing : Understanding physical processes and sensor mechanics is required to predict equipment failure accurately
        - Aviation and Logistics : Safety-critical systems rely on domain logic to prevent catastrophic failures
        - Cybersecurity : Attackers are adaptive; understanding attacker behavior is necessary to distinguish threats from false positives
        - Energy : Physical constraints (grid capacity, weather patterns) affect modeling accuracy 
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 5: KEY AREAS OF INFLUENCE
    # ============================================
    st.header("Key Areas Where Domain Knowledge Supports the Workflow")
    
    st.write(
        """
        If you are building or deploying a data science application, domain knowledge influences the entire lifecycle:
        
        - **Problem Framing:** Identifying the right KPIs and business objectives
        - **Data Behavior:** Understanding industry-specific trends and seasonality
        - **Feature Engineering:** Crafting meaningful predictors from raw data
        - **Validation:** Testing model assumptions against real-world logic
        - **Interpretation:** Distinguishing between actionable anomalies and statistical noise
        - **Safety & Compliance:** Ensuring models meet regulatory and ethical standards
        - **Deployment:** Defining realistic evaluation metrics and monitoring for drift
        - **Risk Management:** Assessing the downstream impact of model errors
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 6: SUMMARY COMPARISON
    # ============================================
    st.header("Summary: Domain Knowledge Impact Across Disciplines")
    
    summary_data = {
        "Discipline": ["Data Science", "Data Analytics", "Machine Learning & AI"],
        "Primary Focus": [
            "Prediction, modeling, feature engineering",
            "Interpretation, reporting, decision support",
            "Automation, scalability, real-time intelligence"
        ],
        "Domain Knowledge Provides": [
            "Problem framing, feature ideas, model selection, cleaning logic",
            "Relevant KPIs, contextual insights, stakeholder communication",
            "Model constraints, explainability, operational guardrails, drift detection"
        ],
        "Risk Without Domain Knowledge": [
            "Models optimized for wrong metrics, poor feature selection",
            "Vanity metrics, misinterpreted patterns, irrelevant recommendations",
            "Black-box failures, regulatory violations, unsafe deployments"
        ]
    }
    
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")
    
    st.write(
        """
        As the fields of data science and AI continue to evolve, the hard truth remains: 
        **algorithms are a commodity, but domain knowledge is a competitive advantage.**
        
        A data scientist with domain expertise is worth ten data scientists without it. 
        They do not just find patterns; they find the *right* patterns. 
        They do not just build models; they build solutions that fit seamlessly into the real world.
        
        So, whether you are an aspiring data scientist or a business leader investing in AI, 
        remember to prioritize context alongside computation. Because in the end, the goal is not just to predict the future—
        it's to understand it well enough to shape it.
        """
    )
    
    st.divider()
    
    # ============================================
    # BEST PRACTICES
    # ============================================
    st.header(" Best Practices for Leveraging Domain Knowledge")
    
    st.markdown(
        """
        **1. Collaborate Early and Often**
        - Involve domain experts during problem definition, not just at the end for validation
        - Schedule regular syncs between data teams and business stakeholders
        
        **2. Build Cross-Functional Teams**
        - Combine data scientists, ML engineers, and domain specialists
        - Encourage knowledge sharing sessions where domain experts explain industry nuances
        
        **3. Document Domain Assumptions**
        - Record why certain features were created
        - Document business rules and constraints embedded in the model
        - Maintain a knowledge base of domain-specific edge cases
        
        **4. Invest in Domain Training**
        - Data scientists should spend time shadowing domain experts
        - Encourage reading industry reports, attending domain conferences, and understanding regulatory landscapes
        
        **5. Validate with Real-World Feedback**
        - Use A/B testing to confirm model impact in production
        - Establish feedback loops with end-users who understand the domain context
        """
    )