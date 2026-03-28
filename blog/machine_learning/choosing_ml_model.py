import streamlit as st
import pandas as pd

TITLE = "Choosing the Best Machine Learning Model"
CATEGORY = "machine_learning"
KEYWORDS = ["model selection", "EDA", "machine learning workflow", "classification", "regression", "clustering", "time series", "hyperparameter tuning", "model evaluation", "data analysis"]


def show():

    st.title("Dataset Analysis and Choice of Machine Learning Model")
    st.caption("Category: machine_learning | Level: Intermediate → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        This guide follows a **top-down approach**: start from the problem definition, gradually move into data understanding, 
        and then drill down into model selection, evaluation, and tuning.
        
        The goal is to provide a systematic framework for choosing the right machine learning model based on your data, 
        constraints, and business requirements.
        """
    )
    
    # ============================================
    # LEVEL 1: Understand the Problem
    # ============================================
    st.header("LEVEL 1 — Understand the Problem (Top-Level Strategy)")
    
    st.write(
        """
        Before touching the data or algorithms, ask:
        
        **1. What type of problem are we solving?**
        
        All models depend on the problem category.
        """
    )
    
    problem_data = {
        "Problem Type": ["Classification", "Regression", "Clustering", "Time Series", "NLP", "Computer Vision"],
        "Example": [
            "Fraud detection, churn prediction",
            "Sales forecasting, house prices",
            "Customer segmentation",
            "Demand prediction",
            "Sentiment analysis",
            "Object detection"
        ],
        "Model Families": [
            "Logistic Regression, Random Forest, SVM, XGBoost, Neural Nets",
            "Linear Regression, Random Forest Regressor, XGBoost Regressor",
            "K-Means, DBSCAN, Hierarchical",
            "ARIMA, Prophet, LSTMs",
            "BERT, GPT, LSTMs",
            "CNNs, ViT"
        ]
    }
    df_problem = pd.DataFrame(problem_data)
    st.dataframe(df_problem, use_container_width=True)
    
    st.info("Never choose a model before identifying the problem type.")
    
    st.divider()
    
    # ============================================
    # LEVEL 2: Analyze the Dataset
    # ============================================
    st.header("LEVEL 2 — Analyze the Dataset (Structure First, Content Later)")
    
    st.subheader("2. Identify the Dataset Structure")
    st.write(
        """
        Ask: Is it:
        - Tabular data?
        - Time-series data?
        - Text data?
        - Image/video data?
        - Streaming or batch data?
        
        Different structures → Different model families.
        """
    )
    
    st.subheader("3. Check Data Quantity")
    st.write("Quantity strongly influences model selection.")
    
    quantity_data = {
        "Dataset Size": ["Small (< 10k rows)", "Medium (10k–1M rows)", "Large (> 1M rows)"],
        "Recommended Models": [
            "Logistic/Linear Regression, Decision Trees, Naive Bayes, SVM (small–medium only)",
            "Random Forest, Gradient Boosting (XGBoost, LightGBM, CatBoost)",
            "Deep Learning (Neural Networks), Distributed ML (Spark MLlib)"
        ]
    }
    df_quantity = pd.DataFrame(quantity_data)
    st.dataframe(df_quantity, use_container_width=True)
    
    st.subheader("4. Check Data Quality")
    st.write(
        """
        Look at:
        - Missing values
        - Imbalance in target classes
        - Noise or outliers
        - Mixed data types
        - High cardinality categories
        - Duplicates
        
        *Poor data quality → simpler or robust models perform better.*
        """
    )
    
    st.divider()
    
    # ============================================
    # LEVEL 3: Exploratory Data Analysis (EDA)
    # ============================================
    st.header("LEVEL 3 — Exploratory Data Analysis (EDA)")
    
    st.write(
        """
        This helps identify the model requirements.
        
        **5. EDA for Relationships**
        
        Check:
        - Correlation heatmap (numerical)
        - Feature distributions
        - Scatter plots (numeric)
        - Boxplots (outliers)
        - Bar charts (categorical)
        """
    )
    
    eda_data = {
        "Pattern Detected": [
            "Linear relationships",
            "Non-linear patterns",
            "Many categories",
            "Sparse text",
            "Seasonality"
        ],
        "Implication for Modeling": [
            "→ Linear models",
            "→ Tree-based or Neural networks",
            "→ CatBoost works well",
            "→ NLP models needed",
            "→ Time series models"
        ]
    }
    df_eda = pd.DataFrame(eda_data)
    st.dataframe(df_eda, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # LEVEL 4: Define Model Requirements
    # ============================================
    st.header("LEVEL 4 — Define Model Requirements (Before Choosing Models)")
    
    st.subheader("6. Decide What Matters Most")
    st.write("Every modeling task has trade-offs.")
    
    requirements_data = {
        "Priority": [
            "Interpretability required",
            "Speed required",
            "Accuracy is the main goal",
            "High-dimensional data",
            "Mixed categorical + numerical",
            "Imbalanced problem"
        ],
        "Recommended Approach": [
            "→ Logistic/Linear Regression, Decision Trees, Explainable Boosting Machines",
            "→ Naive Bayes, Logistic Regression, Linear SVM",
            "→ XGBoost, LightGBM, CatBoost, Neural Networks",
            "→ Linear models, SVM, PCA + ML models",
            "→ CatBoost, Random Forest",
            "→ XGBoost, Random Forest + class weights or SMOTE"
        ]
    }
    df_requirements = pd.DataFrame(requirements_data)
    st.dataframe(df_requirements, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # LEVEL 5: Choose Candidate Models
    # ============================================
    st.header("LEVEL 5 — Choose Candidate Models (Model Search Space)")
    
    st.write("Select 2–5 algorithms that match the problem, dataset size, and constraints.")
    
    st.subheader("7. Recommended Model Families by Scenario")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**For Classification**")
        st.markdown(
            """
            - **Baseline:** Logistic Regression, Naive Bayes
            - **Strong models:** Random Forest, Gradient Boosting (XGBoost/LightGBM)
            - **Complex:** Deep Neural Nets
            """
        )
        
        st.markdown("**For Regression**")
        st.markdown(
            """
            - **Baseline:** Linear Regression, Decision Tree
            - **Strong:** Random Forest Regressor, XGBoost Regressor
            - **Complex:** Neural Networks, LSTMs (for sequences)
            """
        )
        
        st.markdown("**For Clustering**")
        st.markdown(
            """
            - **K-Means** (simple, scalable)
            - **DBSCAN** (noise-resistant)
            - **Hierarchical** (small datasets)
            """
        )
    
    with col2:
        st.markdown("**For Time Series**")
        st.markdown(
            """
            - **ARIMA** (classic)
            - **Prophet** (quick and explainable)
            - **Deep Learning** (LSTM, Transformers)
            """
        )
        
        st.markdown("**For Natural Language Processing (NLP)**")
        st.markdown(
            """
            - **Naive Bayes** (small text)
            - **TF-IDF + SVM**
            - **Transformers** (BERT, GPT)
            """
        )
        
        st.markdown("**For Computer Vision**")
        st.markdown(
            """
            - **CNNs** (ResNet, EfficientNet)
            - **Vision Transformers** (ViT)
            """
        )
    
    st.divider()
    
    # ============================================
    # LEVEL 6: Train and Validate Models
    # ============================================
    st.header("LEVEL 6 — Train and Validate Models")
    
    st.subheader("8. Use Proper Train-Test Splits")
    st.write(
        """
        - 80/20 or 70/30 split
        - Or cross-validation (recommended for tabular data)
        """
    )
    
    st.subheader("9. Key Training Steps")
    st.markdown(
        """
        - Transform/encode features
        - Normalize if required (for SVM, KNN, NN)
        - Fit the model to training data
        - Validate using cross-validation
        """
    )
    
    st.divider()
    
    # ============================================
    # LEVEL 7: Evaluate the Models
    # ============================================
    st.header("LEVEL 7 — Evaluate the Models")
    
    st.subheader("10. Choose the Right Metrics")
    
    metrics_data = {
        "Problem Type": ["Classification", "Regression", "Clustering", "Time Series"],
        "Metrics": [
            "Accuracy, Precision, Recall, F1 Score, ROC-AUC, Confusion Matrix",
            "MAE, RMSE, R²",
            "Silhouette Score, Davies-Bouldin Index",
            "MAPE, RMSE, Forecast bias"
        ]
    }
    df_metrics = pd.DataFrame(metrics_data)
    st.dataframe(df_metrics, use_container_width=True)
    
    st.info("**Rule of Thumb:** Always judge models using the metric aligned with business goals.")
    
    st.divider()
    
    # ============================================
    # LEVEL 8: Select the Best Model
    # ============================================
    st.header("LEVEL 8 — Select the Best Model")
    
    st.write(
        """
        Pick the model that best satisfies:
        
        1. **Business Requirements**
           - Explainability?
           - Speed?
           - Accuracy?
           - Stability?
        
        2. **Performance Metrics**
           - Best score on validation/test set
        
        3. **Complexity**
           - Avoid overly complex models if simpler ones perform similarly
        """
    )
    
    st.divider()
    
    # ============================================
    # LEVEL 9: Tune the Winning Model
    # ============================================
    st.header("LEVEL 9 — Tune the Winning Model (Optimization)")
    
    st.subheader("11. Hyperparameter Tuning Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Recommended**")
        st.markdown(
            """
            - **RandomizedSearchCV** (fast + effective)
            - **GridSearchCV** (slow but thorough)
            """
        )
    
    with col2:
        st.markdown("**Advanced**")
        st.markdown(
            """
            - **Optuna**
            - **Hyperopt**
            - **Bayesian Optimization**
            """
        )
    
    st.subheader("Key Hyperparameters to Tune")
    
    hyperparams_data = {
        "Model": ["Random Forest", "XGBoost", "SVM", "K-Means", "Neural Networks"],
        "Hyperparameters": [
            "n_estimators, max_depth",
            "learning_rate, max_depth, subsample",
            "C, gamma, kernel",
            "n_clusters",
            "learning_rate, batch_size, layers"
        ]
    }
    df_hyperparams = pd.DataFrame(hyperparams_data)
    st.dataframe(df_hyperparams, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # LEVEL 10: Finalize the Model
    # ============================================
    st.header("LEVEL 10 — Finalize the Model")
    
    st.subheader("12. Perform Final Steps")
    st.markdown(
        """
        - Retrain model on full dataset
        - Save model (Pickle, Joblib, ONNX, SavedModel)
        - Monitor drift over time
        - Re-train periodically
        """
    )
    
    st.divider()
    
    # ============================================
    # COMPLETE FLOW SUMMARY
    # ============================================
    st.header("COMPLETE FLOW (Top-Down Summary)")
    
    flow_steps = [
        "1. Define the business problem",
        "2. Identify problem type (classification, regression, etc.)",
        "3. Understand data structure",
        "4. Examine data quantity & quality",
        "5. Conduct EDA",
        "6. Define model constraints (interpretability, accuracy, speed)",
        "7. Select candidate models",
        "8. Train them properly",
        "9. Evaluate using correct metrics",
        "10. Choose the best model",
        "11. Tune it for maximum performance",
        "12. Deploy & monitor"
    ]
    
    for step in flow_steps:
        st.write(f"- {step}")
    
    st.divider()
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")
    
    st.write(
        """
        Choosing the right machine learning model is not about picking the most complex or popular algorithm. 
        It's a systematic process that starts with understanding your problem, analyzing your data, and aligning 
        model capabilities with business requirements.
        
        **Key Takeaways:**
        
        - **Start with the problem**, not the algorithm
        - **Let your data guide** your model selection—quantity, quality, and structure matter
        - **Use EDA to uncover patterns** that point toward appropriate model families
        - **Define constraints early**—interpretability, speed, and accuracy often involve trade-offs
        - **Select 2–5 candidate models** and evaluate them systematically
        - **Use the right metrics** aligned with business objectives
        - **Tune hyperparameters** to extract maximum performance from your chosen model
        
        By following this top-down approach, you can confidently navigate the vast landscape of machine learning 
        algorithms and select the model that will deliver the best results for your specific use case.
        """
    )
    
    st.divider()
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Libraries for Model Selection & Tuning:**
        - [Scikit-learn](https://scikit-learn.org/stable/): Comprehensive ML toolkit
        - [XGBoost](https://xgboost.readthedocs.io/): Gradient boosting for tabular data
        - [LightGBM](https://lightgbm.readthedocs.io/): Fast gradient boosting
        - [CatBoost](https://catboost.ai/): Handles categorical features natively
        - [Optuna](https://optuna.org/): Advanced hyperparameter optimization
        
        **EDA Tools:**
        - [Pandas Profiling](https://pandas-profiling.github.io/pandas-profiling/docs/): Automated EDA reports
        - [Sweetviz](https://github.com/fbdesignpro/sweetviz): Visual EDA
        - [Seaborn](https://seaborn.pydata.org/): Statistical data visualization
        
        **Model Evaluation:**
        - [Yellowbrick](https://www.scikit-yb.org/): Visual diagnostics for model selection
        - [MLflow](https://mlflow.org/): Experiment tracking
        """
    )