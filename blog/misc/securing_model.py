import streamlit as st
import pandas as pd

TITLE = "Securing MLOps Models in Staging & Production"
CATEGORY = "misc"
KEYWORDS = [
    "MLSecOps", "model security", "staging environment", "production security",
    "data poisoning", "adversarial attacks", "model drift", "access control",
    "CI/CD security", "model registry", "MLflow", "FastAPI", "Prometheus",
    "NIST AI", "OWASP LLM", "MITRE ATLAS"
]

def show():
    st.title(TITLE)
    st.caption("Category: MISC | Level: Beginner → Advanced | A friendly, practical guide")
    st.markdown("---")

    # INTRODUCTION
    st.write(
        """
        Securing machine learning models can feel overwhelming – but it doesn’t have to be. Whether you are a data scientist shipping your first model or an MLOps engineer managing hundreds ofmodels,  
        the core idea is **defense in layers**. Think of it like securing a house: you lock the doors (access control), install cameras (monitoring), and maybe get a dog (anomaly detection).

        This guide walks you through **10 concrete steps** to secure your MLOps pipelines –  from data ingestion to production monitoring with practical tools.
        """
    )

    st.divider()

    # ============================================
    # SECTION 1: Secure Data Pipelines
    # ============================================
    st.header(" 1. Secure Data Pipelines First")
    st.write(
        """
        Your model is only as secure as the data feeding it. If an attacker can poison or spy on your data,  
        everything else is pointless.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Encrypt data at rest and in transit** – Use TLS (HTTPS) for pipelines, encrypt S3 buckets or databases.
        - **Validate and sanitise every input** – Prevent data poisoning and injection attacks.  
          Tools like **Great Expectations** automatically check schemas (e.g., “this column should never be null”).
        - **Enforce strict access control** – Use least‑privilege IAM roles. Keep staging datasets completely separate from production.
        """
    )
    st.code(
        """
# Example: Great Expectations validation in a pipeline
import great_expectations as ge

df = ge.read_csv("s3://raw/transactions.csv")
expectation = df.expect_column_values_to_not_be_null("amount")
if not expectation["success"]:
    raise ValueError("Data poisoning detected: null values in 'amount'")
        """,
        language="python"
    )
    st.info(" **Beginner take:** Treat your data like a chef treats ingredients – if the tomatoes are rotten, the whole dish is ruined.  \n🔧 **Pro tip:** Automate data validation as part of your pipeline. If a schema check fails, fail the pipeline immediately.")

    st.divider()

    # ============================================
    # SECTION 2: Lock Down Training & Experimentation
    # ============================================
    st.header(" 2. Lock Down the Training & Experimentation Environment")
    st.write(
        """
        Staging is where most vulnerabilities creep in – old libraries, open notebooks, shared credentials.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Isolate environments** – Separate dev, staging, and production networks. Use containers (Docker) and orchestration (Kubernetes).
        - **Manage dependency security** – Pin package versions. Scan for vulnerabilities with **Snyk** or **Trivy**.
        - **Ensure reproducibility** – Version datasets, code, and models. **MLflow** and **DVC** are your friends.
        """
    )
    st.code(
        """
# Pin dependencies and scan
$ pip freeze > requirements.lock
$ trivy fs --severity HIGH,CRITICAL .
        """,
        language="bash"
    )
    st.info(" **Beginner take:** Staging is your kitchen prep area – don’t leave raw chicken next to salad.  \n🔧 **Pro tip:** Use `requirements.lock` and run vulnerability scans in your CI pipeline. Block deployment if a critical CVE appears.")

    st.divider()

    # ============================================
    # SECTION 3: Secure Model Artifacts
    # ============================================
    st.header(" 3. Secure Model Artifacts")
    st.write(
        """
        Once trained, your model is a valuable asset – treat it like a signed binary, not a random file.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Digitally sign model artifacts** before deployment. This guarantees integrity.
        - **Store models in a secure registry** (private model registry, not a public bucket). Restrict permissions.
        - **Perform integrity checks** – Always hash‑verify the model before loading it into memory.
        """
    )
    st.code(
        """
# Model signing example (using openssl)
openssl dgst -sha256 -sign private_key.pem -out model.sig model.pkl
# Verification
openssl dgst -sha256 -verify public_key.pem -signature model.sig model.pkl
        """,
        language="bash"
    )
    st.info(" **Beginner take:** Think of signing a model like a tamper‑evident seal on a medicine bottle.  \n🔧 **Pro tip:** Integrate model signing into your CI/CD. Fail the pipeline if the signature is missing or mismatched.")

    st.divider()

    # ============================================
    # SECTION 4: Strong Access Control
    # ============================================
    st.header(" 4. Implement Strong Access Control")
    st.write(
        """
        Who can deploy or query your model? Access control is the lock on your front door.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Authentication & authorisation** – Use OAuth2 or API keys. Enforce **RBAC** (Role‑Based Access Control).
        - **Secrets management** – Store credentials in **HashiCorp Vault**, **AWS Secrets Manager**, or similar.  
          *Never* hardcode secrets in code or notebooks.
        """
    )
    st.code(
        """
# Example: Fetch secret from Vault (Python)
import hvac
client = hvac.Client(url='http://vault:8200', token=os.environ['VAULT_TOKEN'])
secret = client.secrets.kv.v2.read_secret_version(path='mlflow_db')
db_password = secret['data']['data']['password']
        """,
        language="python"
    )
    st.info(" **Beginner take:** Don’t share your house keys with the mailman.  \n🔧 **Pro tip:** Use short‑lived tokens and rotate secrets automatically. Audit access logs weekly.")

    st.divider()

    # ============================================
    # SECTION 5: Secure Model Serving Endpoints
    # ============================================
    st.header("5. Secure Model Serving Endpoints")
    st.write(
        """
        Your model endpoint is now public‑facing (or internal but exposed). Attackers will probe it.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **API gateway protection** – Rate limiting to prevent abuse. Add a Web Application Firewall (WAF).
        - **Input/output filtering** – Detect adversarial inputs. Limit output exposure – don’t return internal confidence scores unless needed.
        - **Network isolation** – Use VPCs and private endpoints whenever possible.
        """
    )
    st.code(
        """
# FastAPI rate limiting with slow api
from slowapi import Limiter, _rate_limit_exceeded_handler
limiter = Limiter(key_func=get_remote_address)

@app.post("/predict")
@limiter.limit("100/minute")
def predict(request: Request, features: dict):
    ...
        """,
        language="python"
    )
    st.info(" **Beginner take:** Your endpoint is like a shop window – you want people to look, but not throw bricks.  \n🔧 **Pro tip:** Use **Adversarial Robustness Toolbox (ART)** to test your model’s resilience before deployment.")

    st.divider()

    # ============================================
    # SECTION 6: Monitor for Threats and Drift
    # ============================================
    st.header("6. Monitor for Threats and Drift")
    st.write(
        """
        Once in production, you need eyes on it 24/7. Security is ongoing, not a one‑time checkbox.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Logging & auditing** – Track every request and prediction. Log who accessed the model.
        - **Anomaly detection** – Monitor for unusual traffic patterns (e.g., 10,000 rapid requests from one IP – could be model extraction).
        - **Model drift monitoring** – Watch for unexpected performance shifts. Drift can be natural, but it can also signal an attack.
        """
    )
    st.code(
        """
# Drift detection with evidently
from evidently.report import Report
from evidently.metrics import DatasetDriftMetric

report = Report(metrics=[DatasetDriftMetric()])
report.run(reference_data=training_data, current_data=recent_data)
drift_score = report.as_dict()['metrics'][0]['result']['dataset_drift']
# Send drift_score to Prometheus
        """,
        language="python"
    )
    st.info(" **Beginner take:** It’s like a baby monitor for your model – you don’t stare all day, but you want to hear a cry.  \n **Pro tip:** Set up alerts for both statistical drift (e.g., PSI > 0.2) and security anomalies (e.g., request rate > 3σ from baseline).")

    st.divider()

    # ============================================
    # SECTION 7: Secure CI/CD Pipelines
    # ============================================
    st.header("7. Secure CI/CD Pipelines (MLOps Pipelines)")
    st.write(
        """
        Your automated pipeline – the thing that trains and deploys models – can be hijacked if you’re not careful.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Pipeline integrity** – Sign and verify each pipeline step. Restrict who can trigger deployments.
        - **Automated security checks** – Static code analysis (e.g., **Bandit** for Python). Dependency vulnerability scans.
        - **Approval gates** – Require manual approval for production releases for high‑risk models.
        """
    )
    st.code(
        """
# .gitlab-ci.yml snippet
stages: [test, build, deploy-staging, deploy-prod]

test:
  script:
    - bandit -r src/                  # static analysis
    - safety check -r requirements.txt  # dependency scan
deploy-prod:
  stage: deploy-prod
  when: manual                       # approval gate
        """,
        language="yaml"
    )
    st.info("**Beginner take:** Your CI/CD pipeline is like an automated factory – you want quality control at every station.  \n🔧 **Pro tip:** Use **policy as code** (e.g., Open Policy Agent) to enforce rules like “no model with a critical CVE can reach production”.")

    st.divider()

    # ============================================
    # SECTION 8: Harden Infrastructure
    # ============================================
    st.header("8. Harden Infrastructure")
    st.write(
        """
        Infrastructure misconfigurations – open ports, outdated containers – are how most breaches happen.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Use Infrastructure as Code (IaC)** – Terraform, CloudFormation, Pulumi. Define security policies alongside resources.
        - **Patch management** – Keep OS, containers, and libraries updated. Automate patch scanning.
        - **Container security** – Run containers as non‑root. Use minimal base images (e.g., Alpine).
        """
    )
    st.code(
        """
# Dockerfile – run as non‑root
FROM python:3.10-slim
RUN useradd -m -u 1000 appuser
USER appuser
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
        """,
        language="dockerfile"
    )
    st.info("**Beginner take:** Infrastructure is the foundation of your house – if it’s cracked, the whole thing leans.  \n🔧 **Pro tip:** Scan container images with **Trivy** or **Clair** in your CI pipeline. Block any image with a high‑severity vulnerability.")

    st.divider()

    # ============================================
    # SECTION 9: ML‑Specific Attack Defenses
    # ============================================
    st.header("9. Protect Against ML‑Specific Attacks")
    st.write(
        """
        Traditional security isn’t enough – we need to defend against adversarial ML, model extraction, and membership inference.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Adversarial attack defenses** – Preprocess inputs (e.g., feature squeezing). Test robustness with **Adversarial Robustness Toolbox**.
        - **Model extraction prevention** – Limit query rates per user. Add slight noise to outputs if you suspect scraping.
        - **Membership inference protection** – Use **differential privacy** techniques (e.g., TensorFlow Privacy).
        """
    )
    st.code(
        """
# Differential privacy training with TensorFlow Privacy
from tensorflow_privacy import DPKerasSGDOptimizer
optimizer = DPKerasSGDOptimizer(
    l2_norm_clip=1.0,
    noise_multiplier=0.5,
    num_microbatches=1,
    learning_rate=0.15
)
model.compile(optimizer=optimizer, loss='categorical_crossentropy')
        """,
        language="python"
    )
    st.info("**Beginner take:** Some attackers don’t break in – they just ask your model cleverly crafted questions to steal its secrets.  \n🔧 **Pro tip:** Libraries like **TensorFlow Privacy** and **IBM Adversarial Robustness Toolbox** help you implement these defenses without starting from scratch.")

    st.divider()

    # ============================================
    # SECTION 10: Governance, Compliance, Auditing
    # ============================================
    st.header(" 10. Governance, Compliance, and Auditing")
    st.write(
        """
        Especially if you are in healthcare, finance, or handling personal data, you need to prove you are secure.
        """
    )
    st.subheader("What to do")
    st.markdown(
        """
        - **Audit trails** – Track every model version, every deployment, every change.
        - **Compliance** – Map controls to regulations (GDPR, HIPAA, SOC2).
        - **Documentation** – Maintain **model cards** and **risk assessments**.
        """
    )
    st.code(
        """
# Example: Automatically generate a model card (pseudo)
model_card = {
    "model_name": "FraudDetector v2",
    "training_data": "transactions_2024_03 (hashed)",
    "metrics": {"accuracy": 0.98, "f1": 0.95},
    "intended_use": "Real‑time fraud detection for e‑commerce",
    "limitations": "May degrade if transaction volume changes drastically",
    "security_controls": ["signed artifact", "RBAC", "drift monitoring"]
}
        """,
        language="python"
    )
    st.info("**Beginner take:** Documentation sounds boring until an auditor asks for it at 4 PM on a Friday.  \n🔧 **Pro tip:** Automate model card generation as part of your pipeline – use **MLflow** or **SageMaker Model Cards**.")

    st.divider()

    # ============================================
    # Staging vs Production Cheat Sheet
    # ============================================
    st.header(" Staging vs. Production – Quick Cheat Sheet")
    staging_prod_df = pd.DataFrame({
        "Area": ["Data", "Access", "Monitoring", "Security controls"],
        "Staging": ["Masked / anonymised", "Broader (devs, testers)", "Basic – correctness only", "Moderate – focus on preventing mistakes"],
        "Production": ["Real, sensitive data", "Strict, limited (service accounts + on‑call)", "Advanced + alerting (24/7)", "Maximum – assume attackers are probing"]
    })
    st.dataframe(staging_prod_df, use_container_width=True)
    st.caption("**Key takeaway:** What’s okay in staging (e.g., open notebooks, broad access) is never okay in production.")

    st.divider()

    # ============================================
    # CYBER RESILIENCE STANDARDS
    # ============================================
    st.header("Cyber Resilience Standards and Frameworks")
    standards_df = pd.DataFrame({
        "Standard": [
            "NIST AI Profile (IR 8596)",
            "ETSI EN 304 223",
            "ISO/IEC 27001 + 42001",
            "OWASP Top 10 for LLMs (2025)",
            "MITRE ATLAS"
        ],
        "Use case": [
            "Securing AI systems, using AI for defence, defending against AI attacks",
            "First European standard – 13 principles across AI lifecycle",
            "Traditional ISMS + AI management system",
            "Specific risks for LLMs (prompt injection, data leakage, etc.)",
            "Adversarial threat framework for ML"
        ],
        "Why You Care": [
            "Best all‑round guide – maps to popular NIST CSF",
            "Required for EU clients; great for structured compliance",
            "When you need certification – use 27001 for general security, 42001 for AI",
            "Mandatory reading if you work with LLMs or GenAI",
            "Great for threat modeling – think 'MITRE ATT&CK for ML'"
        ]
    })
    st.dataframe(standards_df, use_container_width=True)
    st.info("**Procedural tip:** Start with a threat model (MITRE ATLAS). Then pick one framework (NIST AI Profile is a solid default). Implement controls in stages – don’t boil the ocean.")

    st.divider()

    # ============================================
    # RESOURCES
    # ============================================
    st.header(" Curated Resources – Tools & Learning")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Frameworks & official docs**")
        st.markdown(
            """
            - [OWASP Top 10 for LLMs](https://genai.owasp.org)
            - [MITRE ATLAS](https://atlas.mitre.org)
            """
        )
        st.markdown("**Tools**")
        st.markdown(
            """
            - **Data validation:** Great Expectations, Pydantic
            - **Dependency scanning:** Snyk, Trivy, Safety
            - **Model registry:** MLflow, DVC, Hugging Face Hub (private repos)
            - **Adversarial robustness:** ART, Foolbox, CleverHans
            - **Differential privacy:** TensorFlow Privacy, OpenDP
            - **Policy as code:** Open Policy Agent (OPA)
            """
        )
    with col2:
        st.markdown("**Free learning**")
        st.markdown(
            """
            - [Building AI Security In- MLSecOps in Practice](https://www.youtube.com/watch?v=byWL54oyDgI) – MLSecOps.
            """
        )
        st.markdown("**Communities**")
        st.markdown(
            """
            - OpenSSF AI/ML Security Working Group
            - Cloud Security Alliance (CSA) AI Security Initiative
            """
        )

    st.divider()

    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Final Thought")
    st.write(
        """
        You don’t need to implement all ten steps on day one.  

        - **If you’re new:** Pick steps 1 (secure data), 4 (access control), and 6 (monitoring).  
          That alone will put you ahead of 80% of teams.  

        - **If you’re advanced:** Automate steps 2, 3, and 7 into your CI/CD.  
          Add step 9 (ML‑specific defenses) for high‑value models.  

        Security is a journey, not a destination. And now you’ve got a map. **
        """
    )

    st.divider()
    st.caption(f" Article: {TITLE} | Category: {CATEGORY} | Level: Beginner → Advanced")
