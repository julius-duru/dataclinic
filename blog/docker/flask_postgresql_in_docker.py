import streamlit as st
import pandas as pd

TITLE = "Secure Architecture & CI/CD - Streamlit + PostgreSQL on Docker: "
CATEGORY = "docker"
KEYWORDS = [
    "docker", "streamlit", "postgresql", "docker-compose", "containerization",
    "CVE scanning", "Trivy", "GitHub Actions", "Docker registry", "GHCR",
    "security hardening", "volume persistence", "MLOps workflow"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Intermediate → Advanced (Production focus)")
    st.markdown("---")

    # INTRO – conversational tone
    st.write(
        """
        Once you are ready to ship your Streamlit app with a real database, then 
        wrapped in Docker. When you add PostgreSQL and proper security scanning, 
        you are building something that can actually survive the real world applications.

        **In this guide you will learn:**  
        - How to choose secure, minimal Docker images (and which ones to avoid)  
        - A complete `docker-compose.yml` that connects Streamlit to PostgreSQL  
        - Essential Docker commands – what they do and when to use them  
        - How to scan for CVEs and harden your containers  
        - How to push your images to GitHub Container Registry via GitHub Actions  
        - Networking, volumes, and MLOps considerations

        > Think of this as your **production checklist** for shipping Streamlit apps. No fluff, just battle-tested patterns.
        """
    )
    st.markdown("---")

    # 1. WHY THIS ARCHITECTURE MATTERS
    st.header("Why host PostgreSQL, streamit in Docker")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            **The problem:** Your Streamlit app needs a database, but:
            - Local SQLite doesn't scale
            - "Just install Postgres" leads to version conflicts
            - Your teammate can't reproduce your setup
            
            **The solution:** Docker Compose orchestrates both services in an isolated network. Your app talks to `postgres:5432` and it just works – on your laptop, on a cloud VM, anywhere.
            """
        )
    with col2:
        st.image("https://docs.docker.com/get-started/images/docker-compose.png", caption="Docker Compose multi-container architecture")
    
    st.markdown("---")

    # 2. CHOOSING THE BEST DOCKER IMAGES – table format
    st.header("Choosing the Best Docker Images (Security First!)")
    st.write(
        """
        Your first line of defense against CVEs is picking the right base image. Here's what production teams actually use.
        """
    )
    images_df = pd.DataFrame({
        "Component": ["Streamlit App", "PostgreSQL Database", "Security Scanner"],
        "Recommended Image": ["python:3.12-slim", "postgres:16.4-alpine", "aquasec/trivy"],
        "Why This Choice": [
            "Multi-stage build compatible, ~40% smaller than full Debian, frequent security patches",
            "Official, Alpine-based (~5MB base), zero unnecessary packages",
            "Industry-standard OSS scanner, finds OS + language CVEs"
        ]
    })
    st.dataframe(images_df, use_container_width=True)

    st.warning(
        """
        Always use **official Docker Hub images** and **never use `:latest` tags in production**. Pin exact versions like `postgres:16.4-alpine`.
        """
    )
    st.markdown("---")

    # 3. PROJECT STRUCTURE – expander with code
    st.header(" Sample Project Structure")
    with st.expander("Click to see the complete directory layout", expanded=False):
        st.code(
            """
streamlit-postgres-app/
├── docker-compose.yml          # Multi-container orchestration
├── .env                        # Environment variables (NEVER commit this!)
├── Dockerfile                  # Streamlit app build instructions
├── requirements.txt            # Python dependencies
├── app.py                      # Streamlit application
├── .dockerignore               # Exclude files from build context
├── postgres/
│   └── init/
│       └── 01-init.sql        # Database initialization script
└── .github/
    └── workflows/
        └── docker-publish.yml  # GitHub Actions CI/CD pipeline
            """,
            language="bash"
        )
        st.caption("Copy this structure exactly – it follows Docker best practices.")

    st.markdown("---")

    # 4. STEP-BY-STEP CONFIGURATION – multiple expanders
    st.header(" Step-by-Step Configuration")

    with st.expander(" 1. Create `.dockerignore` (Prevent Credential Leaks)", expanded=False):
        st.write("This prevents accidentally baking secrets into your image.")
        st.code(
            """
.git
.env
*.log
__pycache__
*.pyc
.venv
venv
node_modules
.DS_Store
            """,
            language="dockerignore"
        )

    with st.expander(" 2. Create `.env` File (Never Commit This!)", expanded=False):
        st.code(
            """
# PostgreSQL Configuration
POSTGRES_USER=streamlit_user
POSTGRES_PASSWORD=ChangeMe123!
POSTGRES_DB=streamlit_db

# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
            """,
            language="env"
        )

    with st.expander(" 3. The Dockerfile (Multi-Stage, Non-Root User)", expanded=False):
        st.write("**Key security features:** Multi-stage build, non-root user, health check.")
        st.code(
            """
# Streamlit app Dockerfile
FROM python:3.12-slim AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    libpq-dev \\
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ---- Final Stage ----
FROM python:3.12-slim

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash streamlit
USER streamlit
WORKDIR /home/streamlit/app

# Copy installed packages from builder
COPY --from=builder /root/.local /home/streamlit/.local
ENV PATH=/home/streamlit/.local/bin:$PATH

# Copy application code
COPY --chown=streamlit:streamlit . .

# Expose Streamlit default port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run Streamlit
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
            """,
            language="dockerfile"
        )

    with st.expander(" 4. Sample Streamlit App (`app.py`)", expanded=False):
        st.write("A minimal app that connects to PostgreSQL and displays a table.")
        st.code(
            """
import streamlit as st
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Streamlit + PostgreSQL", layout="wide")
st.title(" Dockerized Streamlit with PostgreSQL")

# Database connection
def get_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres"),
        database=os.getenv("POSTGRES_DB", "streamlit_db"),
        user=os.getenv("POSTGRES_USER", "streamlit_user"),
        password=os.getenv("POSTGRES_PASSWORD", "")
    )

