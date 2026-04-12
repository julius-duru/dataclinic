import streamlit as st
import pandas as pd

TITLE = "MLOps End-to-End Pipeline"
CATEGORY = "machine_learning"
KEYWORDS = [
    "MLOps pipeline", "FastAPI", "MLflow", "Docker", "Airflow", "model registry",
    "CI/CD", "GitLab CI", "GitHub Actions", "Prometheus", "Grafana", "model drift",
    "retraining automation", "staging environment", "Kubernetes", "ArgoCD",
    "unit testing", "integration testing", "performance testing"
]

def show():
    st.title(TITLE)
    st.caption("Category: MLOps | Level: Intermediate → Advanced")
    st.markdown("---")

    # INTRODUCTION
    st.write(
        """
        Building and deploying machine learning models is only half the battle.  
        The real challenge lies in **operationalizing them** – automating data pipelines,
        versioning models, serving them reliably, monitoring for drift, and retraining automatically.

        This guide presents a **complete, hands‑on MLOps pipeline** using:

        - **FastAPI** for model serving (REST API)
        - **MLflow** for experiment tracking and model registry
        - **Docker** for containerisation (standardised, portable)
        - **Apache Airflow** (or Prefect) for data collection & cleaning
        - **GitLab CI / GitHub Actions** for CI/CD
        - **Prometheus + Grafana** for monitoring
        - **ArgoCD** for GitOps‑based deployment (staging → production)
        - **Alertmanager + drift detection** to trigger automatic retraining

        Every component runs in Docker containers, and the entire workflow is **production‑ready**.
        """
    )

    st.divider()

    # ============================================
    # SECTION 1: Data Collection & Cleaning (Airflow)
    # ============================================
    st.header("1. Data Collection & Cleaning – Apache Airflow (or Prefect)")

    st.write(
        """
        Raw data comes from databases, APIs, logs, or IoT devices.  
        We use **Airflow** to orchestrate batch ingestion and cleaning.
        """
    )
    st.subheader("Hands‑on Steps")
    st.markdown(
        """
        - **Launch Airflow** with Docker Compose (including PostgreSQL, Redis, S3/minio volumes).
        - **Create a DAG** that:
            - Extracts data from a source (e.g., `requests.get` or `pandas.read_sql`).
            - Cleans data (handles missing values, duplicates, outliers).
            - Validates schema/quality with **Great Expectations**.
            - Stores processed data as Parquet in S3/minio (or a feature store like Feast).
        """
    )
    st.code(
        """
from airflow.decorators import dag, task
from datetime import datetime

@dag(start_date=datetime(2026,04,04), schedule="@daily", catchup=False)
def ml_pipeline():
    @task
    def extract():
        return pd.read_csv("s3://raw/transactions.csv")

    @task
    def clean(df):
        df = df.dropna().drop_duplicates()
        return df

    @task
    def validate(df):
        ge_df = GreatExpectations(...)
        ge_df.expect_column_values_to_not_be_null("amount")
        return ge_df.validate()

    clean(extract()) >> validate()
        """,
        language="python"
    )
    st.info("📦 **Containerisation:** Airflow webserver, scheduler, and workers each run in separate containers defined in `docker-compose.yml`.")

    st.divider()

    # ============================================
    # SECTION 2: Model Development & MLflow
    # ============================================
    st.header("2. Model Development & Experiment Tracking – MLflow")

    st.write(
        """
        Train multiple models, log parameters, metrics, and artifacts.  
        **MLflow** tracks everything and registers the best model.
        """
    )
    st.subheader("Hands‑on Steps")
    st.markdown(
        """
        - Run **MLflow Tracking Server** in a Docker container with PostgreSQL backend and S3/minio artifact store.
        - Write a training script (`train.py`) that:
            - Loads cleaned data from step 1.
            - Splits train/test.
            - Trains a model (scikit‑learn, XGBoost, PyTorch, etc.).
            - Logs hyperparameters, metrics (accuracy, F1, latency).
            - Registers the best model in **MLflow Model Registry**.
        """
    )
    st.code(
        """
import mlflow
with mlflow.start_run():
    mlflow.log_params(params)
    mlflow.log_metrics({"accuracy": acc, "f1": f1})
    mlflow.sklearn.log_model(model, "model")
    mlflow.register_model(f"runs:/{run_id}/model", "FraudDetector")
        """,
        language="python"
    )
    st.write("The training job is also **containerised** and can be triggered manually or from Airflow.")

    st.divider()

    # ============================================
    # SECTION 3: Model Validation & Testing
    # ============================================
    st.header("3. Model Validation & Testing – Unit, Integration, Performance")

    st.write(
        """
        Before deployment, we ensure code quality, data contract, model behaviour, and inference speed.
        """
    )
    testing_table = pd.DataFrame({
        "Test Type": ["Unit tests", "Integration tests", "Performance tests"],
        "Tool / Framework": ["pytest", "pytest", "Locust / k6"],
        "What is verified": [
            "Data cleaning functions, feature engineering, model prediction shape",
            "End‑to‑end from data ingestion to model inference (small dataset)",
            "Simulate 100 req/s, measure p95 latency"
        ]
    })
    st.dataframe(testing_table, use_container_width=True)

    st.code(
        """
# Example CI job (GitLab CI)
test:
  script:
    - pytest tests/unit
    - pytest tests/integration
    - locust -f tests/performance/locustfile.py --headless -u 50 -r 5 --run-time 30s
        """,
        language="yaml"
    )
    st.success("All tests run inside a Docker container identical to production.")

    st.divider()

    # ============================================
    # SECTION 4: Model Registry – MLflow
    # ============================================
    st.header("4. Model Registry – MLflow")

    st.write(
        """
        The **Model Registry** is the single source of truth for all production‑ready and candidate models.
        """
    )
    st.subheader("Key capabilities")
    st.markdown(
        """
        - **Version control** for models (every change gets a unique version)
        - **Metadata tracking** (hyperparameters, metrics, training data hash)
        - **Stage transitions**: `None` → `Staging` → `Production` → `Archived`
        - **Approval workflows** (manual or automated)
        - **Rollback** – redeploy any previous version with one command
        """
    )
    st.code(
        """
# Promote a model version to Production
mlflow transition-model-stage --name "FraudDetector" --version 2 --stage "Production"
        """,
        language="bash"
    )
    st.info("The FastAPI serving container always pulls the **latest Production** model from MLflow.")

    st.divider()

    # ============================================
    # SECTION 5: FastAPI Serving Container
    # ============================================
    st.header("5. Build FastAPI Serving Container")

    st.write(
        """
        Expose the model as a REST API with health checks and Prometheus metrics.
        """
    )
    st.code(
        """
from fastapi import FastAPI
import mlflow
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
def load_model():
    global model
    model = mlflow.pyfunc.load_model("models:/FraudDetector/Production")

@app.post("/predict")
def predict(features: dict):
    df = pd.DataFrame([features])
    pred = model.predict(df)
    return {"prediction": int(pred[0])}

instrumentator.expose(app)   # exposes /metrics for Prometheus
        """,
        language="python"
    )
    st.write("**Dockerfile** example:")
    st.code(
        """
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
        """,
        language="dockerfile"
    )

    st.divider()

    # ============================================
    # SECTION 6: CI/CD Pipeline
    # ============================================
    st.header("6. Automated CI/CD – GitLab CI / GitHub Actions + Jenkins")

    st.write(
        """
        The pipeline automatically builds, tests, and deploys the model container to staging and production.
        """
    )
    st.subheader("Example `.gitlab-ci.yml` (simplified)")
    st.code(
        """
stages:
  - test
  - build
  - deploy-staging
  - deploy-prod

variables:
  DOCKER_IMAGE: $CI_REGISTRY/mlops/fastapi-model

unit-test:
  stage: test
  script: docker run --rm $DOCKER_IMAGE pytest tests/unit

build:
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE:$CI_COMMIT_SHA .
    - docker push $DOCKER_IMAGE:$CI_COMMIT_SHA

deploy-staging:
  stage: deploy-staging
  script:
    - kubectl set image deployment/fastapi-staging fastapi=$DOCKER_IMAGE:$CI_COMMIT_SHA -n staging
  only:
    - main

deploy-prod:
  stage: deploy-prod
  script:
    - kubectl set image deployment/fastapi-prod fastapi=$DOCKER_IMAGE:$CI_COMMIT_SHA -n prod
  when: manual
        """,
        language="yaml"
    )
    st.write("**Jenkins alternative:** Declarative pipeline with stages: Checkout → Test → Build → Push → Deploy to staging → Smoke tests → Promote to prod.")

    st.divider()

    # ============================================
    # SECTION 7: Staging Environment
    # ============================================
    st.header("7. Staging Environment – Test with Real Data")

    st.write(
        """
        Before full production rollout, we validate the model in a **pre‑production environment**.
        """
    )
    st.markdown(
        """
        - Deploy the same FastAPI container to a separate Kubernetes namespace (`staging`).
        - Feed it a copy of recent real data (anonymised) via an Airflow task.
        - Use **canary** or **shadow mode** – route a small percentage of real traffic to the staging model.
        - Compare predictions against ground truth (if available) or against the current production model.
        """
    )
    st.info("Only after staging validation (e.g., 24 hours with no performance degradation) does the model get promoted to production.")

    st.divider()

    # ============================================
    # SECTION 8: Production Deployment – ArgoCD (GitOps)
    # ============================================
    st.header("8. Production Deployment – GitOps with ArgoCD (RBCD)")

    st.write(
        """
        **ArgoCD** synchronises the production Kubernetes manifests from a Git repository.  
        This gives you **declarative, auditable, and automated deployments**.
        """
    )
    st.code(
        """
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-prod
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: api
        image: registry/mlops/fastapi-model:latest
        ports:
        - containerPort: 8000
        env:
        - name: MLFLOW_TRACKING_URI
          value: "http://mlflow-tracking:5000"
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
        """,
        language="yaml"
    )
    st.write("When CI pushes a new image tag, ArgoCD automatically rolls out the change (or requires manual sync). Rolling updates ensure zero downtime.")

    st.divider()

    # ============================================
    # SECTION 9: Monitoring – Prometheus + Grafana
    # ============================================
    st.header("9. Continuous Monitoring – Prometheus & Grafana")

    st.write(
        """
        Monitor **system health**, **prediction latency**, **data drift**, and **model performance**.
        """
    )
    monitoring_table = pd.DataFrame({
        "What is monitored": [
            "Request count, latency, error rate (FastAPI `/metrics`)",
            "CPU / memory (node exporters)",
            "Data drift (PSI, KL divergence) – computed by sidecar",
            "Model accuracy (if ground truth arrives later)"
        ],
        "Tool / Method": [
            "Prometheus scrapes `/metrics`",
            "Prometheus node exporter",
            "Evidently AI / custom Python script",
            "Batch job comparing predictions with labels"
        ]
    })
    st.dataframe(monitoring_table, use_container_width=True)

    st.code(
        """
# Example: drift detection with Evidently
from evidently.report import Report
from evidently.metrics import DatasetDriftMetric

report = Report(metrics=[DatasetDriftMetric()])
report.run(reference_data=training_data, current_data=recent_data)
drift_score = report.as_dict()['metrics'][0]['result']['dataset_drift']
# Push drift_score to Prometheus (e.g., via pushgateway)
        """,
        language="python"
    )

    st.divider()

    # ============================================
    # SECTION 10: Alerting & Automatic Retraining
    # ============================================
    st.header("10. Alerting & Automatic Retraining – Closing the Loop")

    st.write(
        """
        When data or customer behaviour changes, the model must be **retrained automatically**.
        """
    )
    st.subheader("Prometheus Alerting Rule")
    st.code(
        """
groups:
- name: mlops
  rules:
  - alert: ModelDriftDetected
    expr: model_drift_score > 0.2
    for: 10m
    annotations:
      summary: "Model drift detected (PSI > 0.2)"
        """,
        language="yaml"
    )
    st.subheader("Webhook → Retraining Pipeline (Airflow)")
    st.markdown(
        """
        Alertmanager sends a webhook to **Airflow**, which triggers a retraining DAG:

        1. Collect latest cleaned data.
        2. Train a new model (MLflow run).
        3. Compare new metrics with current production model.
        4. If improved, register the new model as `Staging`.
        5. Run validation tests.
        6. Promote to `Production` (MLflow stage transition).
        7. ArgoCD automatically redeploys the FastAPI service (it pulls the latest Production model).
        """
    )
    st.success("✅ The pipeline is now **self‑healing** – models adapt to changing data without manual intervention.")

    st.divider()

    # ============================================
    # SUMMARY TABLE – ALL TOOLS
    # ============================================
    st.header("Complete Toolchain Overview")

    toolchain = pd.DataFrame({
        "Step": [
            "Data collection & cleaning",
            "Experiment tracking",
            "Model registry",
            "Model serving",
            "Containerisation",
            "CI/CD",
            "Deployment (GitOps)",
            "Staging validation",
            "Monitoring",
            "Alerting & retraining"
        ],
        "Technology": [
            "Apache Airflow (or Prefect) + Great Expectations",
            "MLflow Tracking",
            "MLflow Model Registry",
            "FastAPI",
            "Docker + Docker Compose / Kubernetes",
            "GitLab CI / GitHub Actions (or Jenkins)",
            "ArgoCD",
            "Kubernetes namespace + real data replay",
            "Prometheus + Grafana + Evidently AI",
            "Prometheus Alertmanager + Airflow retrain DAG"
        ]
    })
    st.dataframe(toolchain, use_container_width=True)

    st.divider()

    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")

    st.write(
        """
        This **end‑to‑end MLOps pipeline** transforms isolated ML experiments into a **production‑grade, automated, and governed system**.  

        Key takeaways:
        - **Every component is containerised** – portable and reproducible.
        - **Airflow orchestrates data** and retraining pipelines.
        - **MLflow provides the model registry** – versioning, stage transitions, and rollbacks.
        - **CI/CD (GitLab CI / GitHub Actions) automates testing and deployment**.
        - **ArgoCD enables GitOps** for Kubernetes deployments.
        - **Prometheus + Grafana monitor** performance and drift.
        - **Alertmanager + Airflow close the loop** with automatic retraining.

        By adopting this stack, you move from fragile, manual workflows to a **robust, scalable, and self‑healing ML platform**.
        """
    )

    st.divider()
    st.caption(f"📖 Article: {TITLE} | Category: {CATEGORY} | Level: Intermediate → Advanced")