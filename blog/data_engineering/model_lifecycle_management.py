import streamlit as st
import pandas as pd

TITLE = "Model Lifecycle Management with Model Registry: From Development to Governance"
CATEGORY = "mlops"
KEYWORDS = [
    "model lifecycle management", "model registry", "MLflow", "model versioning",
    "model lineage", "staging", "production", "archived", "drift detection",
    "model governance", "CI/CD", "MLOps", "model approval workflows", "rollback strategy",
    "feature store integration", "model monitoring", "compliance auditing"
]


def show():
    st.title("Model Lifecycle Management with Model Registry: From Development to Governance")
    st.caption("Category: MLOps | Level: Intermediate → Advanced")
    st.markdown("---")

    # INTRO
    st.write(
        """
        Machine learning has evolved from isolated Jupyter notebooks to production‑critical systems
        powering fraud detection, medical diagnostics, recommendation engines, and autonomous vehicles.

        But with this growth comes a fundamental challenge: **models don't just get built and deployed once**.
        They must be managed continuously throughout their lifecycle to ensure performance, fairness,
        reproducibility, compliance, and business impact.

        This is where **Model Lifecycle Management (MLM)** and **Model Registries** play a strategic,
        non‑negotiable role. Without them, you are not doing MLOps — you are just hoping for the best.
        """
    )

    # ============================================
    # SECTION: What is Model Lifecycle Management?
    # ============================================
    st.header("What is Model Lifecycle Management?")

    st.write(
        """
        Model Lifecycle Management is the **structured, end‑to‑end process** of building, validating,
        registering, deploying, monitoring, governing, and retiring machine learning models across
        different environments (development, staging, production).

        Unlike traditional software artifacts, ML models degrade over time due to data drift,
        concept drift, and changing operational conditions. MLM addresses these unique challenges.
        """
    )

    st.subheader("Why MLM Matters")
    st.write(
        """
        A well‑designed MLM ensures that models are:

        - **Reproducible:** The exact same inputs (data + code + environment) produce the same outputs
        - **Traceable:** Every model version can be linked to its training data, hyperparameters, and engineer
        - **Governed:** Approvals, compliance checks, and audit trails are enforced
        - **Monitored:** Performance, drift, and business KPIs are tracked in real time
        - **Efficiently updated:** Retraining and redeployment happen without manual firefighting
        """
    )

    st.subheader("The Seven Stages of MLM")
    stages_data = {
        "Stage": [
            "1. Experimentation & Training",
            "2. Versioning & Registry",
            "3. Validation / Approval",
            "4. Deployment",
            "5. Serving & Monitoring",
            "6. Retraining & Updating",
            "7. Retirement"
        ],
        "Key Activities": [
            "Data exploration, feature engineering, model selection, track metrics",
            "Store model as immutable artifact with metadata, register with version",
            "Test against holdout data, business rules, fairness checks, approval gates",
            "Push model to serving infrastructure, containerization, API integration",
            "Real‑time inference with telemetry on latency, accuracy, drift alerts",
            "Trigger new training on data drift or schedule, canary rollouts",
            "Deprecate, archive, move to Archived stage, delete from production"
        ]
    }
    df_stages = pd.DataFrame(stages_data)
    st.dataframe(df_stages, use_container_width=True)

    st.info(
        "💡 **Key insight**: Stages are not linear in practice — you may have multiple model versions "
        "in `Staging` or `Production` simultaneously (A/B tests, canaries)."
    )

    st.divider()

    # ============================================
    # SECTION: What is a Model Registry?
    # ============================================
    st.header("What is a Model Registry?")

    st.write(
        """
        A **Model Registry** is a centralized catalog that stores, versions, tracks, and governs
        machine learning models throughout their lifecycle. It acts as the **single source of truth**
        for all production‑ready and candidate models — analogous to artifact repositories
        (Nexus, Artifactory) for software binaries or Git for source code.
        """
    )

    st.subheader("Core Functions of a Model Registry")

    registry_functions = {
        "Function": [
            "Track versions",
            "Store rich metadata",
            "Manage lineage",
            "Validation metrics",
            "Deployment status",
            "Rollback & reproducibility"
        ],
        "What it means in practice": [
            "Every model change gets a unique version (e.g., v1.2.0)",
            "Hyperparameters, feature names, training data hash, framework version",
            "Which data, code, and pipeline produced this model? (DAG)",
            "Accuracy, F1, ROC‑AUC, fairness metrics (demographic parity)",
            "None → Staging → Production → Archived (with timestamps and approvers)",
            "One command to redeploy any archived version"
        ]
    }
    df_functions = pd.DataFrame(registry_functions)
    st.dataframe(df_functions, use_container_width=True)

    st.subheader("Example: MLflow Model Registry Entry")
    st.code(
        """
{
  "model_name": "water_potability_xgboost",
  "version": "3.2.1",
  "stage": "Production",
  "run_id": "abc123",
  "training_data_uri": "s3://bucket/water_samples_2026-03-01.parquet",
  "hyperparameters": {"max_depth": 7, "eta": 0.1},
  "metrics": {"accuracy": 0.94, "f1": 0.92},
  "registered_by": "ml_team@example.com",
  "approval_timestamp": "2026-04-01T10:00:00Z"
}
        """,
        language="json"
    )

    st.divider()

    # ============================================
    # SECTION: Industry Standards & Best Practices
    # ============================================
    st.header("Industry Standards and Best Practices")

    st.subheader("1. Versioning Beyond Code — The Five Dimensions")
    st.write(
        """
        Traditional software versioning (Git commits) is insufficient for ML. You must version:

        - **Model code** (training script, inference wrapper)
        - **Training data** (exact snapshot or hash)
        - **Feature transformations** (scalers, encoders, feature engineering logic)
        - **Hyperparameters** (including random seeds)
        - **Environment** (library versions, CUDA, OS)
        """
    )

    st.subheader("2. Metadata and Lineage Tracking — The Audit Trail")
    st.write(
        """
        Industry leaders (Google Vertex, AWS SageMaker, Microsoft Azure ML) emphasize **full lineage capture**
        to satisfy both internal debugging and external audits (GDPR, SOX, HIPAA).

        **Critical metadata to capture**:
        - Training dataset version or snapshot URI
        - Feature set definition (including derived features)
        - Hyperparameter search space
        - Hardware resources (GPU type, RAM)
        - Validation results per data slice
        - Responsible engineer(s) and review sign‑offs
        """
    )

    st.subheader("3. Deployment and Approval Workflows — The Governance Gates")
    st.write("Models should not move to production without controlled gates:")

    gates_data = {
        "Stage": ["Staging", "Canary", "Shadow", "Production", "Deprecated"],
        "Description": [
            "Test on mirror of production data (historical)",
            "Small % of live traffic (e.g., 5%)",
            "Run in parallel with production model, no user impact",
            "Full rollout to 100% traffic",
            "Model no longer serving but archived"
        ],
        "Typical Validation": [
            "Accuracy ≥ baseline, no fairness violations",
            "Monitor for 24h, error rate < threshold",
            "Compare predictions, detect divergence",
            "Business KPIs monitored",
            "Retention policy applied (e.g., 1 year)"
        ]
    }
    df_gates = pd.DataFrame(gates_data)
    st.dataframe(df_gates, use_container_width=True)

    st.divider()

    # ============================================
    # SECTION: Real-World Applications
    # ============================================
    st.header("Real-World Applications")

    # Finance
    st.subheader("Finance — Fraud Detection")
    st.write(
        """
        **Context:** Fraud patterns evolve rapidly (new payment methods, seasonal spikes). Models may degrade within weeks.

        **Challenges:**
        - Frequent retraining (daily or weekly)
        - Regulatory audits requiring full model history
        - Multiple model variants in production (by region or card type)

        **Registry Solution:**
        - Maintain 10+ candidate models alongside production champion
        - Track data drift metrics (PSI, KS statistic) automatically
        - Trigger rollback if production AUC drops below 0.85 within 2 hours
        - Store immutable audit trails (who approved which model, when, with what validation)

        **Outcome:** A large European bank reduced fraud losses by 18% and passed an audit with zero findings.
        """
    )

    # Healthcare
    st.subheader("Healthcare — Diagnostic Models")
    st.write(
        """
        **Context:** Model decisions impact patient outcomes. Explainability and compliance are paramount.

        **Challenges:**
        - HIPAA and GDPR require data lineage (which patients' data trained the model?)
        - Black‑box models may be rejected; SHAP/LIME explanations must be stored
        - Model updates need clinical review

        **Registry Benefits:**
        - Each model version tied to a dataset snapshot (de‑identified patient cohort)
        - Approval workflows require sign‑off from clinical lead and data privacy officer
        - Registry logs every prediction request (if permitted) for retrospective analysis

        **Example:** A radiology AI for pneumonia detection linked each model version to the exact set of chest X‑rays.
        When a new model improved sensitivity by 5%, the registry automatically generated a compliance report for the FDA.
        """
    )

    # E-commerce
    st.subheader("E‑commerce — Recommendation Engines")
    st.write(
        """
        **Context:** User behavior shifts with seasons, promotions, and trends. A/B testing is continuous.

        **Registry Benefits:**
        - Compare candidate models using business KPIs: conversion rate, average order value, click‑through rate
        - Manage dozens of A/B test variants simultaneously
        - Rapid rollback (within minutes) if customer engagement drops

        **Real metric:** A large online retailer detected a 3% drop in add‑to‑cart rate within 15 minutes and automatically
        reverted to the previous champion, saving an estimated $2.5M in lost sales.
        """
    )

    st.divider()

    # ============================================
    # SECTION: Deep Technical Insights
    # ============================================
    st.header("Deep Technical Insights")

    st.subheader("Model Artifact and Metadata Storage — Architecture Choices")
    storage_data = {
        "Component": ["Model binary", "Metadata (structured)", "Metrics (time‑series)", "Lineage graph"],
        "Storage Technology": [
            "Object storage (S3, GCS, Azure Blob) + path in registry",
            "Relational DB (PostgreSQL) or key‑value store",
            "Prometheus, InfluxDB, or registry‑cached",
            "Graph DB (Neo4j) or metadata store with DAG support"
        ],
        "Why": [
            "Large files, versioned, immutable",
            "Fast queries by version, stage, metric",
            "Trend analysis, alerting",
            "Complex lineage queries"
        ]
    }
    df_storage = pd.DataFrame(storage_data)
    st.dataframe(df_storage, use_container_width=True)

    st.subheader("Linking Features and Training Data — The Missing Link")
    st.write(
        """
        One of the most overlooked areas: **reproducing the exact feature vectors** used at training time.

        **Solution:** Use a feature store (Feast, Tecton) that versions feature definitions and data snapshots.
        The model registry stores a **feature set version** or **data hash**.

        **Example registry entry with feature linkage:**
        """
    )
    st.code(
        """
model_version: "fraud_detection_v2.1"
feature_service: "user_transaction_features@v2026-03-15"
training_data_snapshot: "lakefs://fraud/train@2026-03-01"
feature_hash: "md5:8a3f2b..."
        """,
        language="yaml"
    )

    st.subheader("Automation and CI/CD Integration — The Pipeline")
    st.write(
        """
        **Example CI/CD workflow with Model Registry:**

        1. **Code change** → Git push triggers CI
        2. **Test** → Unit tests for data validation, schema checks
        3. **Train** → Run training pipeline on fresh data
        4. **Evaluate** → Compare metrics against current `Production` model
        5. **Register** → If metrics improve, register as `Staging` in registry
        6. **Approval** → Manual or automated (if improvement > threshold)
        7. **Deploy** → GitOps (ArgoCD) pulls the `Staging` model and deploys to canary
        8. **Monitor** → 1 hour canary with drift detection; auto‑promote or rollback

        **Tools:** GitHub Actions + MLflow + ArgoCD + Prometheus
        """
    )

    st.subheader("Monitoring and Feedback Loops — Closing the Loop")
    monitoring_data = {
        "Layer": ["Model performance", "Data drift", "Business KPIs", "Operational"],
        "Metrics": [
            "Accuracy, AUC, F1, precision/recall",
            "Population Stability Index (PSI), KL divergence, feature distributions",
            "Revenue, conversion, latency, error rate",
            "Inference time, throughput, memory"
        ],
        "Action on threshold breach": [
            "Retrain or rollback",
            "Alert data engineering, retrain",
            "Page ops team, rollback",
            "Auto‑scale or model optimization"
        ]
    }
    df_monitoring = pd.DataFrame(monitoring_data)
    st.dataframe(df_monitoring, use_container_width=True)

    st.write(
        "**Feedback loop:** When drift exceeds 20% over 7 days, the Model Registry can trigger an automated "
        "retraining pipeline using the latest data, register the new candidate, and start a canary deployment."
    )

    st.divider()

    # ============================================
    # SECTION: Tools and Ecosystem
    # ============================================
    st.header("Tools and Ecosystem")

    tools_data = {
        "Category": ["Model Registry", "Feature Store", "Workflow Orchestration", "Data Versioning", "Monitoring", "Governance"],
        "Tools": [
            "MLflow, Kubeflow Model Registry, SageMaker, Vertex AI",
            "Feast, Tecton, Databricks Feature Store",
            "Airflow, Prefect, Argo, Kubeflow Pipelines",
            "DVC, LakeFS, Delta Lake",
            "Prometheus + Grafana, Evidently, WhyLogs",
            "Open Policy Agent (OPA), custom approval UIs"
        ],
        "When to choose": [
            "MLflow for open‑source flexibility; cloud‑native for tight integration",
            "Feast for open source; Tecton for enterprise",
            "Airflow for batch; Argo for Kubernetes",
            "DVC for Git‑like; LakeFS for S3 versioning",
            "Evidently for drift; Prometheus for ops",
            "OPA for policy‑as‑code"
        ]
    }
    df_tools = pd.DataFrame(tools_data)
    st.dataframe(df_tools, use_container_width=True)

    st.info(
        "📌 **Selection guideline:** Start with MLflow + DVC + Airflow. "
        "As scale grows, add Feast and Kubeflow."
    )

    st.divider()

    # ============================================
    # SECTION: Case Example — MLflow
    # ============================================
    st.header("Case Example: MLflow Model Registry in Action")

    st.write(
        """
        **Scenario:** A team builds a water potability classifier.

        **Step‑by‑step with MLflow:**
        """
    )
    st.code(
        """
import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

# 1. Train and log
with mlflow.start_run():
    mlflow.log_param("model_type", "XGBoost")
    mlflow.log_metric("accuracy", 0.92)
    mlflow.sklearn.log_model(model, "model")

# 2. Register
result = mlflow.register_model("runs:/<run_id>/model", "WaterPotabilityModel")
version = result.version

# 3. Transition to Staging
client.transition_model_version_stage(
    name="WaterPotabilityModel",
    version=version,
    stage="Staging"
)

# 4. After validation → Production
client.transition_model_version_stage(
    name="WaterPotabilityModel",
    version=version,
    stage="Production"
)

# 5. Archive old version
client.transition_model_version_stage(
    name="WaterPotabilityModel",
    version=1,
    stage="Archived"
)
        """,
        language="python"
    )

    st.write(
        """
        **Benefits realized:**
        - Central catalog of all models (no more "final_final_v3.pkl")
        - Approval governance: only senior engineers can move to `Production`
        - Version history with metrics to compare performance across releases
        """
    )

    st.divider()

    # ============================================
    # SECTION: Industry Standards & Frameworks
    # ============================================
    st.header("Industry Standards and Frameworks")

    standards_data = {
        "Standard / Framework": [
            "ISO/IEC 38507",
            "NIST AI Risk Management Framework",
            "FAIR Principles",
            "IEEE 7000 series",
            "MLflow Model Registry spec"
        ],
        "Scope": [
            "Governance of AI systems",
            "Identify, measure, manage AI risks",
            "Data and model traceability",
            "Ethical AI, transparency",
            "De facto open standard for model metadata"
        ],
        "Relevance to Model Registry": [
            "Registry provides audit trail and role‑based access",
            "Registry tracks risk assessments per model version",
            "Registry makes models FAIR by design",
            "Store fairness metrics and explanations in registry",
            "Used by thousands of organizations"
        ]
    }
    df_standards = pd.DataFrame(standards_data)
    st.dataframe(df_standards, use_container_width=True)

    st.warning(
        "⚠️ **Compliance tip:** Many regulated industries require that every production model has a "
        "corresponding registry entry with approval signature and validation report. Without a registry, "
        "passing audits is nearly impossible."
    )

    st.divider()

    # ============================================
    # SECTION: Summary Comparison
    # ============================================
    st.header("Summary: MLM Impact Across Roles")

    summary_data = {
        "Role": ["Data Scientist", "ML Engineer", "ML Ops Engineer", "Compliance Officer"],
        "Primary Focus": [
            "Model development, experimentation, feature engineering",
            "Deployment, scalability, inference optimization",
            "CI/CD pipelines, monitoring, infrastructure",
            "Audit trails, approvals, regulatory compliance"
        ],
        "Model Registry Provides": [
            "Experiment reproducibility, version comparison, staging validation",
            "Artifact storage, rollback capability, deployment targets",
            "Stage transitions, automated triggers, drift alerts",
            "Immutable history, approval workflows, model lineage"
        ],
        "Risk Without Registry": [
            "Lost experiments, unreproducible results",
            "Manual artifact handling, deployment errors",
            "No automated rollback, undetected drift",
            "Failed audits, compliance violations"
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
        Model Lifecycle Management and Model Registries are not "nice‑to‑have" tools — they are
        **essential pillars of mature MLOps**. They transform machine learning from a collection
        of ad‑hoc experiments into a governed, scalable, and trustworthy engineering discipline.

        A model registry is to ML what Git is to code — the foundation of collaboration, trust, and history.

        By combining proper tooling, thoughtful workflows, and observability, enterprises can move
        from fragile, one‑off models to **robust, governed ML systems** that deliver sustained business value.
        """
    )

    st.divider()

    # ============================================
    # BEST PRACTICES
    # ============================================
    st.header("Best Practices for Model Lifecycle Management")

    st.markdown(
        """
        **1. Start Small, but Start Now**
        - Even a simple registry (MLflow with shared S3 bucket) brings immediate reproducibility benefits
        - Don't wait for perfect infrastructure — begin with versioning and staging

        **2. Automate Approvals and Transitions**
        - Manual stage changes lead to errors and delays
        - Use CI/CD pipelines to enforce validation gates

        **3. Link Models to Data Versions**
        - Without data lineage, reproducibility is a myth
        - Use data versioning tools (DVC, LakeFS) and store hashes in the registry

        **4. Monitor After Deployment**
        - A model in production without monitoring is like a car without a dashboard
        - Track drift, performance, and business KPIs continuously

        **5. Plan for Retirement**
        - Archived models should be kept for compliance but excluded from active inference
        - Define retention policies (e.g., 1 year for financial models)

        **6. Establish Approval Workflows**
        - Require sign‑offs for Staging → Production transitions
        - Maintain audit logs of who approved what and when
        """
    )

    st.success(
        "✅ **Next steps:** Evaluate your current model management maturity. "
        "If you cannot answer 'Which data produced this model?' or 'Who approved it for production?' "
        "within 30 seconds, you need a Model Registry today."
    )

    st.divider()
    st.caption("📖 Article: Model Lifecycle Management with Model Registry | Category: MLOps | Level: Intermediate → Advanced")