# Query data
@st.cache_data(ttl=60)
def load_data():
    with get_connection() as conn:
        return pd.read_sql("SELECT * FROM users ORDER BY id", conn)

# Display data
st.subheader(" User Data from PostgreSQL")
try:
    df = load_data()
    st.dataframe(df, use_container_width=True)
    st.metric("Total Users", len(df))
except Exception as e:
    st.error(f"Database connection failed: {e}")
    st.info("Ensure PostgreSQL is running and the `users` table exists.")
            """,
            language="python"
        )

    with st.expander(" 5. PostgreSQL Init Script (`postgres/init/01-init.sql`)", expanded=False):
        st.code(
            """
-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO users (name, email) VALUES
    ('Alice Johnson', 'alice@example.com'),
    ('Bob Smith', 'bob@example.com'),
    ('Charlie Brown', 'charlie@example.com')
ON CONFLICT (email) DO NOTHING;
            """,
            language="sql"
        )

    with st.expander(" 6. The Complete `docker-compose.yml`", expanded=True):
        st.write("This is the heart of the setup. Notice the security hardening options.")
        st.code(
            """
version: '3.8'

services:
  postgres:
    image: postgres:16.4-alpine
    container_name: streamlit_postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./postgres/init:/docker-entrypoint-initdb.d:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - app_network
    # Security hardening
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp
      - /var/run/postgresql

  streamlit:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: streamlit_app
    restart: unless-stopped
    ports:
      - "8501:8501"
    environment:
      POSTGRES_HOST: localhost
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - app_network
    # Security hardening
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp

volumes:
  postgres_data:
    name: streamlit_postgres_data

