import streamlit as st
import pandas as pd

TITLE = "Data Pipelines, a Guide for Data Professionals"
CATEGORY = "data_engineering"
KEYWORDS = [
    "data pipelines", "ETL", "ELT", "streaming", "lambda architecture",
    "batch processing", "war story", "real-time", "data engineering", "data science"
]

def show():
    st.title(TITLE)
    st.caption("Category: Data Engineering | Level: Intermediate | 4 pipeline patterns explained with real‑world stories")
    st.markdown("---")

    # INTRODUCTION – SETTING THE STAGE
    st.write(
        """
        Assume you are a data wrangler. You have probably heard “data pipeline” thrown around a thousand times.  
        Maybe you’ve built a few yourself – a cron job that runs a Python script, an Airflow DAG held together by duct tape,  
        or a Kafka stream that you secretly hope never breaks.

        But let’s get real: data pipelines are the unsung heroes (or villains) of every data‑driven organisation.  
        When they work, nobody notices. When they fail, suddenly everyone’s a data engineer.

        In this guide, we’ll talk through the four core pipeline patterns – **ETL, ELT, streaming, and Lambda** –  
        with enough technical detail for an intermediate data scientist or analyst. I will share trade‑offs, real‑world 
        war stories, and resources that actually helped me when I was learning.

        """
    )
    st.markdown("---")

    # 1. BATCH ETL
    st.header("Batch ETL – The Old Reliable (But Slow)")
    st.write(
        """
        The classic. You pull data every night, transform it on a staging server, then load it into a warehouse.
        """
    )
    with st.expander("When to use Batch ETL", expanded=False):
        st.markdown(
            """
            - **Regulatory obligations** – Finance, healthcare. You need an audit trail of exactly what was cleaned and when.
            - **Legacy warehouses** – Many on‑premise data warehouses (Teradata, Oracle) are optimised for clean, batch loads.
            - **Complex, multi‑step transformations** – If you need to join 20 tables and run business rules that are hard to express in SQL.
            """
        )

    st.subheader("Trade‑offs (the real talk)")
    tradeoff_batch = pd.DataFrame({
        "Dimension": ["Latency", "Cost", "Complexity", "Fault Tolerance", "Vibe"],
        "Assessment": [
            "High (minutes to days) – your dashboard shows yesterday's data",
            "Low to moderate – spin up a server only during batch window",
            "Low to medium – mature tooling (Airflow, Talend), easy debugging",
            "Simple – restart from checkpoint, DLQ for rejects",
            "Old Reliable, but don't run it every hour on Black Friday"
        ]
    })
    st.dataframe(tradeoff_batch, use_container_width=True, hide_index=True)

    st.subheader("War story")
    st.info(
        """
        **Micro‑batch meltdown** – A retail startup ran ETL every hour because “real‑time is overrated.”  
        Then Black Friday hit. Their transformation server melted. They learned the hard way that ETL’s cost advantage  
        disappears when you run it every 60 minutes on 10x normal volume. They switched to ELT the next month.
        """
    )
    st.markdown("---")

    # 2. MODERN ELT
    st.header("Modern ELT – The Cloud Native")
    st.write(
        """
        The cool kid. You load raw data into a cloud warehouse (Snowflake, BigQuery, Redshift) as‑is,  
        then transform it inside the warehouse using SQL or engines like dbt.
        """
    )
    with st.expander("When to use Modern ELT", expanded=False):
        st.markdown(
            """
            - **Cloud‑native data stacks** – Snowflake + dbt + Looker is the modern standard.
            - **Exploratory analytics** – Analysts love it because raw data is always available.
            - **Self‑serve** – Business users can write their own transformations (with governance).
            """
        )

    st.subheader("Trade‑offs (the real talk)")
    tradeoff_elt = pd.DataFrame({
        "Dimension": ["Latency", "Cost", "Complexity", "Fault Tolerance", "Vibe"],
        "Assessment": [
            "Medium – raw data lands quickly, transformations run on schedule",
            "Low storage, but transformation cost can spike (full scans hurt)",
            "Medium – manage dependencies (dbt helps), schema evolution",
            "High – raw layer is immutable, fix SQL and re‑run",
            "Cloud native – but watch your warehouse bill"
        ]
    })
    st.dataframe(tradeoff_elt, use_container_width=True, hide_index=True)

    st.subheader("War story")
    st.info(
        """
        **The `SELECT *` trap** – A fintech used ELT with dbt. Their payment provider added a new field `risk_score`.  
        Raw load worked fine, but all downstream models broke because they used `SELECT *` and assumed column order.  
        They learned to use explicit column lists and add schema tests. Painful but memorable.
        """
    )
    st.markdown("---")

    # 3. REAL‑TIME STREAMING
    st.header("Real‑Time Streaming – The Need for Speed")
    st.write(
        """
        For when “nightly” is a swear word. Events are processed as they arrive – no waiting, no batches.
        """
    )
    with st.expander("When to use Real‑Time Streaming", expanded=False):
        st.markdown(
            """
            - **Fraud detection** – Decline a transaction in under 100ms.
            - **Real‑time monitoring** – Server metrics, Uber driver locations.
            - **Event‑driven architectures** – Trigger face recognition immediately after photo upload.
            """
        )

    st.subheader("Trade‑offs (the real talk)")
    tradeoff_stream = pd.DataFrame({
        "Dimension": ["Latency", "Cost", "Complexity", "Consistency", "Fault Tolerance", "Vibe"],
        "Assessment": [
            "Very low (milliseconds to seconds)",
            "High – Kafka cluster, Flink, ops overhead",
            "High – exactly‑once, state management, watermarking",
            "Often at‑least‑once – true exactly‑once is hard",
            "Challenging – checkpointing, idempotent sinks",
            "Exciting when it works, terrifying when it breaks"
        ]
    })
    st.dataframe(tradeoff_stream, use_container_width=True, hide_index=True)

    st.subheader("War story")
    st.info(
        """
        **Streaming anxiety** – A logistics company built a real‑time pipeline to track delivery vans using Kafka + Flink.  
        A misconfigured window caused state to blow up (hours‑long windows on millions of events).  
        Their Flink job crashed, and recovery took 6 hours because they hadn’t tuned checkpointing.  
        The ops team now has a “streaming anxiety” support group.
        """
    )
    st.warning(
        "**When to say no**: If you can tolerate 5‑minute latency, use micro‑batching. Real‑time is a surgical tool, not a default."
    )
    st.markdown("---")

    # 4. LAMBDA ARCHITECTURE
    st.header("Lambda Architecture – The 'I Want It All' Pattern")
    st.write(
        """
        Batch + speed layers, merged at serving time. Batch gives accurate historical views, speed gives low‑latency recent data.
        """
    )
    with st.expander("When to use Lambda", expanded=False):
        st.markdown(
            """
            - **Recommendation engines** – Batch computes user preferences overnight, speed layer incorporates last‑minute clicks.
            - **Financial risk dashboards** – End‑of‑day VaR (batch) + intra‑day limit breaches (streaming).
            - **Social media analytics** – “Trending now” (streaming) + “top posts this month” (batch).
            """
        )

    st.subheader("Trade‑offs (the real talk)")
    tradeoff_lambda = pd.DataFrame({
        "Dimension": ["Latency", "Cost", "Complexity", "Fault Tolerance", "Vibe"],
        "Assessment": [
            "Dual – batch high, speed low; serving merges",
            "Very high – run two pipelines in parallel",
            "Very high – maintain two code paths, tricky merging",
            "Robust – if one layer fails, the other can fill gaps",
            "Powerful but complex – many teams eventually move to Kappa"
        ]
    })
    st.dataframe(tradeoff_lambda, use_container_width=True, hide_index=True)

    st.subheader("The dirty secret & war story")
    st.info(
        """
        **The dirty secret**: Many teams that start with Lambda eventually move to **Kappa architecture** – streaming only,  
        with the ability to reprocess historical data by replaying the event log. It’s simpler, but requires your stream processor to handle historical throughput.

        **War story**: A music streaming service used Lambda for personalised playlists. Batch ran nightly, speed layer every minute.  
        The two layers never quite matched – a song listened to 59 minutes ago appeared in speed but not batch.  
        Users saw playlists flip‑flop. They spent months fixing merging logic before giving up and moving to Kappa with Flink.
        """
    )
    st.markdown("---")

    # DECISION FRAMEWORK
    st.header("Decision Framework")
    st.write(
        """
        Ask yourself these questions – they’ve saved me from over‑engineering more than once.

        1. **What’s the required data freshness?**  
           - Seconds → Real‑time or Lambda  
           - Minutes to hours → ELT with micro‑batching  
           - Daily → Batch ETL or nightly ELT  

        2. **Do you need to keep raw data forever?**  
           - Yes (compliance, reprocessing) → ELT or Lambda  
           - No → ETL  

        3. **What’s your team’s skill set?**  
           - Strong SQL, weak Python/Java → ELT + dbt  
           - Strong software engineers → Streaming or Lambda  
           - Mixed → Start with ELT, add streaming only where needed  

        4. **What’s your budget (time + money)?**  
           - Low → Batch ETL on a single server  
           - Medium → ELT on Snowflake  
           - High and critical latency → Real‑time  

        5. **Do you need both perfect accuracy and low latency?**  
           - Yes → Lambda (but consider Kappa)  
           - No → Single pattern  

        **A pragmatic path:**  
        - Start with ELT. It’s flexible, cloud‑friendly, and forgiving.  
        - Add streaming for the 20% of use cases that truly need it.  
        - Only consider Lambda if you have a dedicated platform team and a clear, long‑term need.
        """
    )
    st.markdown("---")

    # SUMMARY TABLE
    st.header("Summary: Patterns at a Glance")
    summary_df = pd.DataFrame({
        "Pattern": ["Batch ETL", "Modern ELT", "Real‑time Streaming", "Lambda"],
        "Latency": ["High (daily)", "Medium (raw fast, transform scheduled)", "Very low (ms)", "Dual (batch + speed)"],
        "Cost": ["Low–medium", "Low storage, compute variable", "High", "Very high"],
        "Complexity": ["Low–medium", "Medium", "High", "Very high"],
        "Best for": ["Legacy / compliance", "Cloud data warehouses", "Fraud / monitoring", "Recommendations / risk"]
    })
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
    st.markdown("---")

    # QUALITY RESOURCES
    st.header("Quality Resources That Actually Help")
    st.write(" Here are resources that respect your time and intelligence.")

    resources_df = pd.DataFrame({
        "Category": ["Books", "Free Courses", "Blogs & Newsletters", "Tools to Learn", "Communities"],
        "Recommendations": [
            "Designing Data‑Intensive Applications – Kleppmann\nFundamentals of Data Engineering – Reis & Housley",
            "Data Engineering Zoomcamp (DataTalks.Club)\nApache Flink Training (Ververica)",
            "Benn Stancil’s Substack\ndbt Developer Hub\nUber / Netflix engineering blogs",
            "Airbyte (ELT)\ndbt Core\nApache Kafka (Docker)\nApache Flink (fraud detection tutorial)",
            "r/dataengineering (Reddit)\nLocally Optimistic Slack\ndbt Slack"
        ]
    })
    st.dataframe(resources_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown(
        """
        **Final thoughts**  
        Data pipelines are the foundation of trust in your data. A beautiful dashboard or a sophisticated ML model is worthless if the pipeline behind it is a house of cards.

        **My advice to you:**  
        - Start simple. Batch ELT (not ETL) is often enough.  
        - Instrument everything – logging, monitoring, alerting. If you can’t see your pipeline failing, it’s already failing.  
        - Treat your transformation code (SQL, dbt, Python) with the same rigour as production software.  
        - Don’t chase “real‑time” because it sounds cool. Real‑time is a feature, not a religion.

        You now have a mental framework to evaluate pipeline patterns, understand trade‑offs, and avoid common mistakes.  
        Go build pipelines that let you sleep at night.

        
        """
    )
    st.markdown("---")
    st.caption("Data Pipelines | Conversational guide for intermediate data pros | Trade-offs, war stories, and resources that actually help")