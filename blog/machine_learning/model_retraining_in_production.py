import streamlit as st
import pandas as pd

TITLE = "Model Retraining and Monitoring in Production"
CATEGORY = "machine_learning"
KEYWORDS = ["model retraining", "ML monitoring", "data drift", "concept drift", "target drift", "MLOps", "model performance", "production ML", "model observability", "continuous retraining"]


def show():

    st.title("Model Retraining and Monitoring in Production")
    st.caption("Category: machine_learning | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        This is a clear, practical, and industry-standard guide on the conditions for retraining machine learning models 
        and how to monitor them in production.
        
        This guidance is applicable to all ML systems—classification, regression, NLP, CV, forecasting, and recommendation engines.
        """
    )
    
    # ============================================
    # SECTION 1: Key Conditions That Trigger Model Retraining
    # ============================================
    st.header("1. Key Conditions That Trigger Model Retraining")
    
    st.write(
        """
        Retraining is required when the model's performance or environment changes. 
        These conditions fall into four major categories:
        """
    )
    
    # Category A: Data Drift
    st.subheader("A. Data Drift (Changes in Input Data)")
    
    st.markdown("**1. Feature Drift**")
    st.write(
        """
        When the distribution of input features changes.
        
        **Examples:**
        - Product prices suddenly increase due to inflation
        - Customer behavior changes during seasons or holidays
        - New categories appear (new locations, new job titles, new devices)
        
        **Detection Methods:**
        - KS test
        - Population Stability Index (PSI)
        - Jensen-Shannon divergence
        - Moving window analysis
        
        **Condition to Retrain:** When drift metrics exceed defined thresholds.
        """
    )
    
    st.markdown("**2. Concept Drift**")
    st.write(
        """
        The relationship between features and target changes.
        
        **Examples:**
        - Fraud patterns evolve
        - Customer churn behavior changes
        - Market conditions shift
        
        **Symptoms:** Model prediction accuracy slowly drops even if input data distribution is stable.
        
        **Condition to Retrain:** When the model can no longer correctly map inputs → outputs due to environmental change.
        """
    )
    
    st.markdown("**3. Target Drift**")
    st.write(
        """
        When the distribution of the target variable changes.
        
        **Examples:**
        - More customers start defaulting on loans
        - A new class label appears
        - Seasonality affects demand levels
        
        **Condition to Retrain:** When the underlying target distribution changes significantly over time.
        """
    )
    
    # Category B: Performance Degradation
    st.subheader("B. Performance Degradation")
    
    st.markdown("**4. Drop in Accuracy/Precision/Recall**")
    st.write(
        """
        Monitor key performance metrics using real-world feedback.
        
        **Condition to Retrain:** When metrics fall below agreed SLA thresholds.
        """
    )
    
    st.markdown("**5. Increased Error Rates**")
    st.write(
        """
        - For regression models: Rising RMSE/MAE or forecast error
        - For classification: Increased false positives/false negatives
        
        **Condition to Retrain:** When real-world outcomes show higher variance or unpredictability.
        """
    )
    
    st.markdown("**6. Latency or Throughput Issues**")
    st.write(
        """
        The model becomes slow because:
        - Data size increased
        - Model complexity grew
        
        **Condition to Retrain:** When the model takes too long to produce predictions, causing business impact.
        """
    )
    
    # Category C: Business or Data Pipeline Changes
    st.subheader("C. Business or Data Pipeline Changes")
    
    st.markdown("**7. New Features or Data Sources Added**")
    st.write(
        """
        Retrain your model whenever:
        - A new data column becomes available
        - Data sources change (database → API)
        - Business logic is updated
        """
    )
    
    st.markdown("**8. Change in Business Strategy**")
    st.write(
        """
        **Examples:**
        - New KPI introduced
        - New customer segments
        - New pricing model
        
        **Condition to Retrain:** When model goals no longer align with business goals.
        """
    )
    
    st.markdown("**9. System Integration or API Changes**")
    st.write(
        """
        If the environment changes (e.g., database schema change), retraining may be required.
        """
    )
    
    # Category D: Time-Based Retraining
    st.subheader("D. Time-Based Retraining (Scheduled)")
    
    st.markdown("**10. Fixed Retraining Schedule**")
    st.write(
        """
        Some industries require periodic retraining:
        """
    )
    
    schedule_data = {
        "Industry": ["Finance/Fraud", "Healthcare diagnosis", "Retail demand forecasting", "Customer churn", "Credit scoring"],
        "Retrain Frequency": [
            "Weekly – monthly",
            "Monthly",
            "Weekly – quarterly",
            "Quarterly",
            "Once or twice a year"
        ]
    }
    df_schedule = pd.DataFrame(schedule_data)
    st.dataframe(df_schedule, use_container_width=True)
    
    st.write(
        """
        **Condition to Retrain:** Even without detected drift, regular retraining ensures model freshness.
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 2: How to Monitor Models for Retraining
    # ============================================
    st.header("2. How to Monitor Models for Retraining")
    
    st.write(
        """
        Monitoring ML models requires tracking all the above conditions using structured metrics.
        """
    )
    
    # A. Monitor Data Drift
    st.subheader("A. Monitor Data Drift")
    
    st.markdown("**Techniques:**")
    st.markdown(
        """
        - **Statistical Tests:** Kolmogorov–Smirnov (K-S test), Chi-square test, PSI (Population Stability Index – industry favorite), KL Divergence
        - **Visualization:** Feature histograms over time
        - **Automated Detectors:** Evidently AI, Alibi Detect
        """
    )
    
    st.markdown("**Signals:**")
    st.markdown(
        """
        - Change in distribution > threshold
        - Missing data increases
        - Rise in unexpected values or categories
        """
    )
    
    # B. Monitor Model Performance
    st.subheader("B. Monitor Model Performance")
    
    st.markdown("**Metrics:**")
    st.markdown(
        """
        - Accuracy, Precision/Recall, ROC-AUC
        - RMSE/MAE, MAPE
        """
    )
    
    st.markdown("**Methods:**")
    st.markdown(
        """
        - Shadow deployment
        - A/B testing
        - Real vs predicted monitoring
        - Rolling window performance tracking
        """
    )
    
    st.markdown("**Signals:**")
    st.markdown(
        """
        - Performance drops consistently for N days
        - Sudden drop beyond threshold
        - Increased variance that cannot be explained by noise
        """
    )
    
    # C. Monitor Operational Metrics
    st.subheader("C. Monitor Operational (System) Metrics")
    
    st.markdown("**Metrics:**")
    st.markdown(
        """
        - Latency
        - Throughput
        - Memory/CPU usage
        """
    )
    
    st.markdown("**Signals:**")
    st.markdown(
        """
        - Model becomes too slow
        - Infrastructure cost increases unexpectedly
        - Bottlenecks appear during inference
        """
    )
    
    # D. Monitor Business Metrics
    st.subheader("D. Monitor Business Metrics")
    
    st.markdown("**Examples:**")
    st.markdown(
        """
        - Drop in conversion rate
        - Increase in fraud cases missed
        - Poor customer satisfaction score
        """
    )
    
    st.markdown("**Signals:**")
    st.markdown(
        """
        - Business KPIs diverge from expected levels
        - Model predictions no longer lead to positive outcomes
        """
    )
    
    st.divider()
    
    # ============================================
    # SUMMARY TABLE
    # ============================================
    st.header("Summary Table: Conditions & Monitoring Methods")
    
    summary_data = {
        "Condition": ["Feature Drift", "Concept Drift", "Target Drift", "Low Accuracy", "High Error", "Latency Issues", "New Features", "Business Changes", "Scheduled"],
        "Monitoring Method": [
            "PSI, KS test",
            "Performance drops",
            "Distribution shifts",
            "Eval metrics",
            "MAE/RMSE spikes",
            "Inference logs",
            "Data pipeline update",
            "KPI monitoring",
            "Timers/Cron"
        ],
        "Retrain When": [
            "Drift > threshold",
            "Sudden or continuous drop",
            "Target freq changes",
            "Accuracy < SLA",
            "Error > threshold",
            "Slow inference",
            "Pipeline change",
            "Strategy updated",
            "Time reached"
        ]
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # BEST PRACTICES
    # ============================================
    st.header("Best Practices for Model Retraining")
    
    st.markdown(
        """
        **1. Establish Baselines Early**
        - Define performance SLAs before deployment
        - Capture initial data distributions as reference points
        
        **2. Implement Layered Monitoring**
        - Monitor data quality, model performance, and business impact
        - Don't rely on a single metric—use a dashboard approach
        
        **3. Automate Retraining Decisions**
        - Set up automated triggers based on thresholds
        - Include human-in-the-loop for critical decisions
        
        **4. Version Everything**
        - Version models, data, and training pipelines
        - Maintain ability to roll back to previous versions
        
        **5. Test Before Full Deployment**
        - Use canary deployments or A/B testing for new models
        - Validate that retrained models actually improve performance
        
        **6. Monitor Post-Retraining**
        - Track if retraining resolved the detected issues
        - Watch for unintended side effects
        """
    )
    
    st.divider()
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")
    
    st.write(
        """
        Model retraining is not a one-time event—it's a continuous process that ensures your ML systems remain 
        accurate, reliable, and aligned with business goals over time.
        
        **Key Takeaways:**
        
        - **Data drift, concept drift, and target drift** are the primary technical indicators for retraining
        - **Performance degradation** and **business metric changes** signal that your model may be outdated
        - **Scheduled retraining** provides a safety net even when drift isn't detected
        - **Comprehensive monitoring** across data, performance, operations, and business metrics is essential
        - **Automation** through MLOps pipelines makes retraining sustainable at scale
        
        By implementing robust monitoring and establishing clear retraining conditions, you can ensure your 
        machine learning models continue to deliver value long after their initial deployment.
        """
    )
    
    st.divider()
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Monitoring & Observability Tools:**
        - [Evidently AI](https://evidentlyai.com/): Open-source drift and performance monitoring
        - [Arize AI](https://arize.com/): Production model monitoring
        - [Prometheus](https://prometheus.io/): Metrics-based monitoring
        
        **MLOps Frameworks:**
        - [MLflow](https://mlflow.org/): Model lifecycle management
        - [Kubeflow](https://www.kubeflow.org/): ML pipelines on Kubernetes
        - [TensorFlow Extended (TFX)](https://www.tensorflow.org/tfx): Production ML pipelines
        
        **Further Reading:**
        - [MLOps: Continuous Delivery for Machine Learning](https://ml-ops.org/)
        - [Google's ML Production Readiness Checklist](https://developers.google.com/machine-learning/guides/rules-of-ml)
        - [Monitoring Machine Learning Models in Production](https://christophergs.com/machine%20learning/2020/03/14/how-to-monitor-machine-learning-models/)
        """
    )