networks:
  app_network:
    driver: bridge
    name: streamlit_network
            """,
            language="yaml"
        )
        st.info(
            """
            **Configuration Highlights:**  
            - `restart: unless-stopped` → Auto-recovery after crashes  
            - `depends_on` with `condition: service_healthy` → Wait for DB to be truly ready  
            - `volumes:` `postgres_data` → Data survives container deletion  
            - `read_only: true` → Prevents attackers from writing to filesystem  
            - `security_opt: no-new-privileges:true` → Blocks privilege escalation
            """
        )

    st.markdown("---")

    # 5. DOCKER COMMANDS REFERENCE – table format
    st.header(" Essential Docker Commands Cheat Sheet")
    st.write("You'll use these daily. Bookmark this section.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Building & Running")
        build_df = pd.DataFrame({
            "Command": [
                "docker build -t myapp:1.0 .",
                "docker run -d -p 8501:8501 --name streamlit myapp:1.0",
                "docker run -v /host/data:/container/data myapp",
                "docker pull postgres:16.4-alpine",
                "docker start streamlit_app",
                "docker stop streamlit_app",
                "docker-compose up -d",
                "docker-compose down -v"
            ],
            "Purpose": [
                "Build image from Dockerfile with tag",
                "Run container detached, map ports",
                "Mount host directory as volume",
                "Download image from registry",
                "Start stopped container",
                "Gracefully stop container",
                "Start all services in compose file",
                "Stop + remove containers, networks, volumes"
            ]
        })
        st.dataframe(build_df, use_container_width=True, hide_index=True)

    with col2:
        st.subheader("Inspection & Management")
        inspect_df = pd.DataFrame({
            "Command": [
                "docker ps",
                "docker ps -a",
                "docker images",
                "docker logs streamlit_app",
                "docker exec -it postgres /bin/bash",
                "docker exec -it postgres /bin/sh",
                "docker network ls",
                "docker network create my_network",
                "docker tag myapp:1.0 myrepo/myapp:1.0",
                "docker rmi myapp:1.0",
                "docker rm streamlit_app"
            ],
            "Purpose": [
                "List running containers",
                "List all containers (including stopped)",
                "List all local images",
                "View container logs",
                "Open bash shell (Debian/Ubuntu containers)",
                "Open sh shell (Alpine containers)",
                "List all Docker networks",
                "Create custom bridge network",
                "Tag image for registry push",
                "Remove image",
                "Remove container"
            ]
        })
        st.dataframe(inspect_df, use_container_width=True, hide_index=True)

    with st.expander(" Advanced Command Examples", expanded=False):
        st.code(
            """
# Run Redis with specific port mapping and name
docker run -d -p 6001:6379 --name redis redis:7.2-alpine

# Filter containers by name
docker ps -a | grep postgres

# Show port mappings of running containers
docker ps --format "table {{.Names}}\\t{{.Ports}}"

# Interactive shell session workflow
docker exec -it streamlit_app /bin/bash
ls -la
pwd
cd /app
env | grep POSTGRES
exit

# View logs with follow
docker logs -f streamlit_app

# Prune unused images/containers/volumes
docker system prune -a --volumes
            """,
            language="bash"
        )

    st.markdown("---")

    # 6. DOCKER NETWORK CONCEPTS
    st.header(" Docker Networking Explained")
    st.write(
        """
        Docker networks enable isolated communication between containers. In our setup, Streamlit connects to PostgreSQL using the service name `postgres` because both share the `app_network` user-defined bridge.
        """
    )
    network_df = pd.DataFrame({
        "Network Type": ["Bridge (Default)", "User-Defined Bridge", "Host", "Overlay"],
        "Use Case": [
            "Legacy `--link` or basic isolation",
            "DNS resolution by service name (what docker-compose creates)",
            "Container shares host's network stack (use cautiously)",
            "Multi-host communication for Swarm/Kubernetes"
        ],
        "Our Setup": ["❌ Not used", "✅ `app_network`", "❌", "❌"]
    })
    st.dataframe(network_df, use_container_width=True)
    st.info(" **Pro tip:** User-defined bridges give you automatic DNS. Your app can just connect to `postgres:5432` – no IP addresses needed.")

    st.markdown("---")

    # 7. CVE SCANNING & SECURITY HARDENING
    st.header(" CVE Scanning & Security Hardening")
    st.write(
        """
        Every Docker image contains OS packages and libraries – each a potential source of known CVEs. 
        Automated scanning prevents vulnerable images from reaching production.
        """
    )

    scanner_df = pd.DataFrame({
        "Tool": ["Trivy", "Docker Scout", "Dockle", "Hadolint"],
        "Type": ["OSS vulnerability scanner", "Native Docker scanner", "Container linter", "Dockerfile linter"],
        "Best For": [
            "Comprehensive CVE detection, CI/CD integration",
            "Integrated with Docker Desktop/CLI",
            "Configuration best-practice validation",
            "Dockerfile syntax and security rules"
        ]
    })
    st.dataframe(scanner_df, use_container_width=True)

    with st.expander(" Run Trivy Locally", expanded=False):
        st.code(
            """
