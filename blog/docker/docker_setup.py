import streamlit as st
import pandas as pd

TITLE = "Docker Setup for Portable and Reproducible MLOps"
CATEGORY = "docker"
KEYWORDS = [
    "Docker", "MLOps", "reproducibility", "model deployment", "container security",
    "Docker Compose", "performance monitoring", "MLflow", "DVC", "vLLM", "CI/CD",
    "multi‑stage builds", "health checks", "Prometheus", "cAdvisor"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Intermediate → Advanced (Production MLOps)")
    st.markdown("---")

    # INTRO 
    st.write(
        """
        Assume that you have built a great model. Next step is to deploy it on your colleague’s machine, a staging server, or a cloud GPU instance.  
        
        **Docker** solves the classic “it works on my laptop” problem by packaging your code, its environment, and its dependencies into a single portable unit.

        In this guide we’ll build a **production‑ready Docker setup for MLOps** that is:
        - **Portable** – runs identically on any Docker host (local, cloud, edge)  
        - **Reproducible** – same inputs → same outputs, every time  
        - **Maintainable** – easy to update, clean up, and monitor  
        - **Performant** – we’ll measure CPU, memory, and inference latency  
        - **Secure** – non‑root users, read‑only filesystems, vulnerability scanning

        > This is not a toy example – you’ll leave with a real `Dockerfile`, `docker-compose.yml`, and a checklist that works for training, serving, and experiment tracking.
        """
    )
    st.markdown("---")

    # 1. PROJECT STRUCTURE – blueprint
    st.header("Step 1 – Project Structure")
    st.write(
        """
        A clean layout is half the battle. Here’s what we’ll build:
        """
    )
    st.code(
        """
mlops-docker/
├── .env                      # environment variables (never commit secrets)
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── training/
│   ├── train.py
│   └── evaluate.py
├── serving/
│   ├── app.py                # FastAPI/Flask inference endpoint
│   └── wsgi.py
├── monitoring/
│   └── prometheus.yml        # optional
└── data/                     # volume mount for datasets & models
    ├── raw/
    └── models/
        """,
        language="text"
    )
    st.write(
        """
        - `data/` is a **volume mount** – datasets and models persist even after containers die.  
        - `training/` and `serving/` are separated so you can rebuild one without touching the other.  
        - `.dockerignore` keeps secrets and large files out of your image.
        """
    )

    with st.expander("`.dockerignore` – what to exclude", expanded=False):
        st.code(
            """
__pycache__
*.pyc
.git
data/raw/*.csv
*.pkl
.env
            """,
            language="text"
        )
        st.caption("Exclude caches, local data, and secrets – keeps images small and safe.")

    st.markdown("---")

    # 2. DOCKERFILE – multi‑stage, secure
    st.header("Step 2 – Writing the Dockerfile (Multi‑Stage & Secure)")
    st.write(
        """
        A **multi‑stage build** keeps your final image tiny and secure. We’ll have a `base` stage with common dependencies, then `training` and `serving` stages that inherit from it.
        """
    )

    dockerfile_code = """
# ---- base stage (common dependencies) ----
FROM python:3.10-slim AS base
ENV PYTHONUNBUFFERED=1 \\
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

# Install system dependencies (build-essential for some pip packages)
RUN apt-get update && apt-get install -y --no-install-recommends \\
    build-essential \\
    curl \\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- training stage ----
FROM base AS training
COPY training/ ./training/
ENTRYPOINT ["python", "training/train.py"]

# ---- serving stage ----
FROM base AS serving
# Create non‑root user
RUN useradd --create-home --shell /bin/bash mluser && chown -R mluser:mluser /app
USER mluser

COPY serving/ ./serving/
EXPOSE 8000
CMD ["uvicorn", "serving.app:app", "--host", "0.0.0.0", "--port", "8000"]
"""
    st.code(dockerfile_code, language="dockerfile")
    st.write(
        """
        **Why this matters:**  
        - `python:3.10-slim` – small image, fewer vulnerabilities.  
        - `USER mluser` – never run as root inside a container (critical security practice).  
        - `--no-cache-dir` – saves disk space.  
        - Multi‑stage = no build tools or training code end up in the serving image.
        """
    )
    st.markdown("---")

    # 3. DOCKER COMPOSE – orchestrate training, serving, MLflow
    st.header("Step 3 – Docker Compose: Your MLOps Orchestra")
    st.write(
        """
        With Compose you define all services (training, serving, MLflow) in one YAML file.  
        Run everything with `docker compose up -d`.
        """
    )
    compose_code = """
version: '3.8'

services:
  training:
    build:
      context: .
      target: training
    image: mlops-training:latest
    volumes:
      - ./data:/app/data          # datasets & saved models
      - ./training/logs:/app/logs
    environment:
      - MLFLOW_TRACKING_URI=http://mlflow:5000
      - DATA_PATH=/app/data/raw/dataset.csv
    command: --epochs 10 --batch-size 32
    deploy:
      resources:
        limits:
          memory: 8G
          cpus: '4'

  serving:
    build:
      context: .
      target: serving
    image: mlops-serving:latest
    ports:
      - "8000:8000"
    volumes:
      - ./data/models:/app/models:ro   # read‑only model cache
    environment:
      - MODEL_PATH=/app/models/latest.pkl
      - LOG_LEVEL=info
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 5s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 2G
          cpus: '1'

  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.7.1
    ports:
      - "5000:5000"
    volumes:
      - ./data/mlflow:/mlflow
    command: mlflow server --host 0.0.0.0 --backend-store-uri sqlite:///mlflow/mlflow.db
    restart: unless-stopped
"""
    st.code(compose_code, language="yaml")
    st.write(
        """
        **Key points:**  
        - **Resource limits** prevent one service from starving the host.  
        - **Health check** for the serving service – Docker will restart it if it fails.  
        - **Volumes** persist data (`./data`), logs, and MLflow artifacts.  
        - `:ro` means the serving container can only **read** models – extra security.
        """
    )
    st.markdown("---")

    # 4. REPRODUCIBILITY – pin everything
    st.header("Step 4 – Guaranteeing Reproducibility")
    st.write(
        """
        Docker gives you the same environment, but you also need to pin **data, code, and hyperparameters**.
        """
    )
    with st.expander(" How to make any run 100% reproducible", expanded=True):
        st.markdown(
            """
            - **Pin base image digest** – replace `python:3.10-slim` with `python:3.10-slim@sha256:abc123...` (get digest from Docker Hub).  
            - **Lock Python dependencies** – generate `requirements.lock` via `pip freeze` and copy it into the image.  
            - **Version data with DVC** – mount a DVC remote inside the container and run `dvc pull`.  
            - **Log everything with MLflow** – hyperparameters, metrics, model URI. The MLflow server runs in its own container.
            """
        )
        st.code(
            "# Inside Dockerfile – use locked dependencies\n"
            "COPY requirements.lock .\n"
            "RUN pip install --no-cache-dir -r requirements.lock",
            language="dockerfile"
        )
    st.markdown("---")

    # 5. MAINTENANCE – keep containers healthy
    st.header(" Step 5 – Maintenance Strategies")
    st.write(
        """
        A pipeline that’s not maintained will rot. Here’s how to keep it fresh.
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Weekly rebuilds**")
        st.code("docker build --pull --no-cache -t mlops-serving .", language="bash")
        st.caption("`--pull` gets latest base image patches.")
    with col2:
        st.markdown("**Monthly prune**")
        st.code("docker system prune -af --volumes", language="bash")
        st.caption("Removes unused images, containers, volumes – free disk space.")

    st.markdown("**Log rotation** – add this to each service in `docker-compose.yml`:")
    st.code(
        """
logging:
  driver: "json-file"
  options:
    max-size: "10m"
    max-file: "3"
        """,
        language="yaml"
    )
    st.info("Health checks (already in Compose) act as automatic maintenance – unhealthy containers get restarted.")
    st.markdown("---")

    # 6. PERFORMANCE CHECKS – measure and monitor
    st.header("Step 6 – Performance Checks")
    st.write(
        """
        You can’t improve what you don’t measure. Let’s look at real‑time and historical monitoring.
        """
    )
    with st.expander("Quick `docker stats`", expanded=False):
        st.code("docker stats mlops_serving_1", language="bash")
        st.write("Shows live CPU, memory, network I/O, and disk reads/writes per container.")
    with st.expander("Full stack: cAdvisor + Prometheus + Grafana", expanded=False):
        st.write(
            """
            Add this service to your `docker-compose.yml` to collect container metrics:
            """
        )
        st.code(
            """
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
            """,
            language="yaml"
        )
        st.write("Then point Prometheus to `cadvisor:8080` and visualize with Grafana.")
    with st.expander("Inference latency benchmark", expanded=False):
        st.code(
            "hey -z 30s -c 10 http://localhost:8000/predict",
            language="bash"
        )
        st.caption("`hey` is a tiny load generator. Replace with `wrk` or `locust` for more advanced scenarios.")
    with st.expander("🎮 GPU performance (if using CUDA)", expanded=False):
        st.code(
            "docker run --gpus all nvidia/cuda:12.0-base nvidia-smi",
            language="bash"
        )
        st.write("Inside the container, use `nvidia-smi` or `py-spy` to profile GPU kernels.")
    st.markdown("---")

    # 7. SECURITY HARDENING – non‑negotiable
    st.header("Step 7 – Security Hardening (Do This Before Production)")
    st.write(
        """
        Containers share the host kernel – a compromised container can wreck your whole system.  
        Follow these **seven pillars** of container security.
        """
    )
    security_df = pd.DataFrame({
        "Measure": [
            "Non‑root user",
            "Read‑only root filesystem",
            "Drop all capabilities",
            "Secrets management",
            "Image vulnerability scanning",
            "Network isolation",
            "Signed images"
        ],
        "Implementation": [
            "`USER mluser` in Dockerfile",
            "`read_only: true` + `tmpfs: /tmp` in compose",
            "`cap_drop: ALL` in compose",
            "Use Docker secrets or `--env-file` – never bake secrets",
            "`trivy image mlops-serving:latest` in CI",
            "Internal network for training & DB, expose only serving",
            "`export DOCKER_CONTENT_TRUST=1`"
        ]
    })
    st.dataframe(security_df, use_container_width=True)
    st.code(
        """
# Security snippet for docker-compose.yml
services:
  serving:
    read_only: true
    tmpfs: /tmp
    cap_drop: ALL
    security_opt:
      - no-new-privileges:true
    networks:
      - internal
      - public
        """,
        language="yaml"
    )
    st.markdown("---")

    # 8. DEPLOYMENT ORCHESTRATION (Swarm / Kubernetes)
    st.header("Step 8 – From Compose to Production")
    st.write(
        """
        For a single host, **Docker Swarm** is built‑in and uses your same `docker-compose.yml`.  
        For multi‑node, move to **Kubernetes** (but keep your Docker images as the portable artifact).
        """
    )
    st.code(
        """
# Deploy to Swarm
docker stack deploy -c docker-compose.yml mlops

# Zero‑downtime update of serving service
docker service update --image mlops-serving:latest mlops_serving
        """,
        language="bash"
    )
    st.info("On Kubernetes, consider using `kubectl` with a `Deployment` and `Service` – but the image stays exactly the same.")
    st.markdown("---")

    # 9. BEGINNER'S CHECKLIST (condensed but complete)
    st.header("Your End‑to‑End Docker MLOps Checklist")
    st.write(
        """
        Tick off each item before you go to production.
        """
    )
    checklist = """
    **Before writing the Dockerfile:**  
    - [ ] Have I created a `.dockerignore` to exclude secrets, caches, and large data files?  
    - [ ] Did I decide which stages I need (training, serving, maybe data preprocessing)?  

    **Building the image:**  
    - [ ] Does the base image use a specific digest (`@sha256:...`) for reproducibility?  
    - [ ] Are Python dependencies pinned in a `requirements.lock` file?  
    - [ ] Did I create a non‑root user for the serving stage?  

    **Docker Compose orchestration:**  
    - [ ] Are volumes used for datasets, models, and logs (so they persist)?  
    - [ ] Does every service have resource limits (`deploy.resources`)?  
    - [ ] Does the serving service have a healthcheck?  
    - [ ] Are secrets injected via environment files or Docker secrets, never hardcoded?  

    **Performance & monitoring:**  
    - [ ] Can I run `docker stats` and understand the numbers?  
    - [ ] Have I set up cAdvisor + Prometheus for historical metrics?  
    - [ ] Did I benchmark inference latency with a realistic load tool?  

    **Security (before production):**  
    - [ ] Is the root filesystem read‑only for serving?  
    - [ ] Have I dropped all capabilities (`cap_drop: ALL`)?  
    - [ ] Did I run `trivy image` on the final image and fix critical vulnerabilities?  
    - [ ] Is the training network isolated from the public internet?  

    **Maintenance plan:**  
    - [ ] Is there a weekly CI job to rebuild with `--pull --no-cache`?  
    - [ ] Are log rotation settings configured?  
    - [ ] Do I have a monthly calendar reminder to run `docker system prune`?  
    """
    st.markdown(checklist)
    st.success("Check everything – then you’re ready for production-grade MLOps with Docker.")
    st.markdown("---")

    # 10. CONCLUSION & NEXT STEPS
    st.header("Keep It Simple, then Iterate")
    st.write(
        """
        You don’t need Kubernetes or a dozen microservices from day one.  
        **Start with this single `docker-compose.yml`** on a single server.  
        It already gives you portability, reproducibility, health checks, and basic security.

        **Your next actions:**  
        1. Take an existing ML training script and put it into `training/train.py`.  
        2. Build the image and run `docker compose up training` – verify it works.  
        3. Add a simple FastAPI endpoint in `serving/app.py` and test inference.  
        4. Run `trivy image` and fix any critical vulnerabilities.  

        Docker is the foundation; MLOps is the house. Build a solid foundation, and the house will stand.
        """
    )
    st.markdown("---")

    # 11. EXTERNAL RESOURCES – books, docs, tools
    st.header("🔗 Great Resources for Further Reading")
    st.markdown(
        """
        **Official Docker & Security guides**  
        - [Docker security best practices (official docs)](https://docs.docker.com/engine/security/)  
        - [Docker Bench Security – CIS benchmark script](https://github.com/docker/docker-bench-security)  
        - [Trivy – vulnerability scanner for containers](https://trivy.dev)  

        **MLOps with Docker – in‑depth**  
        - [MLflow + Docker example (MLflow docs)](https://mlflow.org/docs/latest/tracking.html#logging-to-a-tracking-server)  
        - [DVC with Docker – data versioning inside containers](https://dvc.org/doc/use-cases/versioning-data-and-models)  
        - [Kubeflow pipelines – containerized steps](https://www.kubeflow.org/docs/components/pipelines/)  

        **Performance monitoring**  
        - [cAdvisor + Prometheus + Grafana step‑by‑step (blog)](https://prometheus.io/docs/guides/cadvisor/)  
        - [hey – HTTP load generator](https://github.com/rakyll/hey)  

        **Books**  
        - “Docker Deep Dive” by Nigel Poulton – practical, conversational.  
        - “Designing Data‑Intensive Applications” by Martin Kleppmann – chapters on container orchestration.  
        - “Machine Learning Engineering in Action” by Ben Wilson – includes a full Docker MLOps case study.  
        """
    )
    st.markdown("---")
    st.caption("© 2026 | Step‑by‑Step Docker Setup for MLOps | Build once, run anywhere – securely and reproducibly.")
