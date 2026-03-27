import streamlit as st
import pandas as pd

TITLE = "Building Data Pipelines for Machine Learning"
CATEGORY = "machine_learning"
KEYWORDS = ["data pipelines", "ETL", "ELT", "machine learning", "MLOps", "data orchestration", "data observability", "feature engineering", "Apache Airflow", "data warehouse","data lakes"]


def show():

    st.title("Building Data Pipelines for Machine Learning")
    st.caption("Category: machine_learning | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        Machine learning (ML) systems rely heavily on the quality, consistency, and availability of data. 
        Behind every successful ML model is a well-designed data pipeline—a set of processes that automatically 
        collects, transforms, stores, and orchestrates data so it can be used efficiently for training and inference.
        
        This guide provides a comprehensive overview of building robust data pipelines for machine learning, 
        covering ETL/ELT workflows, data transformation, pipeline orchestration, tools, and observability.
        """
    )

    # ============================================
    # SECTION 1: What Is a Data Pipeline for ML?
    # ============================================
    st.header("1.  Data Pipeline for Machine Learning?")
    
    st.write(
        """
        A data pipeline is an automated system that moves data from source systems to storage and ultimately to ML workloads. 
        A well-architected pipeline typically consists of the following stages:
        
        - **Extraction:** Ingesting data from various source systems
        - **Transformation:** Converting raw data into machine-learning-ready formats
        - **Loading:** Storing processed data in a target system (data warehouse, data lake, database, or feature store)
        - **Orchestration:** Automating and scheduling workflows to ensure smooth execution
        - **Monitoring & Observability:** Tracking pipeline health, data quality, and reliability
        
        Given the demands of modern ML, these pipelines must be designed to handle high-volume, high-velocity, 
        and high-variety data while maintaining consistency, scalability, and correctness.
        """
    )
    
    st.divider()

    # ============================================
    # SECTION 2: ETL vs ELT
    # ============================================
    st.header("2. ETL vs. ELT for Machine Learning Pipelines")
    
    st.write(
        """
        Choosing between ETL and ELT is a foundational architectural decision that impacts flexibility, 
        scalability, and performance.
        """
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("ETL")
        st.write(
            """
            **Extract → Transform → Load**
            
            In this model, data is transformed before it is loaded into the target system.
            
            **Flow:** Trigger → Extract → Transform → Load
            
            **Target Systems:**
            - Relational databases
            - Traditional data warehouses (MySQL, PostgreSQL, Snowflake)
            
            **Best For:**
            - Workloads requiring structured, analytics-ready data
            - Business dashboards and low-latency queries
            """
        )
    
    with col2:
        st.subheader("ELT")
        st.write(
            """
            **Extract → Load → Transform**
            
            This approach ingests raw data first and applies transformations later, leveraging the compute 
            power of the target system.
            
            **Target Systems:**
            - Data lakes (AWS S3, Google Cloud Storage)
            - Lakehouses (Databricks, Apache Iceberg)
            - Modern cloud warehouses (BigQuery, Snowflake)
            
            **Best For:**
            - ML, AI, and deep learning workloads
            - Access to raw, unstructured data (audio, text, logs, images)
            - Maximum flexibility
            """
        )
    
    st.divider()
    
    # ============================================
    # SECTION 3: Step-by-Step Pipeline Building
    # ============================================
    st.header("3. Step-by-Step: Building the ML Data Pipeline")
    
    # Step 1: Extract
    st.subheader("Step 1: EXTRACT — Gathering Data from Diverse Sources")
    st.write(
        """
        ML systems often rely on a wide array of data sources. Extraction mechanisms must support both 
        batch and real-time ingestion.
        """
    )
    
    extract_data = {
        "Data Source Type": ["Lead Data", "Sales Data", "Social Data", "Web Data", "File Systems", "Sensor Data", "Application Logs"],
        "Examples": [
            "HubSpot, Salesforce, CRM platforms",
            "Transaction logs, payment systems, POS data",
            "APIs from Facebook, Twitter, LinkedIn",
            "Custom scrapers, public datasets, blogs",
            "PDFs, Excel files, text documents",
            "IoT devices, telemetry logs, machine sensors",
            "Server logs, clickstream events, user activity"
        ]
    }
    df_extract = pd.DataFrame(extract_data)
    st.dataframe(df_extract, use_container_width=True)
    
    st.write(
        """
        **Key Considerations:**
        - Managing API rate limits
        - Adhering to legal and compliance requirements (`robots.txt`)
        - Ensuring timestamp alignment across sources
        - Handling both streaming and batch data sources
        """
    )
    
    # Step 2: Transform
    st.subheader("Step 2: TRANSFORM — Preparing Data for Machine Learning")
    st.write(
        """
        Transformation is the most critical stage, where raw, heterogeneous data is converted into clean, 
        structured, and feature-rich datasets suitable for model training.
        
        **Typical Transformation Activities:**
        
        - **Processing Semi-Structured Data:** Inferring schemas and flattening nested structures from JSON, XML, or log files
        - **Handling Unstructured Data:** Converting audio to spectrograms, text to tokens or embeddings, images to normalized tensors
        - **Data Cleaning:** Deduplication, handling missing values, correcting data types, detecting outliers
        - **Feature Engineering:** Creating aggregated metrics, windowed statistics, encoded categorical variables
        - **Validation:** Using frameworks like **Great Expectations** or **TensorFlow Data Validation (TFDV)** to enforce data quality checks
        """
    )
    
    # Step 3: Load
    st.subheader("Step 3: LOAD — Storing Data for Training and Inference")
    st.write(
        """
        The choice of storage system dictates the speed and efficiency with which ML teams can access and use data.
        """
    )
    
    load_data = {
        "Storage Type": ["Object Storage", "Databases", "Data Warehouses", "Data Lakes / Lakehouses"],
        "Examples": [
            "AWS S3, Azure Blob Storage, Google Cloud Storage",
            "PostgreSQL, MySQL, MongoDB, DynamoDB",
            "Snowflake, BigQuery, Redshift",
            "Databricks, Delta Lake, Apache Iceberg, Apache Hudi"
        ],
        "Best For": [
            "Raw files, versioned datasets, unstructured data",
            "Application-level data for inference systems",
            "Aggregated datasets, analytical queries, dashboards",
            "Large-scale ML workloads, batch + streaming pipelines, deep learning"
        ]
    }
    df_load = pd.DataFrame(load_data)
    st.dataframe(df_load, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # SECTION 4: Orchestration
    # ============================================
    st.header("4. Orchestration in ML Data Pipelines")
    
    st.write(
        """
        Orchestration tools automate workflow execution, manage dependencies, and handle scheduling, retries, and logging. 
        A modern ML pipeline requires support for scheduled batch jobs, real-time streams, and trigger-based workflows.
        """
    )
    
    orchestration_data = {
        "Category": ["Workflow Orchestration", "Cloud-Native Orchestration", "Streaming Pipelines", "ML-Specific Orchestration"],
        "Tools": [
            "Apache Airflow, Prefect, Dagster",
            "AWS Step Functions, GCP Cloud Composer, Azure Data Factory",
            "Apache Kafka, Apache Flink, Spark Structured Streaming",
            "Kubeflow Pipelines, MLflow, TensorFlow Extended (TFX)"
        ]
    }
    df_orchestration = pd.DataFrame(orchestration_data)
    st.dataframe(df_orchestration, use_container_width=True)
    
    st.write(
        """
        Effective orchestration ensures pipeline reliability and enables automated retraining cycles by integrating 
        seamlessly with ML platforms.
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 5: Observability
    # ============================================
    st.header("5. Observability: Ensuring Pipeline Health")
    
    st.write(
        """
        Observability is crucial for maintaining data correctness, pipeline performance, and prediction stability 
        throughout the ML lifecycle.
        """
    )
    
    st.subheader("Core Components of Observability")
    
    obs_data = {
        "Component": ["Data Quality Monitoring", "Pipeline Performance Monitoring", "Model & Data Drift Monitoring"],
        "What It Detects": [
            "Schema drift, missing data, outliers, statistical distribution shifts",
            "Throughput, latency, error rates, compute resource usage",
            "Input data drift and model concept drift after deployment"
        ],
        "Tools": [
            "Great Expectations, Monte Carlo, Soda Data, TFDV",
            "Prometheus, Grafana, OpenTelemetry",
            "Evidently AI, WhyLabs, Fiddler AI"
        ]
    }
    df_obs = pd.DataFrame(obs_data)
    st.dataframe(df_obs, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # SECTION 6: Putting It All Together
    # ============================================
    st.header("6. Putting It All Together: A Typical ML Data Pipeline Architecture")
    
    st.write(
        """
        A mature ML data pipeline often follows a structured flow:
        
        | Stage | Description |
        |-------|-------------|
        | **1. Extract** | Ingest data from diverse sources—APIs, databases, logs, sensors, and file systems |
        | **2. Load (ELT)** | Raw data is loaded into a scalable data lake or object storage |
        | **3. Transform** | Using processing engines like Apache Spark, Databricks, or Snowflake to clean, validate, and engineer features |
        | **4. Store** | Curated datasets are loaded into a data warehouse, feature store, or lakehouse for consumption |
        | **5. Orchestrate** | Workflow tools like Airflow or Prefect schedule and manage transformations, triggering downstream processes |
        | **6. Monitor** | Implement observability to track data quality, pipeline performance, and drift |
        | **7. Utilize** | Provide clean, reliable data for model training, batch inference, and real-time serving |
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 7: Comparison Summary
    # ============================================
    st.header("Summary: ETL vs. ELT at a Glance")
    
    summary_data = {
        "Aspect": ["Approach", "Transformation Timing", "Target Systems", "Best For", "Flexibility", "Raw Data Access"],
        "ETL": [
            "Extract → Transform → Load",
            "Before loading",
            "Data warehouses, relational databases",
            "Analytics dashboards, structured reporting",
            "Lower—schema defined upfront",
            "Limited—only transformed data stored"
        ],
        "ELT": [
            "Extract → Load → Transform",
            "After loading (in target system)",
            "Data lakes, lakehouses, cloud warehouses",
            "ML/AI workloads, unstructured data",
            "Higher—raw data preserved for flexibility",
            "Full—raw data available for exploration"
        ]
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # SECTION 8: Best Practices
    # ============================================
    st.header("Best Practices for Building ML Data Pipelines")
    
    st.markdown(
        """
        **1. Design for Scalability**
        - Use columnar storage formats (Parquet, ORC) for analytical workloads
        - Partition data by time or key dimensions to optimize query performance
        - Implement incremental processing to avoid full data reloads
        
        **2. Implement Idempotency**
        - Ensure pipeline stages can be safely re-run without creating duplicates
        - Use upsert patterns (merge operations) for incremental updates
        
        **3. Automate Data Validation**
        - Integrate data quality checks at every stage
        - Set up alerts for schema changes, null value spikes, and distribution shifts
        
        **4. Version Everything**
        - Version your datasets alongside your models
        - Use tools like DVC or LakeFS for data versioning
        
        **5. Monitor Beyond Infrastructure**
        - Track data freshness, completeness, and accuracy
        - Set up SLA-based alerts for pipeline delays
        
        **6. Document Your Pipelines**
        - Maintain data lineage to understand dependencies
        - Document transformation logic and business rules
        - Keep a data dictionary accessible to all team members
        """
    )
    
    st.divider()
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")
    
    st.write(
        """
        A robust data pipeline is not merely a supporting component but the backbone of any successful 
        machine learning system. Effective pipelines deliver:
        
        - **Clean, consistent, and scalable datasets** that fuel accurate models
        - **Automated and repeatable workflows** for reliable retraining
        - **Comprehensive observability** to catch issues before they impact production
        - **Fast access to data** for both training and inference workloads
        
        Whether you adopt an ETL or ELT architecture, choose databases or data lakes, or select specific 
        orchestration and monitoring tools, the core objective remains constant: **to deliver the right data, 
        to the right place, at the right time**—ready to power impactful machine learning applications.
        
        As ML systems grow in complexity, investing in your data pipeline infrastructure is one of the highest-ROI 
        decisions you can make. Because in the world of machine learning, you're only as good as the data you feed it.
        """
    )
    
    st.divider()
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Tools Mentioned in This Guide:**
        - **Orchestration:** [Apache Airflow](https://airflow.apache.org/), [Prefect](https://www.prefect.io/), [Dagster](https://dagster.io/)
        - **Streaming:** [Apache Kafka](https://kafka.apache.org/), [Apache Flink](https://flink.apache.org/)
        - **Storage:** [Delta Lake](https://delta.io/), [Apache Iceberg](https://iceberg.apache.org/), [Apache Hudi](https://hudi.apache.org/)
        - **Validation:** [Great Expectations](https://greatexpectations.io/), [Soda](https://www.soda.io/)
        - **Observability:** [Evidently AI](https://evidentlyai.com/)
        
        **Further Reading:**
        - [MLOps: Continuous Delivery for Machine Learning](https://ml-ops.org/)
        - [The Data Engineering Cookbook](https://github.com/andkret/Cookbook)
        """
    )