# Install Trivy (macOS)
brew install trivy

# Or via script (Linux)
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh

# Scan a local image
trivy image streamlit-app:latest

# Scan with severity filter (only HIGH and CRITICAL)
trivy image --severity HIGH,CRITICAL streamlit-app:latest

# Scan and output JSON for automation
trivy image --format json --output scan-results.json streamlit-app:latest

# Scan both OS packages and language dependencies
trivy image --scanners vuln,secret,misconfig streamlit-app:latest
            """,
            language="bash"
        )
        st.caption("Output shows CVE IDs, severity, and fixed versions.")

    with st.expander(" 30+ Production Security Checklist", expanded=False):
        st.markdown(
            """
            **Build Time:**
            -  Use trusted base images with pinned version tags
            -  Scan images with Trivy before pushing
            -  Multi-stage builds to reduce size and attack surface
            -  Run as non-root user (`USER 1000`)
            -  Never hardcode credentials in Dockerfile

            **Run Time:**
            -  Drop all capabilities, add only required ones: `--cap-drop=ALL --cap-add=NET_BIND_SERVICE`
            -  Disable privileged mode (never use `--privileged`)
            -  Set resource limits: `--memory=512m --cpus=1 --pids-limit=100`
            -  Use read-only root filesystem with `--read-only`
            -  Apply seccomp/AppArmor profiles
            """
        )

    st.markdown("---")

    # 8. GITHUB ACTIONS – DEPLOY TO GHCR
    st.header(" Deploy to GitHub Container Registry via GitHub Actions")
    st.write(
        """
        This workflow builds, scans, and pushes your image to GHCR on every push to `main`. 
        **The push only happens if Trivy finds zero HIGH/CRITICAL CVEs.**
        """
    )

    with st.expander(" `.github/workflows/docker-publish.yml`", expanded=True):
        st.code(
            """
name: Build, Scan, and Publish Docker Images

on:
  push:
    branches: [ main ]
    tags: [ 'v*' ]
  pull_request:
    branches: [ main ]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
      security-events: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata for Docker
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}
            type=sha,prefix=
            type=raw,value=latest,enable={{is_default_branch}}

      - name: Build Docker image
        id: build
        uses: docker/build-push-action@v5
        with:
          context: .
          load: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ steps.meta.outputs.tags }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'
          exit-code: '1'
          ignore-unfixed: true

      - name: Upload Trivy scan results to GitHub Security tab
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: 'trivy-results.sarif'

      - name: Push Docker image to GHCR
        if: github.event_name != 'pull_request'
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
            """,
            language="yaml"
        )

    st.success(
        """
        **After the workflow succeeds, pull your image:**  
        `docker pull ghcr.io/your-username/streamlit-postgres-app:latest`
        """
    )

    st.markdown("---")

    # 9. MLOPS & UPGRADE CONSIDERATIONS
    st.header(" MLOps Workflow & Upgrading Running Apps")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Zero-Downtime Updates")
        st.code(
            """
# Pull latest image
docker-compose pull streamlit

# Recreate only the Streamlit container
docker-compose up -d --no-deps streamlit
            """,
            language="bash"
        )
    with col2:
        st.subheader("MLOps Considerations")
        st.markdown(
            """
            - **Model Versioning:** Store model artifacts in volumes or S3, not in images
            - **Environment Consistency:** Use identical images across training and inference
            - **GPU Support:** Add `nvidia-docker` runtime and GPU device mappings
            - **Experiment Tracking:** Mount MLflow/W&B config via volumes
            """
        )

    st.markdown("---")

    # 10. TROUBLESHOOTING
    st.header(" Troubleshooting Common Issues")

    issues_df = pd.DataFrame({
        "Issue": [
            "Database connection refused",
            "Container exits immediately",
            "Can't access Streamlit on localhost:8501",
            "Volume data not persisting"
        ],
        "Fix": [
            "`docker exec streamlit_postgres pg_isready -U streamlit_user` → Check DB health. `docker exec streamlit_app ping postgres` → Verify network.",
            "`docker logs streamlit_app` → Check for Python errors or missing dependencies.",
            "Confirm port mapping: `docker ps --format 'table {{.Names}}\\t{{.Ports}}'`. Check firewall.",
            "Verify named volume exists: `docker volume ls`. Use `docker-compose down` (without `-v`) to preserve data."
        ]
    })
    st.dataframe(issues_df, use_container_width=True)

    st.code(
        """
