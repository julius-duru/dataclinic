import streamlit as st
import pandas as pd

TITLE = "Data Governance for Data Scientists: Risks, Remedies & MLOps"
CATEGORY = "mlops_data_governance"
KEYWORDS = [
    "data governance", "MLOps", "GDPR", "data privacy", "data lineage",
    "data quality", "bias mitigation", "compliance", "data versioning",
    "DVC", "data contracts", "consent management", "right to be forgotten"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Beginner → Intermediate (MLOps focus)")
    st.markdown("---")

    # INTRO – conversational tone
    st.write(
        """
        **Data governance** is a critical aspect of data science and MLOps. Data scientist or ML engineer need to understand it.  
        It is strongly tied to terms like *GDPR*, *data lineage*, or *compliance*. They are standards that keep your models reliable and keep an organisation compliant with regulations surrounding data usage.

        **In this guide you will learn:**  
        - What data governance *actually* means for your daily ML work  
        - Real risks you face when you skip it (with real‑world fine examples)  
        - Simple, practical remedies you can apply today  
        - Dependencies (people, tools, processes) you need to make it stick  
        - Key regulations in plain English – no law degree required  
        - A beginner’s checklist for every end‑to‑end MLOps project

        > Think of governance as the **rule book and referee** for your data – it answers: Where did this come from? Can I use it? Who changed it? What if a user asks to be forgotten?
        """
    )
    st.markdown("---")

    # 1. RISKS – table format for clarity
    st.header("What happens when you ignore data governance?")
    st.write(
        """
        These risks include payment of fines, loss of reputation, loss of business or even legal consequences. Other attendant technical risks include:
        """
    )
    risks_df = pd.DataFrame({
        "Risk": [
            "Poor data quality",
            "Data leakage (future info)",
            "Bias & unfairness",
            "Privacy violations",
            "No lineage / audit trail",
            "Compliance breach"
        ],
        "Real‑world impact": [
            "Model trains on duplicates / stale data → fails in production",
            "Model looks amazing in tests, then bombs because it used tomorrow’s data",
            "Loan approval model discriminates; you end up in headlines",
            "Model memorises and outputs someone’s address → GDPR fine up to €20M or 4% global revenue",
            "Regulator asks 'what data trained that model?' – you have no answer",
            "You ignored a 'right to be forgotten' request – illegal under GDPR"
        ]
    })
    st.dataframe(risks_df, use_container_width=True)
    st.markdown("---")

    # 2. REMEDIES – practical steps with code snippets
    st.header("Remedies: what you can do, step by step")
    st.write(
        """
        To remain compliant, you don’t need a huge team. Have a dedicated team that is intensional with documentations, and integrate these into your MLOps pipeline.
        """
    )

    with st.expander("1. Data catalog + lineage tracking", expanded=False):
        st.write(
            """
            **What**: Record for each dataset: source, owner, update frequency, quality score, consent flags.  
            **Tool examples**: Amundsen, DataHub, or even a simple spreadsheet.  
            **Why**: When someone asks “where did this come from?” you have an answer.
            """
        )
        st.code(
            "# Minimal lineage example (pseudocode)\n"
            "dataset_metadata = {\n"
            "    'name': 'customer_events',\n"
            "    'source': 'kafka_topic_cdc',\n"
            "    'owner': 'data_team@example.com',\n"
            "    'pii_columns': ['email', 'phone'],\n"
            "    'consent_given': True,\n"
            "    'last_updated': '2026-04-01'\n"
            "}",
            language="python"
        )

    with st.expander("2. Version your data like code", expanded=False):
        st.write(
            """
            **What**: Use tools like DVC or Delta Lake. Every change to a dataset gets a hash.  
            **Why**: Reproduce any model from any point in time. No more “it worked last week, I swear”.
            """
        )
        st.code(
            "# Using DVC\n"
            "dvc add data/customer_churn.csv\n"
            "git add data/customer_churn.csv.dvc .gitignore\n"
            "git commit -m 'Add dataset version 1.0'",
            language="bash"
        )

    with st.expander("3. Automate data quality tests", expanded=False):
        st.write(
            """
            **What**: Write simple expectations (no nulls in ID, revenue > 0, date monotonic).  
            **Tools**: Great Expectations, Soda, or custom pytest checks.  
            **Why**: Your pipeline fails early, not after three days of training.
            """
        )
        st.code(
            "# Great Expectations example\n"
            "expect_column_values_to_not_be_null('customer_id')\n"
            "expect_column_values_to_be_between('age', 0, 120)\n"
            "expect_column_pair_values_A_to_be_greater_than_B('end_date', 'start_date')",
            language="python"
        )

    with st.expander("4. Privacy by design", expanded=False):
        st.write(
            """
            - **Data minimisation**: only collect what you really need.  
            - **Anonymisation / pseudonymisation** before training.  
            - For sensitive projects: **differential privacy** or **synthetic data**.
            """
        )
        st.code(
            "# Pseudonymisation example (hash email)\n"
            "import hashlib\n"
            "df['email_hash'] = df['email'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())\n"
            "df.drop('email', axis=1, inplace=True)",
            language="python"
        )

    with st.expander("5. Deletion mechanism (right to be forgotten)", expanded=False):
        st.write(
            """
            **What**: In your pipeline, when a user requests deletion, flag that record. Decide if you need to retrain the model (often yes for small datasets – document your decision).  
            **Why**: You can legally say “that person’s data is gone from our active systems”.
            """
        )
        st.code(
            "# Pseudo logic for deletion\n"
            "deleted_users = load_deletion_list()\n"
            "df = df[~df['user_id'].isin(deleted_users)]\n"
            "# If model retraining needed:\n"
            "retrain_model(df)",
            language="python"
        )

    with st.expander("6. Audit log for high‑risk predictions", expanded=False):
        st.write(
            """
            **What**: For decisions like loans, hiring, medical triage – log input features, model version, output. Store immutably.  
            **Why**: You can later explain or contest a decision (legally required in some cases, e.g. GDPR Article 22).
            """
        )
        st.code(
            "# Simple logging to a database or cloud storage\n"
            "prediction_log = {\n"
            "    'timestamp': '2026-04-10T12:00:00Z',\n"
            "    'model_version': 'churn_v2.joblib',\n"
            "    'input_features': X_test.iloc[0].to_dict(),\n"
            "    'prediction': 1,\n"
            "    'confidence': 0.87\n"
            "}\n"
            "# store in secure, immutable store",
            language="python"
        )

    st.markdown("---")

    # 3. DEPENDENCIES
    st.header("Dependencies – what else needs to be in place")
    st.write(
        """
        Governance doesn’t live in a vacuum. It needs:
        - **Organisational buy‑in** – manager & legal agree on retention policies, risk thresholds.
        - **MLOps infrastructure** – pipelines that can version data, run quality checks, log lineage.
        - **Data engineering support** – someone to help set up catalog or quality tests (or learn it yourself).
        - **Clear roles** – Who owns quality of the `customer_events` table? Who approves new data sources?
        - **Training** – A single 1‑hour workshop for your team can prevent months of pain.
        """
    )
    st.info("Without these dependencies, governance becomes “one person’s hobby” and breaks when you’re on vacation.")
    st.markdown("---")

    # 4. REGULATIONS – plain English
    st.header("Regulations you should know (no law degree required)")
    reg_df = pd.DataFrame({
        "Regulation": ["GDPR", "CCPA / CPRA", "HIPAA", "PIPL", "EU AI Act"],
        "Region": ["EU", "California, USA", "USA (healthcare)", "China", "EU"],
        "What it means for you (plain English)": [
            "Need a legal reason to process personal data. Users can ask to see, correct, or delete their data. Automated decisions must be explainable.",
            "Similar to GDPR, with extra focus on opt‑out from data 'selling'. Right to delete and know what data you hold.",
            "If you touch protected health information (PHI), you need strict security, access logs, and business associate agreements. Fines per record add up fast.",
            "Separate consent for different purposes. Cross‑border data transfers heavily restricted.",
            "Categorises AI by risk. High‑risk systems (employment, credit, law enforcement) require risk management, data governance, and human oversight."
        ]
    })
    st.dataframe(reg_df, use_container_width=True)
    st.caption("For beginners: assume GDPR applies to any data that could identify a person. When in doubt, anonymise aggressively.")
    st.markdown("---")

    # 5. BEGINNER'S CHECKLIST
    st.header("Your end‑to‑end checklist for every MLOps project")
    st.write(
        """
        Copy this into your project wiki or notebook. Answer each question honestly.
        """
    )
    checklist = """
    **Before you write a single line of code:**  
    - [ ] Do I have permission to use this data for this purpose?  
    - [ ] Have I documented where the data came from?  
    - [ ] Is there any PII? If yes, can I anonymise it?  

    **During data prep:**  
    - [ ] Are my data quality checks passing? (nulls, duplicates, ranges)  
    - [ ] Did I accidentally create data leakage? (e.g., using future info)  
    - [ ] Is the train/val/test split truly i.i.d.?  

    **During training & versioning:**  
    - [ ] Did I version both the data AND the code?  
    - [ ] Can I reproduce this model six months from now?  

    **Before deployment:**  
    - [ ] Does this model make high‑risk decisions? If yes, have I logged an explanation method?  
    - [ ] Do I have a way to honour deletion requests?  
    - [ ] Have I documented any known biases or limitations?  

    **In production:**  
    - [ ] Am I monitoring for data drift and concept drift?  
    - [ ] If the model output changes, can I trace it back to a specific data change?  
    """
    st.markdown(checklist)
    st.success("If you can answer “yes” or “we have a plan” to these, you’re already ahead of most teams.")
    st.markdown("---")

    # 6. CONCLUSION & NEXT STEPS
    st.header("Approach to governance: start small, iterate, and ask for help")
    st.write(
        """
        Don’t try to boil the ocean. Pick **one** governance practice for your next project – maybe data versioning, or a single data quality test. Then add another. Over time, these habits become second nature.

        Regulators don’t fine you for trying your best. They fine you for wilful neglect. So just start. Document what you do. And when you’re unsure, ask your legal or compliance team – they’d much rather answer a question early than clean up a mess later.

        **Next actions for you:**  
        1. Take one of your existing notebooks and add a data quality test using Great Expectations or a simple `assert`.  
        2. Install DVC and version your dataset – run `dvc add` and commit the metadata.  
        3. Write a one‑page “data governance light” doc for your team: who owns which datasets, what’s our deletion process, and which columns contain PII.

        You’ve got this. Now go build something awesome – and responsible. 
        """
    )
    st.markdown("---")

    # 7. EXTERNAL RESOURCES
    st.header("External resources to go deeper")
    st.markdown(
        """
        **Data governance frameworks & standards**  
        - [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)  
        
        **Tools for governance in MLOps**  
        - [DVC (Data Version Control)](https://dvc.org)  
        - [Great Expectations (data quality)](https://greatexpectations.io)  
        - [OpenLineage (cross‑platform lineage)](https://openlineage.io)  
        - [MLflow (experiment tracking + model registry)](https://mlflow.org)  

        **Privacy‑preserving techniques**  
        - [Google’s Differential Privacy library](https://github.com/google/differential-privacy)  
        - [Synthetic Data Vault (SDV)](https://sdv.dev)  

        **Regulations (plain‑language summaries)**  
        - [GDPR in 20 minutes (CNIL video)](https://www.cnil.fr/en/gdpr-20-minutes)  
        - [EU AI Act explained (European Parliament)](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)  
        
        **Books**  
        - “Fundamentals of Data Engineering” by Joe Reis & Matt Housley (chapters on governance)  
        - “Designing Data‑Intensive Applications” by Martin Kleppmann (consistency, lineage, audits)
        """
    )
    st.markdown("---")
    st.caption("© 2026 | Data Governance for Data Scientists | Build responsible MLOps from day one.")
