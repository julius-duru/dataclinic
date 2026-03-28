import streamlit as st
import pandas as pd

TITLE = "Data Science Toolkit"
CATEGORY = "programming_tools"
KEYWORDS = ["data science", "machine learning", "ML engineering", "Python", "PyTorch", "TensorFlow", "SQL", "data visualization", "MLOps", "deployment", "orchestration", "data pipelines", "Jupyter", "VS Code", "Docker", "FastAPI"]


def show():

    st.title("Data Science Toolkit")
    st.caption("Category: programming_tools | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        The landscape of data science and machine learning is vast and evolves at a breakneck pace. 
        For practitioners, whether you are a data scientist building models or an ML engineer deploying models to production—
        mastering the right tools is not just about efficiency; it is also about feasibility. 
        A well-chosen stack can mean the difference between a model that dies in a Jupyter notebook and one that drives business value for years.
        
        This guide provides a detailed exploration of the modern data science toolkit, categorized by function, 
        and explains how these tools interconnect to form a robust, end-to-end workflow.
        """
    )

    # ============================================
    # SECTION 1: Core Programming Languages
    # ============================================
    st.header("1. Core Programming Languages: The Foundation")
    
    st.write(
        """
        Every project begins with a language. While the ecosystem supports several languages, two dominate Datascience landscape.
        """
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Python")
        st.write(
            """
            Python is the bedrock of machine learning, prized for its simplicity and the depth of its ecosystem.
            
            - **NumPy & Pandas:** The bedrock of data manipulation. NumPy provides efficient array operations, 
              while Pandas offers high-level structures (DataFrames) for cleaning, transforming, and analyzing structured data.
            - **Scikit-learn:** The go-to library for traditional machine learning. It provides a consistent API for 
              preprocessing, model selection, and classical algorithms like random forests and SVMs.
            - **TensorFlow & PyTorch:** The titans of deep learning. PyTorch is favored in research for its dynamic 
              computation graphs, while TensorFlow is often chosen for production-scale deployments.
            """
        )
    
    with col2:
        st.subheader("R & SQL")
        st.write(
            """
            **R:** Excels in statistical analysis and advanced visualization. The **tidyverse** (dplyr, ggplot2) offers 
            a cohesive grammar for data manipulation that is unmatched for exploratory analysis. **caret** and **tidymodels** 
            provide unified interfaces for model training.
            
            **SQL:** The universal language of data. Before a model can be trained, data must be extracted. 
            Whether querying **PostgreSQL** or a data warehouse like **BigQuery**, SQL remains essential for data 
            validation, aggregation, and feature extraction.
            """
        )
    
    st.divider()
    
    # ============================================
    # SECTION 2: Development Environments
    # ============================================
    st.header("2. Development Environments: From Exploration to Production")
    
    st.write(
        """
        The environment you use changes depending on the stage of the project—from initial experimentation to production-ready code.
        """
    )
    
    env_data = {
        "Environment": ["JupyterLab / Notebook", "Google Colab", "VS Code"],
        "Primary Use": [
            "Exploratory Data Analysis (EDA), prototyping, research",
            "Deep learning experimentation with free GPUs/TPUs",
            "Production engineering, scripting, team collaboration"
        ],
        "Key Features": [
            "Interactive cells, markdown integration, multi-language kernels",
            "GitHub integration, preinstalled ML libraries, cloud-based",
            "Extensions (Python, Jupyter, GitLens, Black Formatter), type checking, debugging"
        ]
    }
    df_env = pd.DataFrame(env_data)
    st.dataframe(df_env, use_container_width=True)
    
    st.write(
        """
        **Best Practice:** Start in Jupyter or Colab for exploration and prototyping. As the project matures, 
        migrate to VS Code to enforce code quality, version control, and maintainability.
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 3: Data Storage & Big Data Processing
    # ============================================
    st.header("3. Data Storage & Big Data Processing")
    
    st.write(
        """
        Data rarely sits neatly in a single file. Understanding the data lifecycle and storage options is crucial for scalability.
        """
    )
    
    storage_data = {
        "Category": ["Relational Databases", "Cloud Data Warehouses", "NoSQL", "Big Data Processing", "Orchestration"],
        "Examples": [
            "MySQL, PostgreSQL, SQL Server",
            "BigQuery, Snowflake, Redshift",
            "MongoDB, Cassandra",
            "Apache Spark, Hadoop",
            "Apache Airflow, Prefect"
        ],
        "Use Case": [
            "Transactional data, source of truth",
            "Petabyte-scale analytics, feature stores",
            "Unstructured data, high-throughput reads",
            "Distributed processing for large datasets",
            "Scheduling and monitoring data workflows"
        ]
    }
    df_storage = pd.DataFrame(storage_data)
    st.dataframe(df_storage, use_container_width=True)
    
    st.write(
        """
        **Key Considerations:**
        - **Apache Spark** (via PySpark) is the de facto standard for large-scale data processing, enabling transformations on terabyte-scale datasets.
        - **Airflow / Prefect** orchestrate DAGs (Directed Acyclic Graphs) that automate data extraction, feature computation, and model training—essential for reliable model refreshes.
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 4: Visualization Tools
    # ============================================
    st.header("4. Visualization: Telling the Story")
    
    st.write(
        """
        A model's performance metrics are meaningless if stakeholders cannot understand them. Visualization bridges the gap.
        """
    )
    
    viz_data = {
        "Tool Type": ["Enterprise BI", "Python Libraries", "Interactive Dashboards"],
        "Examples": [
            "Tableau, Power BI, Looker Studio",
            "Matplotlib, Seaborn, Plotly",
            "Streamlit, Dash"
        ],
        "Best For": [
            "Communicating KPIs, model drift, and ROI to business stakeholders",
            "Technical analysis, statistical plots, custom visualizations",
            "Building internal tools, model playgrounds, interactive demos"
        ]
    }
    df_viz = pd.DataFrame(viz_data)
    st.dataframe(df_viz, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # SECTION 5: Machine Learning Libraries
    # ============================================
    st.header("5. Machine Learning Libraries: Beyond the Basics")
    
    st.write(
        """
        Modern ML requires a diverse set of specialized libraries beyond the standard deep learning frameworks.
        """
    )
    
    ml_data = {
        "Library Category": ["Traditional ML", "Deep Learning", "Gradient Boosting", "NLP & Transformers"],
        "Libraries": [
            "Scikit-learn",
            "TensorFlow / Keras, PyTorch",
            "XGBoost, LightGBM",
            "Hugging Face Transformers"
        ],
        "Primary Application": [
            "Preprocessing, model selection, classical algorithms",
            "Neural networks, computer vision, time series",
            "Tabular data, Kaggle competitions, structured problems",
            "Pre-trained models for text, translation, summarization"
        ]
    }
    df_ml = pd.DataFrame(ml_data)
    st.dataframe(df_ml, use_container_width=True)
    
    st.write(
        """
        **Pro Tip:** For tabular data, XGBoost and LightGBM often outperform deep learning models. 
        For NLP, Hugging Face Transformers provides thousands of pre-trained models with a unified API, 
        drastically reducing time to implementation.
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 6: Deployment & MLOps
    # ============================================
    st.header("6. Deployment & MLOps: The Last Mile")
    
    st.write(
        """
        The hardest part of machine learning is often deployment. This is where ML engineers distinguish themselves.
        """
    )
    
    deploy_data = {
        "Component": ["Version Control", "API Frameworks", "Interactive Apps", "Containerization", "Cloud Platforms"],
        "Tools": [
            "Git, GitHub, DVC (Data Version Control)",
            "FastAPI, Flask",
            "Streamlit",
            "Docker",
            "AWS (SageMaker), Azure ML, GCP Vertex AI"
        ],
        "Purpose": [
            "Code and data versioning, collaboration",
            "Serving model inferences via REST APIs",
            "Internal demos, model playgrounds",
            "Environment consistency, immutable artifacts",
            "Managed training, hosting, monitoring"
        ]
    }
    df_deploy = pd.DataFrame(deploy_data)
    st.dataframe(df_deploy, use_container_width=True)
    
    st.write(
        """
        **Best Practice:** 
        - Wrap models in **FastAPI** for automatic OpenAPI documentation and async support.
        - Use **Docker** to containerize models, ensuring consistency across development, staging, and production.
        - Leverage cloud ML platforms for autoscaling, model monitoring, and lifecycle management.
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 7: Putting It All Together
    # ============================================
    st.header("7. Putting It All Together: End-to-End Workflow")
    
    st.write(
        """
        A mature ML workflow integrates these tools into a cohesive pipeline:
        
        | Stage | Tools | Description |
        |-------|-------|-------------|
        | **1. Data Extraction** | SQL, APIs, Kafka | Pull data from transactional DBs, event streams, and external sources |
        | **2. Data Transformation** | Pandas, Spark, dbt | Clean, aggregate, and engineer features at scale |
        | **3. Experimentation** | Jupyter, Colab, PyTorch | Prototype models interactively, track experiments |
        | **4. Model Development** | Scikit-learn, XGBoost, Hugging Face | Train and validate models using specialized libraries |
        | **5. Version Control** | Git, DVC | Track code, data, and model versions together |
        | **6. Orchestration** | Airflow, Prefect | Schedule retraining, manage dependencies |
        | **7. Deployment** | FastAPI, Docker, AWS | Serve models via APIs, containerize, deploy to cloud |
        | **8. Monitoring** | Evidently, Prometheus, Grafana | Track model drift, performance, and data quality |
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 8: Best Practices
    # ============================================
    st.header("Best Practices for Modern ML Engineers & Data Scientists")
    
    st.markdown(
        """
        **1. Version Everything**
        - Version code with Git, data with DVC or LakeFS, and models with MLflow.
        - Reproducibility depends on knowing exactly which data and code produced a given model.
        
        **2. Automate the Pipeline**
        - Use orchestration tools (Airflow, Prefect) to schedule retraining and data updates.
        - Implement CI/CD for models to streamline deployment.
        
        **3. Monitor Continuously**
        - Track data drift, concept drift, and model performance post-deployment.
        - Set up alerts for data quality issues and pipeline failures.
        
        **4. Design for Scalability**
        - Use columnar formats (Parquet) for analytical workloads.
        - Implement incremental processing to avoid full data reloads.
        
        **5. Maintain Documentation**
        - Document data lineage, transformation logic, and model assumptions.
        - Keep a shared data dictionary accessible to all team members.
        
        **6. Think in Stages**
        - Use notebooks for exploration, scripts for production.
        - Refactor early to avoid technical debt.
        """
    )
    
    st.divider()
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")
    
    st.write(
        """
        The tools outlined in this guide represent the distinct phases of the machine learning lifecycle. 
        A modern data scientist or ML engineer must be a polyglot—fluent in the **SQL** used to extract data, 
        the **Python** used to train a model, the **Docker** used to containerize it, and the **FastAPI** used to serve it.
        
        Mastering this stack allows practitioners to move fluidly from exploratory analysis in **Jupyter** 
        to robust, scalable pipelines orchestrated by **Airflow** and deployed on **AWS**. 
        By understanding not just *how* to use these tools, but *when* and *why* to use them, 
        you can build systems that are not only accurate but also resilient, scalable, and ready for production.
        
        In the world of machine learning, your tools shape what you can build. Choose them wisely, 
        and invest in learning how they fit together—because the most powerful models are useless without 
        the infrastructure to deliver them reliably.
        """
    )
    
    st.divider()
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Official Documentation & Learning:**
        - **Python Data Science:** [Real Python](https://realpython.com/), [Pandas Docs](https://pandas.pydata.org/docs/)
        - **Machine Learning:** [Scikit-learn Docs](https://scikit-learn.org/stable/), [PyTorch Tutorials](https://pytorch.org/tutorials/), [TensorFlow Learn](https://www.tensorflow.org/learn)
        - **MLOps & Deployment:** [FastAPI Docs](https://fastapi.tiangolo.com/), [Docker Curriculum](https://docker-curriculum.com/)
        
        **Courses & Guides:**
        - [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
        - [fast.ai](https://www.fast.ai/)
        - [DeepLearning.AI](https://www.deeplearning.ai/courses/)
        - [Hugging Face Courses](https://huggingface.co/learn)
        
        """
    )