# Reset everything and rebuild
docker-compose down -v
docker-compose up -d --build
        """,
        language="bash"
    )

    st.markdown("---")

    # 11. CHECKLIST
    st.header(" Your Production Deployment Checklist")
    st.markdown(
        """
        **Before pushing to registry:**
        - [ ] `.env` is in `.gitignore` and `.dockerignore`
        - [ ] Base images use pinned version tags (no `:latest`)
        - [ ] Trivy scan returns zero HIGH/CRITICAL CVEs
        - [ ] Dockerfile runs as non-root user
        - [ ] `docker-compose.yml` includes `read_only: true` and `security_opt`

        **Before deploying:**
        - [ ] Named volume is configured for PostgreSQL data
        - [ ] Health checks are defined for both services
        - [ ] Resource limits (memory, CPU) are set
        - [ ] GitHub Actions workflow is configured and passing

        **In production:**
        - [ ] Monitor logs via `docker-compose logs -f`
        - [ ] Set up backup strategy for PostgreSQL volume
        - [ ] Plan for zero-downtime updates using `--no-deps`
        """
    )
    st.success("If you've checked all these boxes, your app is ready for production.")

    st.markdown("---")

    # 12. CONCLUSION
    st.header(" Shipping with Confidence")
    st.write(
        """
        Dockerizing a Streamlit app with PostgreSQL isn't just about making it run – it's about making it **reproducible, secure, and deployable anywhere**. Start with the `docker-compose.yml` in this guide, add your own app logic, and you'll have a production-ready setup in under an hour.

        The security scanning (Trivy) and GitHub Actions pipeline might feel like "extra work" at first, but they pay off the first time they catch a critical CVE before it hits production. Trust me – your future self will thank you.

        **Next actions for you:**  
        1. Copy the project structure and files from this guide.  
        2. Run `docker-compose up -d` and verify you can access `http://localhost:8501`.  
        3. Push to GitHub and watch the Actions workflow build and scan your image.  
        4. Pull your image from GHCR and run it on a different machine – pure magic.

        You've got this. Now go build something awesome – and ship it with confidence. 
        """
    )

    st.markdown("---")

    # 13. EXTERNAL RESOURCES
    st.header(" External Resources")
    st.markdown(
        """
        **Docker & Compose Documentation**  
        - [Docker Compose Overview](https://docs.docker.com/compose/)  
        - [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)  
        - [Docker Security Cheat Sheet (OWASP)](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
        - [Simplifying Multi-Container Development with Docker Compose](https://dev.to/mayankcse/simplifying-multi-container-development-with-docker-compose-4adb)

        **Security Scanning**  
        - [Trivy Documentation](https://aquasecurity.github.io/trivy/)  
        - [Docker Scout](https://docs.docker.com/scout/)  
        - [Dockle](https://github.com/goodwithtech/dockle)

        **GitHub Actions & GHCR**  
        - [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)  
        - [Docker Metadata Action](https://github.com/docker/metadata-action)  
        - [Trivy Action](https://github.com/aquasecurity/trivy-action)

        **Streamlit & PostgreSQL**  
        - [Streamlit Docs: Deploy with Docker](https://docs.streamlit.io/deploy/tutorials/docker)  
        - [PostgreSQL Docker Official Image](https://hub.docker.com/_/postgres)  
        - [psycopg2 Documentation](https://www.psycopg.org/docs/)

        **MLOps & Production Patterns**  
        - [Full Stack Deep Learning: MLOps Course](https://fullstackdeeplearning.com/)  
        - [Made with ML: MLOps Course](https://madewithml.com/)  
        - [DVC (Data Version Control)](https://dvc.org)
        """
    )

    st.markdown("---")
    st.caption("© 2026 | Streamlit + PostgreSQL on Docker | Build secure, production-ready apps.")