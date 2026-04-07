import streamlit as st
import pandas as pd

TITLE = "MLOps Workflow - Training to Production with Automated Retraining"
CATEGORY = "misc"
KEYWORDS = ["MLOps", "model serialization", "pickle vs joblib", "model retraining", "drift detection", "Docker", "FastAPI", "continuous training", "MLflow", "Kubernetes"]


def show():
    st.title("Modern MLOps Workflow - Training to Production with Automated Retraining")
    st.caption("Category: misc | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        This article is for Data scientists, ML engineers, MLOps practitioners, and technical leads.
        The core themes include serialization formats (pickle vs joblib), API serving, containerization, automated retraining pipelines, and drift detection.
        
        **Why This Guide Matters**
        
        - **If you are a data scientist:** You will learn how to move your notebook models into production reliably. You will understand why serialization format matters and how to structure a model for serving.
        - **If you are an ML engineer or MLOps lead:** You will gain a detailed end-to-end pipeline with retraining triggers, a comparison of serialization methods, and a reusable framework for continuous training (CT).
        
        > The best ML models are not just accurate — they are reproducible, scalable, and self-improving.
        
        Below, we present the core workflow (Train → Serialize → Build API → Containerize), an explanation of pickle vs joblib, a complete retraining pipeline, and the key factors that determine when a model should be retrained.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 1: The Core Workflow Overview
    # ============================================
    st.header("1. The Core MLOps Workflow: Train → Serialize → Build API → Containerize")
    
    st.write(
        """
        This workflow represents the journey of a machine learning model from development to production deployment. It ensures your model is reproducible, scalable, and easy to integrate with applications.
        
        **1. Train** – Build the model using data.  
        **2. Serialize** – Save the trained model into a portable file.  
        **3. Build the API** – Wrap the model so applications can call it.  
        **4. Containerize** – Package everything for consistent, scalable deployment.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 2: Training Stage
    # ============================================
    st.header("2. Train – Model Development and Training")
    
    st.write(
        """
        In this stage, data becomes intelligence. You collect and prepare the dataset, explore features, run experiments, and select algorithms. Training is performed using frameworks such as Scikit-learn, TensorFlow, PyTorch, XGBoost, or LightGBM.
        
        **Outputs of this stage:**
        - A trained model object in memory.
        - Evaluation metrics (accuracy, F1, RMSE, etc.).
        - Versioned results (if using tools like DVC or MLflow).
        
        **Why it matters:** Everything after this step depends on the correctness and reproducibility of training.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 3: Serialization – pickle vs joblib
    # ============================================
    st.header("3. Serialize – Saving the Model: pickle vs joblib")
    
    st.write(
        """
        Serialization converts the in‑memory trained model into a file format that can be stored, versioned, and reloaded later without retraining. This makes the model portable and eliminates the cost of retraining on every service restart.
        
        Two popular formats in Python are pickle (.pkl) and joblib. The table below compares them.
        """
    )
    
    serial_data = {
        "Aspect": ["Built-in", "Optimized for NumPy arrays", "Load speed for large models", "File size", "Security", "Best for"],
        "pickle (.pkl)": [
            "Yes (Python standard library)", 
            "No", 
            "Slower", 
            "Larger", 
            "Risk – only load from trusted sources", 
            "Small Python objects, custom classes, lightweight models"
        ],
        "joblib (.joblib)": [
            "No (SciPy ecosystem)", 
            "Yes", 
            "Faster", 
            "Smaller", 
            "Safer when used with trusted models", 
            "Scikit-learn models, large NumPy arrays, performance-critical APIs"
        ]
    }
    df_serial = pd.DataFrame(serial_data)
    st.dataframe(df_serial, use_container_width=True)
    
    st.info(
        "**Recommendation:** For modern MLOps pipelines, especially those using Scikit-learn or any model with substantial array data, joblib is the preferred choice. "
        "Use native save methods for PyTorch (.pt) and TensorFlow (SavedModel). Use pickle only for small, generic Python objects where joblib offers no advantage."
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 4: Build the API
    # ============================================
    st.header("4. Build the API – Model Serving Layer")
    
    st.write(
        """
        After saving the model, you create an API that applications can call to get predictions. Popular tools include FastAPI (most common), Flask, Django REST, and gRPC.
        
        **Core steps:**
        1. Load the serialized model from disk or cloud storage on service startup.
        2. Expose HTTP endpoints: `/predict` for predictions, `/health` for health checks.
        3. Validate incoming request data (e.g., using Pydantic in FastAPI).
        4. Run inference using the loaded model.
        5. Return results in JSON format.
        
        **Why APIs?** They decouple the model from consuming applications, allowing independent updates and making the model accessible to websites, mobile apps, and microservices.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 5: Containerization
    # ============================================
    st.header("5. Containerize – Docker and DevOps Packaging")
    
    st.write(
        """
        Containerization (usually with Docker) packages the entire application – API code, model files, dependencies, and runtime – into a lightweight, reproducible, isolated unit called a container.
        
        **Typical Dockerfile steps:**
        - Choose a base image (e.g., `python:3.10-slim`).
        - Copy project files.
        - Install dependencies from `requirements.txt`.
        - Expose the API port (e.g., 8000).
        - Start the API server (e.g., `uvicorn main:app --host 0.0.0.0 --port 8000`).
        
        **Why containerization is essential:**
        - Ensures the model behaves identically across local, cloud, and production.
        - Makes scaling easy (Kubernetes, ECS, GKE, AKS).
        - Supports CI/CD pipelines for automated deployment.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 6: End-to-End Pipeline with Retraining Stages
    # ============================================
    st.header("6. End-to-End MLOps Pipeline with Detailed Retraining Stages")
    
    st.write(
        """
        The core workflow is the foundation. A complete, production‑ready MLOps pipeline adds data ingestion, feature engineering, deployment, monitoring, and an automated retraining loop. Below is the full pipeline structure.
        """
    )
    
    pipeline_data = {
        "Stage": [
            "1. Data Ingestion", 
            "2. Feature Engineering", 
            "3. Model Training (Initial)", 
            "4. Serialization", 
            "5. API + Containerization", 
            "6. Deployment", 
            "7. Monitoring & Drift Detection", 
            "8. Retraining Pipeline"
        ],
        "Description": [
            "Pull raw data from databases, cloud storage, APIs, or streams. Validate schema and quality.",
            "Clean, encode, scale, and select features. Output to feature store and train/test splits.",
            "Select algorithm, tune hyperparameters, cross-validate, and log metrics with MLflow.",
            "Save model using joblib (or pickle) with metadata: version, data version, timestamp, metrics.",
            "Build FastAPI service, load model on startup, create endpoints. Containerize with Docker.",
            "Deploy to Kubernetes, ECS, or serverless. Enable autoscaling and monitoring dashboards.",
            "Track API latency, data drift, concept drift, and performance decay using EvidentlyAI, Prometheus + Grafana.",
            "Collect new data, detect drift, trigger retraining, evaluate, and promote if better."
        ]
    }
    df_pipeline = pd.DataFrame(pipeline_data)
    st.dataframe(df_pipeline, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 7: Detailed Retraining Pipeline Steps
    # ============================================
    st.header("7. Detailed Retraining Pipeline (Automated MLOps Loop)")
    
    st.write(
        """
        Retraining is not a manual, periodic task. It should be triggered by measurable signals. The retraining pipeline consists of the following steps:
        
        **Step 1: Collect New Data** – Incremental daily/weekly data, user feedback, or newly labeled ground truth.
        
        **Step 2: Compare New Data vs Old Data** – Perform data drift detection, feature drift detection, and target drift detection.
        
        **Step 3: Trigger Retraining If Needed** – Based on the factors listed in Section 8.
        
        **Step 4: Rebuild Features** – Apply the same transformations as the original training pipeline, using the feature store to ensure consistency.
        
        **Step 5: Retrain the Model** – Use the same pipeline code with the new data, including hyperparameter tuning and cross-validation. Log new metrics.
        
        **Step 6: Model Evaluation** – Compare the new model against the current production model using accuracy, F1, RMSE, latency, fairness, and bias checks.
        
        **Step 7: Approval** – If the new model is better, promote it to production (automated or with human approval). If worse, roll back.
        
        **Step 8: Redeploy the New Model** – Serialize, containerize, and deploy again, completing the continuous training (CT) loop.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 8: Factors That Flag Retraining
    # ============================================
    st.header("8. Key Factors That Flag Model Retraining")
    
    st.write(
        """
        Retraining should be driven by objective, measurable triggers. The following factors indicate that a model may have become stale or inaccurate.
        """
    )
    
    factors_data = {
        "Factor": [
            "Data Drift", 
            "Concept Drift", 
            "Performance Decay", 
            "Increase in Prediction Errors", 
            "Data Volume Threshold", 
            "Model Age Threshold", 
            "Business Rule Changes"
        ],
        "Description": [
            "Statistical distribution of input features changes (e.g., customer age, new products). Detected via PSI or Kolmogorov‑Smirnov test.",
            "Relationship between features and target changes (e.g., fraud patterns, seasonal shifts).",
            "Drop in metrics like accuracy, F1, or increase in RMSE beyond a threshold (e.g., F1 < 0.92).",
            "High number of misclassifications, manual corrections, or low‑confidence predictions.",
            "Retrain after collecting a certain amount of new data (e.g., every 10,000 new rows).",
            "Time‑based retraining (e.g., every 30, 60, or 90 days) for domains with gradual change.",
            "New product lines, market entry, or regulatory changes invalidate old assumptions."
        ],
        "Example Trigger": [
            "PSI > 0.25", 
            "Rolling accuracy drops 5% in a week", 
            "RMSE increases by 10%", 
            "User corrections exceed 2% of predictions", 
            "10,000 new labeled records available", 
            "Last retraining was 45 days ago", 
            "New region launched"
        ]
    }
    df_factors = pd.DataFrame(factors_data)
    st.dataframe(df_factors, use_container_width=True)
    
    st.error(
        "**Important:** Do not retrain on a fixed schedule without checking drift. "
        "Unnecessary retraining wastes compute and may introduce regressions. Always evaluate the new model against the current production model before deployment."
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 9: Real-World MLOps Deployment Example
    # ============================================
    st.header("9. Real-World MLOps Deployment Example")
    
    example_data = {
        "Step": ["Train", "Serialize", "API", "Containerize", "Deploy", "Monitor", "Retrain"],
        "Tool / Method": [
            "Jupyter + Scikit-learn", 
            "Joblib (model.joblib)", 
            "FastAPI with /predict endpoint", 
            "Docker (python:3.10-slim)", 
            "AWS ECS / Kubernetes", 
            "Prometheus + Grafana + EvidentlyAI", 
            "MLflow + Apache Airflow"
        ],
        "Description": [
            "Build model and tune hyperparameters.", 
            "Save model.pkl or model.joblib to cloud storage.", 
            "Load model on startup, validate input, return JSON predictions.", 
            "Build image: ml-app:latest, push to registry.", 
            "Deploy with autoscaling and load balancing.", 
            "Track latency, error rates, data drift, and concept drift.", 
            "Schedule daily drift checks; trigger retraining if drift detected or performance drops."
        ]
    }
    df_example = pd.DataFrame(example_data)
    st.dataframe(df_example, use_container_width=True)
    
    st.success(
        "👉 This combination creates a production-ready MLOps loop: train once, serve reliably, and retrain automatically when the data or environment changes."
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 10: Pro Tips for MLOps
    # ============================================
    st.header("10. Pro Tips for Production MLOps")
    
    pro_tips_data = {
        "Technique": [
            "Model Versioning", 
            "Artifact Registry", 
            "CI/CD for Models", 
            "Canary Deployments", 
            "Automated Rollback", 
            "Feature Store", 
            "Shadow Mode"
        ],
        "How to Implement": [
            "Tag each model with Git commit hash + data version (DVC) + training timestamp.",
            "Use MLflow Model Registry or S3 with structured paths: `s3://bucket/models/version/`.",
            "GitHub Actions or GitLab CI: on new data or drift trigger → retrain → test → deploy.",
            "Route 5% of traffic to new model version, compare metrics before full rollout.",
            "If new model's accuracy drops below threshold in production, automatically revert to last good version.",
            "Store and serve pre‑computed features (Feast, AWS Feature Store) for consistency between training and inference.",
            "Deploy new model alongside production model, log predictions without serving them, validate offline."
        ]
    }
    df_pro = pd.DataFrame(pro_tips_data)
    st.dataframe(df_pro, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # SECTION 11: Core Skills Progression for MLOps
    # ============================================
    st.header("11. Core Skills Progression: Beginner → Advanced in MLOps")
    
    skills_data = {
        "Skill Area": ["Model Training", "Serialization", "API Serving", "Containerization", "Retraining & Drift", "Orchestration"],
        "Beginner": [
            "Trains models in notebooks, logs metrics manually.",
            "Uses `pickle.dump()` without metadata.",
            "Runs a local Flask or FastAPI app.",
            "Writes a basic Dockerfile, runs container locally.",
            "Retrains manually on a schedule (e.g., monthly).",
            "Uses cron jobs or manual scripts."
        ],
        "Advanced / Lead": [
            "Uses MLflow for experiment tracking, hyperparameter tuning, and model registry.",
            "Chooses joblib for NumPy-heavy models, stores versioned artifacts in S3/GCS.",
            "Builds production‑grade FastAPI with Pydantic validation, async endpoints, and load testing.",
            "Optimizes Docker images (multi‑stage builds, slim images), deploys to Kubernetes with Helm.",
            "Implements automated drift detection (EvidentlyAI), triggers retraining via Airflow/Prefect, A/B tests new models.",
            "Orchestrates end‑to‑end pipelines with Kubeflow, Airflow, or ZenML; uses GitOps for deployment."
        ]
    }
    df_skills = pd.DataFrame(skills_data)
    st.dataframe(df_skills, use_container_width=True)
    
    st.write(
        """
        **Most important universal skill:**  
        *The ability to design for failure – monitoring, rollback, and retraining are not afterthoughts; they are core requirements.*
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 12: Best Practices Summary
    # ============================================
    st.header("12. Best Practices Summary")
    
    summary_data = {
        "Best Practice": [
            "Always version your models and data",
            "Use joblib for Scikit-learn, native formats for DL frameworks",
            "Containerize even for development",
            "Implement automated drift detection",
            "Retrain only when triggered by data or performance signals",
            "Use a feature store for consistency",
            "Monitor both system metrics and model metrics",
            "Automate rollback on performance degradation"
        ],
        "Why It Matters": [
            "Without versioning, you cannot reproduce or debug production issues.",
            "Wrong format leads to slow loading and larger images, affecting latency.",
            "Containers eliminate 'works on my machine' problems from day one.",
            "Drift is silent – it erodes model value before metrics show failure.",
            "Fixed‑schedule retraining wastes compute and may introduce regressions.",
            "Training‑serving skew is a major source of production errors.",
            "Latency spikes and prediction errors have different root causes.",
            "Manual rollback is too slow during an active incident."
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
        **For data scientists:** Start by moving your notebook model into a simple FastAPI container. Use joblib to serialize the model. Add a `/predict` endpoint. Run it locally with Docker. That single step bridges the gap from notebook to production.
        
        **For ML engineers and MLOps leads:** Implement the retraining pipeline with drift detection (EvidentlyAI) and workflow orchestration (Airflow or Prefect). Use MLflow for model registry and canary deployments. Build a dashboard that shows data drift and performance decay over time.
        
        > A great MLOps pipeline is not just about deploying a model – it is about keeping it accurate, safe, and self‑correcting.
        
        ---
        
        **Your winning formula:**
        
        1. Train with reproducibility (track code, data, hyperparameters).
        2. Serialize using the right format (joblib for most Python ML).
        3. Build a simple, validated API (FastAPI).
        4. Containerize everything (Docker + orchestration).
        5. Monitor for drift and performance decay.
        6. Retrain only when triggered by measurable signals.
        7. Automate evaluation, promotion, and rollback.
        
        **Next actions for you:**  
        1. Take a model you trained in a notebook. Serialize it with joblib and write a FastAPI script that loads it and returns predictions.  
        2. Write a Dockerfile for that API. Build and run it locally. Call the `/predict` endpoint using `curl` or Python `requests`.  
        3. Install EvidentlyAI and run a data drift report on your production data versus training data.  
        4. Define three retraining triggers (e.g., PSI > 0.2, accuracy drop > 5%, or 30 days elapsed). Automate one of them with a simple cron or Airflow DAG.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # ADDITIONAL RESOURCES (Best Resources)
    # ============================================
    st.header("Best Resources for Implementing Modern MLOps")
    
    st.markdown(
        """
        **Training and Experiment Tracking**  
        - [MLflow](https://mlflow.org) – Track experiments, log metrics, manage model registry.  
        - [Weights & Biases](https://wandb.ai) – Experiment visualization and collaboration.  
        - [DVC](https://dvc.org) – Version control for data and models.
        
        **Serialization**  
        - [Joblib Documentation](https://joblib.readthedocs.io) – Optimized for NumPy arrays.  
        - [Python pickle (use with caution)](https://docs.python.org/3/library/pickle.html)
        
        **API Serving**  
        - [FastAPI](https://fastapi.tiangolo.com) – Modern, high‑performance API framework.  
        - [Flask](https://flask.palletsprojects.com) – Lightweight alternative.
        
        **Containerization and Orchestration**  
        - [Docker](https://docker.com) – Container platform.  
        - [Kubernetes](https://kubernetes.io) – Production‑grade orchestration.  
        - [Amazon ECS / EKS documentation](https://aws.amazon.com/eks/)
        
        **Monitoring and Drift Detection**  
        - [EvidentlyAI](https://evidentlyai.com) – Open‑source drift and model performance monitoring.  
        - [Prometheus + Grafana](https://prometheus.io) – Metrics collection and dashboards.
        
        **Workflow and Retraining Orchestration**  
        - [Apache Airflow](https://airflow.apache.org) – Pipeline scheduling.  
        - [Prefect](https://prefect.io) – Modern workflow orchestration.  
        - [ZenML](https://zenml.io) – MLOps framework for reproducible pipelines.
        
        **End‑to‑End MLOps Platforms**  
        - [Kubeflow](https://kubeflow.org) – ML toolkit for Kubernetes.  
        - [AWS SageMaker Pipelines](https://aws.amazon.com/sagemaker/pipelines/)  
        """
    )
   
