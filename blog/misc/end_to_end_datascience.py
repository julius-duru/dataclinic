import streamlit as st


TITLE = "Designing an Intelligent System End-to-End"
CATEGORY = "misc"
KEYWORDS = ["mlops", "machine learning", "data engineering", "ai systems", "deployment"]


def show():

    st.title("🧠 Procedure for Designing an Intelligent System")

    st.caption("Category: Misc | Level: Advanced")

    st.markdown("---")

    st.write(
        """
        **Designing an intelligent system** is not merely about building a model; 
        it is a **complex, multidisciplinary engineering process**.

        It requires balancing the following critical factors:
        - Business objectives  
        - Data constraints  
        - Technical architecture  
        - Ethical considerations  

        This lifecycle is structured into **nine phases**, forming a continuous 
        loop of improvement and optimization.
        """
    )

    # -----------------------------
    # PHASE 1
    # -----------------------------
    st.header("📌 Phase 1: Problem Definition & Scoping")

    st.write(
        """
        This is the most critical phase. A poorly defined problem leads to failure 
        regardless of technical excellence.
        """
    )

    st.subheader("1.1 Identify Business Value")
    st.markdown(
        """
        - Define the "why" and What key performance indicators (KPI) or business metrics this system will improve. 
        - Align stakeholders (business, IT, domain experts)
        - This could be:
            - Reduce churn by 15%
            - Improve fraud detection accuracy by 10%
            - Automate 20% of customer support tickets
        """
    )

    st.subheader("1.2 Formulate Machine Learning Problem")
    st.markdown(
        """
        - Classification, Regression, Clustering
        - Define:
            - Inputs (features)
            - Outputs (target variable)
        - Choose metrics:
            - Accuracy, Precision, Recall, F1-score, MAE
        """
    )

    st.subheader("1.3 Feasibility & Risk Assessment")
    st.markdown(
        """
        - Data availability  
        - Expected model performance  
        - Ethical risks (bias, fairness, compliance)
        """
    )

    # -----------------------------
    # PHASE 2
    # -----------------------------
    st.header("📊 Phase 2: Data Strategy & Engineering")

    st.write("Data is the foundation of all AI intelligent systems.")

    st.subheader("2.1 Data Sourcing and Collection")
    st.markdown(
        """
        
        **Identify Sources:** Internal databases (CRM, ERP), application logs, third-party APIs, public datasets, or synthetic data generation.
        **Data Ingestion:** Build robust pipelines to collect data, handling batch or real-time streaming (using tools like Apache Kafka, Apache Airflow).
        """
    )

    st.subheader("2.2 Exploratory Data Analysis (EDA)")
    st.markdown(
        """
        Statistical Summary: Understand data distributions and relationships, analyze distributions, missing values, outliers, and data types.

        Visualization: Use plots (histograms, correlation matrices, scatter plots, box plots, pair plots) to uncover patterns, anomalies, and relationships between features and the target variable.

        Detect missing values and outliers 
         
        Hypothesis Testing: Validate assumptions about the data with domain experts.
        """
    )

    st.subheader("2.3 Data Preparation & Processing")
    st.markdown(
        """
        **Data Cleaning:** Handle missing values (imputation or deletion), correct data types, remove duplicates, and address outliers.

        **Feature Engineering:** Transform raw data into features that better represent the underlying problem. This is a creative, iterative process. Examples:

        **Encoding:** Convert categorical variables (e.g., "country") into numerical formats (one-hot, label encoding).

        **Scaling:** Normalize or standardize features (e.g., Min-Max scaling, Z-score) for algorithms sensitive to magnitude.

        **Derived Features:** Create new features like "day of week" from a timestamp, or "purchase frequency" from transaction logs.

        **Data Splitting:** Partition the data into three distinct sets:

        **Training Set (60-80%):** Used to train the model.

        **Validation Set (10-20%):** Used for hyperparameter tuning and model selection.

        **Test Set (10-20%):** A completely unseen set used only for final evaluation. This set must remain untouched until the final phase to prevent data leakage. 
        """
    )

    st.code(
        """
        # Train / Validation / Test split
        train = 70%
        validation = 15%
        test = 15%
        """,
        language="python"
    )

    # -----------------------------
    # PHASE 3
    # -----------------------------
    st.header("🏗 Phase 3: Infrastructure & Architecture")

    st.markdown(
        """
        Batch vs. Real-Time:

        Batch: Model runs on a schedule (e.g., nightly recommendations). Simpler to implement.

        Real-Time/Streaming: Model serves predictions via an API with millisecond latency (e.g., fraud detection during a transaction). Requires more complex infrastructure (e.g., Kubernetes, Docker, API gateways).

        MLOps Pipeline: Design the automated pipeline for training, versioning, and deployment.  
        """
    )

    # -----------------------------
    # PHASE 4
    # -----------------------------
    st.header("⚙ Phase 4: Model Development & Experimentation")

    st.subheader("4.1 Baseline Model")
    st.write("Start simple before moving to complex models.")

    st.markdown(
        """
        Establish a Baseline
        Implement a simple heuristic or a very simple model (e.g., linear regression, dummy classifier) to establish a minimum performance threshold. The complex model must significantly outperform this baseline.

        Algorithm Selection: Choose algorithms based on problem type, data size, interpretability needs, and performance. Options range from tree-based methods (Random Forest, XGBoost) to neural networks (CNNs, RNNs, Transformers).

        Training Loop: Feed the training data into the model. The model iteratively adjusts its internal parameters to minimize a defined loss function.
        
        """)

    st.subheader("4.2 Model Training")
    st.markdown(
        """
        Algorithm Selection: Choose algorithms based on problem type, data size, interpretability needs, and performance. Options range from tree-based methods (Random Forest, XGBoost) to neural networks (CNNs, RNNs, Transformers).

        Training Loop: Feed the training data into the model. The model iteratively adjusts its internal parameters to minimize a defined loss function.
        """
    )

    st.subheader("4.3 Hyperparameter Tuning")
    st.markdown(
        """
        Systematically search for the optimal configuration of model settings (e.g., learning rate, number of layers, tree depth).

        Techniques: Grid Search, Random Search, Bayesian Optimization.
        
        """
        )

    st.subheader("4.4 Experiment Tracking")
    st.markdown(
        """
        Use an experiment tracking tool (e.g., MLflow, Weights & Biases) to log every run, including:
        -Code version

        -Hyperparameters

        -Model metrics (on training and validation sets)

        -Model artifacts

        This ensures reproducibility and provides a clear history for audit and comparison. 
        """
    )

    # -----------------------------
    # PHASE 5
    # -----------------------------
    st.header("📈 Phase 5: Evaluation & Explainability")
    st.markdown(
        """
        Before deployment, validate the model’s reliability and trustworthiness.
        """
        )
    st.subheader("5.1 Model Evaluation")
    st.markdown(
        
        """
        5.1 Final Model Evaluation
        Run the final model on the unseen test set. This provides the most realistic estimate of real-world performance.

        Analyze performance across different data slices (e.g., "How does the model perform on users from a specific region?"). This helps identify hidden biases or weaknesses.

        5.2 Robustness & Stress Testing
        Adversarial Testing: Test the model with malformed inputs or edge cases to see if it fails gracefully.

        Stability: Test performance under data drift scenarios (e.g., what if the input distribution shifts slightly?).

        5.3 Explainability (XAI)
        For high-stakes domains (finance, healthcare), use techniques to interpret model decisions.

        Model-Specific: Feature importance (for tree-based models).

        Model-Agnostic: LIME (Local Interpretable Model-agnostic Explanations) or SHAP (SHapley Additive exPlanations) to explain individual predictions.
        """             
    )
                

    # -----------------------------
    # PHASE 6
    # -----------------------------
    st.header("🚀 Phase 6: Deployment")

    st.markdown(
        """
        Move the model from a development environment into production.
        """
    )

    st.markdown(
        """
        6.1 Deployment Strategy
        API Endpoint: Wrap the model in a REST or gRPC service.

        Batch Inference: Run predictions on a scheduled job and store results in a database.

        Edge Deployment: Deploy the model on a device (e.g., mobile phone, IoT sensor) using frameworks like TensorFlow Lite or ONNX.

        6.2 CI/CD/CT Pipeline
        Continuous Integration (CI): Automate testing of code, data validation, and model training.

        Continuous Delivery (CD): Automate the deployment of the model artifact to a serving environment.

        Continuous Training (CT): Automate the process of retraining the model on new data to prevent staleness.

        6.3 Deployment Patterns
        Shadow Deployment: Run the new model in parallel with the existing system, logging its predictions without impacting end-users to validate its behavior.

        Canary Deployment: Roll out the new model to a small percentage of users (e.g., 5%) and gradually increase traffic while monitoring performance.

        Blue-Green Deployment: Maintain two identical environments (blue = current, green = new) and switch traffic instantly after validation.  
        """
    )

    # -----------------------------
    # PHASE 7
    # -----------------------------
    st.header("📡 Phase 7: Monitoring & Observability")

    st.markdown(
        """
        7.1 Monitor Key Metrics
        System Health: Latency, throughput, uptime, CPU/memory usage.

        Model Performance: Re-calculate accuracy, precision, etc., on ground-truth data as it becomes available (this is often delayed).

        Data Drift: Monitor the distribution of input features. A significant shift (e.g., a change in user demographics) indicates the model may become outdated.

        Concept Drift: Monitor the relationship between input features and the target variable. Has the underlying mapping changed?

        7.2 Alerting & Logging
        Set up automated alerts for metric degradation, data drift, or system failures.

        Maintain detailed logs of predictions and inputs for auditing and debugging.        
        """
    )

    # -----------------------------
    # PHASE 8
    # -----------------------------
    st.header("🔄 Phase 8: Iteration & Continuous Improvement")

    st.markdown(
        """
        Based on monitoring feedback, the system enters a cycle of improvement.

        Retraining: Trigger a new training pipeline when drift is detected or new data is available.

        Model Versioning: Maintain a registry of models (e.g., in a model registry like MLflow) to enable version control and quick rollbacks.

        A/B Testing: Continuously experiment with new model versions or features in production, using live traffic to statistically determine which version yields superior business outcomes.
        """
    )

    # -----------------------------
    # PHASE 9
    # -----------------------------
    st.header("⚖ Phase 9: Governance, Ethics & Compliance")

    st.markdown(
        """
        A cross-cutting concern that must be integrated into every phase.

        Bias & Fairness Audits: Regularly audit model predictions for disparate impact across protected groups (e.g., race, gender). Use fairness metrics like Demographic Parity or Equalized Odds.

        Data Privacy: Ensure data is anonymized or pseudonymized. Implement strict access controls.

        Explainability Logging: Store explanations for critical predictions to satisfy regulatory requirements (e.g., the "right to explanation" in GDPR).

        Compliance Documentation: Maintain a detailed audit trail of all data sources, model versions, decisions, and performance metrics for internal and external auditors. 
        """
    )

    # -----------------------------
    # WORKFLOW
    # -----------------------------
    st.header("🔁 System Workflow")

    st.code(
        """
Problem → Data → Model → Evaluation → Deployment 
→ Monitoring → Retraining → Improvement
        """,
        language="text"
    )

    st.success(
    "You now understand the full lifecycle of designing a production-grade intelligent system."
    )