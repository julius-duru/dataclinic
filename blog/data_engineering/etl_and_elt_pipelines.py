import streamlit as st
import pandas as pd

TITLE = "Data Pipeline Patterns: Trade-offs, Use Cases & Business Impact by Vertical"
CATEGORY = "data_engineering"
KEYWORDS = [
    "data pipelines", "ETL", "ELT", "streaming", "lambda architecture",
    "batch processing", "real-time", "data engineering", "business impact"
]

def show():
    st.title(TITLE)
    st.caption("Category: Data Engineering | Level: Intermediate → Advanced | 4 pipeline patterns explained")
    st.markdown("---")

    # INTRODUCTION
    st.write(
        """
        Data pipelines are the arteries of modern organizations. Choosing the wrong pattern can lead to high costs, stale insights, or brittle architectures.
        This guide covers the four fundamental patterns: **Batch (ETL)**, **Modern (ELT)**, **Real-Time (Streaming)**, and **Hybrid (Lambda)**.
        For each pattern you’ll learn the trade-offs, ideal use cases, and how different business verticals drive value from them.
        
        Data pipelines are not one‑size‑fits‑all. The batch (ETL) pattern remains relevant for legacy systems and scheduled reporting. Modern ELT has become 
        the default for cloud data warehousing, offering flexibility and scalability. Real‑time streaming is essential for fraud, monitoring, and instant actions 
        but carries higher costs and complexity. Lambda architecture provides a unified view but is best reserved for the most demanding hybrid use cases.

        From finance to healthcare to retail, the business impact of choosing the right pattern is measurable: lower costs, faster insights, reduced risk, and 
        better customer experiences. By understanding the trade-offs outlined above, data leaders can architect pipelines that deliver both operational excellence 
        and strategic value.
        """
    )
    st.markdown("---")

    # 1. BATCH (ETL)
    st.header("1. Batch Pattern (ETL – Extract, Transform, Load)")
    st.write(
        """
        Transform data *before* it lands in the warehouse. Best when data must be clean and validated before storage.
        """
    )
    with st.expander("When to use Batch (ETL)", expanded=False):
        st.markdown(
            """
            - Nightly sales reporting from transactional databases
            - Data migration from on-premise to cloud
            - Regulatory reporting (financial filings, compliance)
            - Batch scoring of ML models (daily customer churn)
            """
        )

    st.subheader("Trade-offs")
    tradeoff_batch = pd.DataFrame({
        "Dimension": ["Latency", "Cost", "Complexity", "Consistency", "Fault Tolerance"],
        "Assessment": [
            "High (minutes to days) – fixed windows",
            "Low to medium – moderate volume",
            "Low to medium – mature tooling (Airflow, Talend)",
            "Strong – clean data before load",
            "Simple – retry from checkpoint, DLQ for rejects"
        ]
    })
    st.dataframe(tradeoff_batch, use_container_width=True, hide_index=True)

    st.subheader("Sample Use Cases")
    st.markdown("- End-of-day reconciliation in banking\n- Weekly inventory forecasting in retail\n- Monthly quality metrics in healthcare")
    st.markdown("---")

    # 2. MODERN (ELT)
    st.header("2. Modern Pattern (ELT – Extract, Load, Transform)")
    st.write(
        """
        Load raw data first, then transform inside the warehouse. Leverages cloud compute power at scale.
        """
    )
    with st.expander("When to use Modern (ELT)", expanded=False):
        st.markdown(
            """
            - Cloud data warehousing (Snowflake, BigQuery, Redshift)
            - Self-service analytics – business users transform raw data with dbt
            - Data lakehouses (Databricks) where raw files are stored and later transformed
            - A/B test analysis – raw event logs loaded first, then filtered
            """
        )

    st.subheader("Trade-offs")
    tradeoff_elt = pd.DataFrame({
        "Dimension": ["Latency", "Cost", "Complexity", "Consistency", "Fault Tolerance"],
        "Assessment": [
            "Medium – raw data lands quickly, transformation later",
            "Low storage cost, transformation can spike (cloud warehouse compute)",
            "Medium – needs ELT tools (Fivetran, dbt)",
            "Good – raw data preserved, transformations versioned",
            "High – raw layer as source of truth, re-transform anytime"
        ]
    })
    st.dataframe(tradeoff_elt, use_container_width=True, hide_index=True)

    st.subheader("Sample Use Cases")
    st.markdown("- Centralized risk data lake for stress testing in finance\n- Customer 360 in e-commerce\n- Research data lake for genomic/imaging data")
    st.markdown("---")

    # 3. REAL-TIME (STREAMING)
    st.header("3. Real-Time Pattern (Streaming Pipeline)")
    st.write(
        """
        Events processed continuously as they arrive – no waiting for batches. Latency in milliseconds.
        """
    )
    with st.expander("When to use Real-Time Streaming", expanded=False):
        st.markdown(
            """
            - Fraud detection (decline transaction in milliseconds)
            - Real-time inventory management (decrement stock instantly)
            - Live dashboards for IoT sensors or website clicks
            - Alerting (server CPU > 90% → PagerDuty)
            """
        )

    st.subheader("Trade-offs")
    tradeoff_stream = pd.DataFrame({
        "Dimension": ["Latency", "Cost", "Complexity", "Consistency", "Fault Tolerance"],
        "Assessment": [
            "Very low (milliseconds to seconds)",
            "High – dedicated infrastructure (Kafka, Flink), ops overhead",
            "High – exactly-once, state management, windowing",
            "Weak unless exactly-once – at-least-once common",
            "Challenging – checkpointing, idempotent sinks, DLQ/retry"
        ]
    })
    st.dataframe(tradeoff_stream, use_container_width=True, hide_index=True)

    st.subheader("Sample Use Cases")
    st.markdown("- Credit card fraud detection\n- Real-time bidding in advertising\n- Patient monitoring alerts in healthcare")
    st.markdown("---")

    # 4. HYBRID (LAMBDA)
    st.header("4. Hybrid Pattern (Lambda Architecture)")
    st.write(
        """
        Batch layer for accuracy + speed layer for low latency. Serving layer merges both views.
        """
    )
    with st.expander("When to use Lambda", expanded=False):
        st.markdown(
            """
            - Recommendation engines (batch for user preferences, speed for last-minute clicks)
            - Financial risk monitoring (batch for end-of-day VaR, streaming for intraday limit breaches)
            - Social media analytics (trending topics real-time + historical engagement batch)
            """
        )

    st.subheader("Trade-offs")
    tradeoff_lambda = pd.DataFrame({
        "Dimension": ["Latency", "Cost", "Complexity", "Consistency", "Fault Tolerance"],
        "Assessment": [
            "Dual – batch high, speed low; serving merges",
            "Very high – run two pipelines in parallel",
            "Very high – maintain two code paths, tricky merging",
            "Good – temporary inconsistencies until batch catches up",
            "Robust – if one layer fails, other can fill gaps"
        ]
    })
    st.dataframe(tradeoff_lambda, use_container_width=True, hide_index=True)

    st.subheader("Sample Use Cases")
    st.markdown("- Real-time position keeping + daily P&L attribution in investment banking\n- Trending now + top 10 this month on streaming platforms\n- Quality control in manufacturing (real-time defect + batch SPC)")
    st.markdown("---")

    # BUSINESS IMPACT BY VERTICAL
    st.header("Business Impact by Vertical")
    st.write("How each pipeline pattern creates value across six major industries.")

    impact_data = {
        "Vertical": ["Financial Services", "Retail & E‑commerce", "Healthcare & Life Sciences", "Manufacturing", "Media & Entertainment", "Telecommunications"],
        "Batch (ETL) Impact": [
            "End-of-day reconciliation, AML batch screening, regulatory reports",
            "Weekly inventory forecasting, supplier payments, historical sales",
            "HIPAA ETL from EHRs, monthly quality metrics",
            "Daily production reports, maintenance schedules",
            "Monthly licensing reports, audience measurement, billing",
            "Call detail record billing, network capacity planning"
        ],
        "Modern (ELT) Impact": [
            "Risk data lake for stress testing – analysts explore raw transactions",
            "Customer 360 – clickstream, purchase, support data for segmentation",
            "Research data lake – genomic, imaging, clinical trials",
            "Manufacturing data lake from PLCs, SCADA, MES for benchmarking",
            "Data lake for user behavior – watch history, in‑app events",
            "Unified customer data platform (network logs + CRM + support)"
        ],
        "Real-Time Impact": [
            "Fraud detection (card declines), high‑frequency trading, real‑time credit scoring",
            "Real‑time stock updates, flash sale dashboards, abandoned cart triggers",
            "Patient monitoring (ICU alerts), real‑time lab results",
            "Predictive maintenance – anomaly detection to reduce downtime",
            "Ad serving (real‑time bidding), live stream bitrate adaptation",
            "Network anomaly detection, SIM swap fraud detection"
        ],
        "Hybrid (Lambda) Impact": [
            "Real‑time position keeping + daily P&L attribution",
            "Recommendation engine: batch collaborative filtering + streaming session‑based",
            "Population health: batch chronic disease trends + streaming outbreak detection",
            "Quality control: batch SPC limits + real‑time defect detection",
            "Trending now (streaming) + top 10 this month (batch)",
            "QoS dashboards: batch SLA reporting + live congestion alerts"
        ]
    }
    df_impact = pd.DataFrame(impact_data)
    st.dataframe(df_impact, use_container_width=True, hide_index=True)
    st.markdown("---")

    # DECISION FRAMEWORK
    st.header("How to Choose the Right Pattern (Decision Framework)")
    st.write(
        """
        Ask these questions in order:

        1. **What is the required latency?**  
           - Seconds → Real-time or Lambda  
           - Minutes to hours → ELT (micro-batch) or ETL  
           - Daily → Batch  

        2. **Do you need to keep raw data forever?**  
           - Yes → ELT or Lambda  
           - No → ETL  

        3. **What is your tolerance for operational complexity?**  
           - Low → Batch or ELT  
           - High (and strong streaming team) → Real-time or Lambda  

        4. **Do you need both historical accuracy and real‑time updates?**  
           - Yes → Lambda (or Kappa if you can reprocess from a stream)  
           - No → Single pattern  

        5. **Cloud vs on‑premise?**  
           - Cloud warehouse (Snowflake/BigQuery) → ELT is natural  
           - On‑premise relational DB → Traditional ETL
        """
    )
    st.markdown("---")

    # SUMMARY TABLE: PATTERNS AT A GLANCE
    st.header("Summary: Patterns at a Glance")
    summary_df = pd.DataFrame({
        "Pattern": ["Batch (ETL)", "Modern (ELT)", "Real-Time (Streaming)", "Hybrid (Lambda)"],
        "Best for": ["Scheduled reporting, clean data before storage", "Cloud data warehousing, raw data first", "Millisecond latency, event-driven actions", "Historical accuracy + real-time recency"],
        "Latency": ["High (minutes to days)", "Medium (raw fast, transform later)", "Very low (ms to seconds)", "Dual (batch high, speed low)"],
        "Cost": ["Low to medium", "Low storage, compute variable", "High", "Very high"],
        "Complexity": ["Low to medium", "Medium", "High", "Very high"]
    })
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
    st.markdown("---")

    # GREAT RESOURCES
    st.header("Great Resources to Go Deeper")
    res_df = pd.DataFrame({
        "Category": ["Books", "Courses", "Tools & Docs", "Community"],
        "Recommendations": [
            "Designing Data-Intensive Applications – Martin Kleppmann\nFundamentals of Data Engineering – Reis & Housley",
            "Data Engineering Zoomcamp (free)\nCoursera: Data Engineering on Google Cloud",
            "Apache Airflow, dbt, Kafka, Flink, Spark Streaming\nSnowflake / BigQuery documentation",
            "r/dataengineering\nDataTalks.Club\nLocally Optimistic"
        ]
    })
    st.dataframe(res_df, use_container_width=True, hide_index=True)

    st.markdown(
        """
        **Next steps:**  
        - Start with batch/ELT for 80% of your use cases.  
        - Add real-time only for the subset that truly needs it.  
        - Avoid Lambda unless you have a dedicated platform team.  
        - Measure business impact: reduced fraud losses, higher conversion, less downtime.

        Choose wisely – your pipelines are a strategic asset.
        """
    )
    st.markdown("---")
    st.caption("Data Pipeline Patterns | Trade-offs, Use Cases & Business Impact by Vertical")
