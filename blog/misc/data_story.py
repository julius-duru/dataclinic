import streamlit as st
import pandas as pd

TITLE = "Data Analytics Terms in a Data Science Project"
CATEGORY = "misc"
KEYWORDS = ["feature engineering","data observability","real-time analytics","reverse ETL","window function","query optimization","imbalanced data","outlier","moving average","regularization","time series", "feature selection", "dimensionality", "ensemble method", "cross-validation", "data leakage", "hyperparameter tuning"]


def show():
    st.set_page_config(
        page_title="Data Analytics Terms in a Data Science Project",
        page_icon="",
        layout="wide"
    )

    st.title("Data Analytics Terms in a Data Science Project")
    st.subheader("Story of a real‑world data science project")

    st.markdown("""
    Sequence of data science project lifecycle. Below is the journey of Maya, a senior data scientist, as she builds a churn prediction model – from SQL extraction to production monitoring.
    """)

    # ------------------------------------------------------------
    st.header("Answering the Business Question")
    st.markdown("""
    The CEO asks: *“Who will churn in the next 30 days?”*  
    Maya starts by framing the problem – no modeling yet, just business understanding.
    """)

    # ------------------------------------------------------------
    st.header("Extracting the Data (SQL & Warehousing)")
    st.markdown("""
    - **Window Functions (Advanced SQL)** – Used to rank each customer’s last purchase:  
    `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY transaction_date DESC)`
    - **Query Optimization** – Adding indexes and studying execution plans to speed up slow queries.
    - **Columnar Lineage / Data Lineage** – Documenting where each column originates (e.g., `total_spend` comes from the `orders` table).
    """)

    # ------------------------------------------------------------
    st.header("Exploring the Data (EDA & Drift Detection)")
    st.markdown("""
    - **Data Drift** – Comparing distribution of `session_duration` between last month and this month.
    - **Concept Drift** – Checking if the relationship between features and target has changed over time.
    - **Stationarity** – Using Augmented Dickey‑Fuller test on daily active users; applying differencing if needed.
    - **Autocorrelation** – ACF/PACF plots to see if today’s activity correlates with yesterday’s.
    - **Time Series Decomposition** – Breaking data into trend, seasonality, and residuals.
    - **Heteroscedasticity** – Detecting non‑constant variance in residuals (affects confidence intervals).
    """)

    # ------------------------------------------------------------
    st.header("Cleaning & Preparing Features")
    st.markdown("""
    - **Outlier Treatment Techniques** – Capping extreme values at the 99th percentile.
    - **SMOTE / Undersampling** – Handling imbalanced classes (only 5% churn) – part of **Data Observability**.
    - **Multicollinearity** – Using VIF to detect high correlations between features (e.g., `total_orders` and `total_spend`); dropping one.
    - **Feature Selection** – Recursive feature elimination and mutual information to reduce noise.
    - **Dimensionality Reduction (PCA, SVD)** – Reducing 50 clickstream features to 10 principal components.
    - **Feature Engineering** – Creating “days since last purchase”, “average cart value”, “ratio of support tickets to orders”.
    """)

    # ------------------------------------------------------------
    st.header("Building the First Models")
    st.markdown("""
    - **Cross-Validation** – 5‑fold stratified CV to evaluate without overfitting.
    - **Bias‑Variance Tradeoff** – Balancing underfitting (high bias) vs overfitting (high variance).
    - **Regularization (L1/L2)** – Lasso (L1) for feature selection, Ridge (L2) for coefficient shrinkage.
    - **Hyperparameter Tuning** – Grid search and Bayesian optimization for parameters like `C`, tree depth, learning rate.
    - **Ensemble Methods** – Bagging (Random Forest), Boosting (XGBoost), and Stacking (meta‑learner on top).
    - **Data Leakage** – Avoiding future data (e.g., using next week’s purchases to predict this week’s churn) – the “Moving Average with future data” pitfall.
    """)

    # ------------------------------------------------------------
    st.header("Evaluating & Interpreting")
    st.markdown("""
    - **Moving Average (smoothing)** – Plotting error rate over batches to detect degradation.
    - **Heteroscedasticity (re‑check)** – Breusch‑Pagan test on residuals.
    - **Model interpretation** – SHAP values to explain predictions to the business.
    """)

    # ------------------------------------------------------------
    st.header("Deployment & Monitoring")
    st.markdown("""
    - **Real‑Time Analytics** – Streaming pipeline (Kafka + Flink) scoring users daily.
    - **Metric Layer / Semantic Layer** – Centralised logic for KPIs (e.g., “churn probability > 0.7”) used across dashboards, alerts, and reports.
    - **Data Observability** – Tools (Great Expectations, Monte Carlo) to monitor null rates, schema changes, and distribution shifts.
    - **Columnar Lineage** – Column‑level data lineage so upstream changes are propagated.
    - **Semantic Layer (operational)** – Writing predictions back to the CRM system for customer agents.
    """)

    # ------------------------------------------------------------
    st.header("The Never‑Ending Story")
    st.markdown("""
    Three months later, Maya detects **Concept Drift** again. She retrains the model, re‑runs **Hyperparameter Tuning**, and re‑checks **Multicollinearity** on fresh data.  
    The cycle continues – that’s the life of a data science project.
    """)

    # ------------------------------------------------------------
    st.header("Where Each Term Appears")
    summary_data = {
        "Term": [
            "Window Functions (SQL)", "Query Optimization", "Columnar Lineage / Data Lineage",
            "Data Drift", "Concept Drift", "Stationarity", "Autocorrelation", "Time Series Decomposition",
            "Heteroscedasticity", "Outlier Treatment", "SMOTE / Undersampling", "Multicollinearity",
            "Feature Selection", "Dimensionality Reduction", "Feature Engineering", "Cross‑Validation",
            "Bias‑Variance Tradeoff", "Regularization (L1/L2)", "Hyperparameter Tuning",
            "Ensemble Methods", "Data Leakage", "Moving Average (smoothing)", "Real‑Time Analytics",
            "Metric Layer / Semantic Layer", "Data Observability"
        ],
        "Project Step": [
            "Data extraction", "Data extraction", "Documentation & deployment",
            "EDA & monitoring", "EDA & monitoring", "Time series EDA", "Time series EDA", "Time series EDA",
            "Model diagnostics", "Data cleaning", "Data preparation", "Feature selection",
            "Feature engineering", "Feature engineering", "Feature engineering", "Model training",
            "Model training", "Model training", "Model tuning", "Model training",
            "Data preparation (caution)", "Evaluation & drift detection", "Deployment",
            "Deployment & reporting", "Monitoring"
        ]
    }

    import pandas as pd
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.caption("Every advanced analytics term finds its place in a real‑world project – from the first SQL query to the last alert in production.")