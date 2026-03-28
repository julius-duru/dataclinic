import streamlit as st
import pandas as pd

TITLE = "Concept of Machine Learning"
CATEGORY = "machine_learning"
KEYWORDS = ["machine learning", "supervised learning", "unsupervised learning", "reinforcement learning", "model training", "model evaluation", "hyperparameter tuning", "ML workflow", "classification", "regression", "clustering"]


def show():

    st.title("Concept of Machine Learning (ML)")
    st.caption("Category: machine_learning | Level: Beginner → Intermediate")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        Machine Learning (ML) is a field of artificial intelligence that enables computers to learn patterns from data 
        and make predictions or decisions without being explicitly programmed. Instead of writing rule-based programs, 
        ML systems use algorithms to identify patterns, relationships, and trends within datasets, improving performance over time.
        
        Machine Learning powers everyday technologies—from product recommendations and fraud detection to chatbots, 
        medical diagnosis systems, and autonomous vehicles.
        """
    )

    # ============================================
    # SECTION 1: What is Machine Learning?
    # ============================================
    st.header("1. Machine Learning works")
    
    st.write(
        """
        Machine Learning uses statistical and mathematical models to analyze data and make predictions. 
        The learning process involves feeding data to algorithms, which then learn rules and patterns.
        """
    )
    
    st.subheader("Three Major Types of Machine Learning")
    
    ml_types_data = {
        "Type": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning"],
        "What It Does": [
            "Learns from labeled data",
            "Finds patterns in unlabeled data",
            "Learns by interacting with an environment"
        ],
        "Examples": [
            "Classification, Regression",
            "Clustering, Association",
            "Game AI, Robotics"
        ]
    }
    df_ml_types = pd.DataFrame(ml_types_data)
    st.dataframe(df_ml_types, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # SECTION 2: How to Create Machine Learning Models
    # ============================================
    st.header("2. How to Create Machine Learning Models")
    
    st.write(
        """
        Creating an ML model follows a structured pipeline.
        """
    )
    
    # Step 1: Define the Objective
    st.subheader("Step 1: Define the Objective")
    st.write(
        """
        Before picking any algorithm, ask:
        
        - What problem am I trying to solve?
        - Is it classification, regression, clustering, forecasting…?
        
        **Examples:**
        - Predict customer churn → Classification
        - Forecast sales → Regression
        - Group customers → Clustering
        """
    )
    
    # Step 2: Collect and Prepare Data
    st.subheader("Step 2: Collect and Prepare Data")
    st.write(
        """
        Data is the backbone of any ML model.
        
        **Data Preparation Tasks:**
        - Handle missing values
        - Remove duplicates
        - Fix inconsistent formats
        - Normalize or standardize numerical values
        - Encode categorical variables
        - Balance the dataset (if needed)
        - Split data into train-test sets
        
        *Proper data preparation dramatically improves model accuracy.*
        """
    )
    
    # Step 3: Choose the Right Model
    st.subheader("Step 3: Choose the Right Model (Model Selection)")
    st.write(
        """
        Choosing an ML model depends on several factors.
        """
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**1. Type of Problem**")
        problem_data = {
            "Problem": ["Classification", "Regression", "Clustering", "NLP", "Image Recognition"],
            "Suitable Algorithms": [
                "Logistic Regression, Random Forest, SVM, XGBoost, Naive Bayes",
                "Linear Regression, Random Forest Regressor, XGBoost, Lasso Regression",
                "K-Means, Hierarchical Clustering",
                "Transformer Models, LSTM, BERT",
                "CNNs, Vision Transformers"
            ]
        }
        df_problem = pd.DataFrame(problem_data)
        st.dataframe(df_problem, use_container_width=True)
    
    with col2:
        st.write("**2. Size of Dataset**")
        st.markdown(
            """
            - Small dataset → Logistic Regression, SVM
            - Large dataset → Random Forest, XGBoost
            - Very large dataset → Deep learning
            """
        )
        st.write("**3. Interpretability**")
        st.markdown(
            """
            - Need explainability? → Linear/Logistic Regression, Decision Trees
            - Performance over interpretability? → Ensemble models, neural networks
            """
        )
    
    # Step 4: Training
    st.subheader("Step 4: Training Machine Learning Models")
    st.write(
        """
        Training is the process of allowing the algorithm to learn from the training dataset.
        
        **What happens during training?**
        - The algorithm identifies relationships between features and the target output
        - Error (loss) is calculated
        - Model parameters are adjusted to minimize the error
        - This process continues over multiple iterations (epochs)
        
        **Training Best Practices:**
        - Use train-validation split or cross-validation
        - Prevent overfitting by:
            - Regularization
            - Early stopping
            - Dropout (neural networks)
            - Using simpler models or reducing noise
        """
    )
    
    # Step 5: Testing
    st.subheader("Step 5: Testing Machine Learning Models")
    st.write(
        """
        Testing assesses how well the model performs on unseen (new) data.
        
        **Purpose of Testing:**
        - Check generalization capability
        - Prevent over-optimistic performance estimates
        - Compare multiple models fairly
        
        Testing is done using:
        - Test set (typically 20–30% of the dataset)
        - Validation set (optional but recommended)
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 3: Model Evaluation Metrics
    # ============================================
    st.header("3. Model Evaluation Metrics")
    
    eval_data = {
        "Category": ["Classification", "Regression", "Clustering"],
        "Metrics": [
            "Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC, Log Loss",
            "Mean Absolute Error (MAE), Mean Squared Error (MSE), R² Score",
            "Silhouette Score, Davies-Bouldin Score, Within-Cluster-Sum-of-Squares (WCSS)"
        ]
    }
    df_eval = pd.DataFrame(eval_data)
    st.dataframe(df_eval, use_container_width=True)
    
    st.write(
        """
        **Important Consideration:** No single metric is perfect. Always choose metrics based on the business objective.
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 4: Model Tuning (Hyperparameter Optimization)
    # ============================================
    st.header("4. Model Tuning (Hyperparameter Optimization)")
    
    st.write(
        """
        Hyperparameters are settings you choose before training a model, e.g.,
        - Number of trees (Random Forest)
        - Learning rate (XGBoost, Neural Networks)
        - Max depth (Decision Trees)
        - Number of clusters (K-Means)
        """
    )
    
    tuning_data = {
        "Method": ["Grid Search", "Randomized Search", "Bayesian Optimization", "Hyperopt / Optuna", "Genetic Algorithms"],
        "Description": [
            "Tests every combination of parameters",
            "Random sampling of parameters (Fast & preferred)",
            "Advanced tuning using probability",
            "Automated hyperparameter optimization",
            "Evolutionary tuning approach"
        ]
    }
    df_tuning = pd.DataFrame(tuning_data)
    st.dataframe(df_tuning, use_container_width=True)
    
    st.subheader("Regularization (Controlling Model Complexity)")
    st.markdown(
        """
        - **L1 (Lasso):** Removes irrelevant features
        - **L2 (Ridge):** Shrinks coefficients
        - **Dropout** for neural networks
        """
    )
    
    st.divider()
    
    # ============================================
    # SECTION 5: Use Cases of Machine Learning
    # ============================================
    st.header("5. Use Cases of Machine Learning")
    
    usecase_data = {
        "Domain": ["Business & Finance", "Healthcare", "Retail", "Technology", "Manufacturing"],
        "Applications": [
            "Fraud detection, Customer churn prediction, Credit scoring, Sales forecasting",
            "Disease prediction, Medical image analysis, Drug discovery",
            "Recommendation engines, Demand forecasting, Price optimization",
            "Chatbots, Image recognition, Speech-to-text",
            "Predictive maintenance, Quality control, Anomaly detection"
        ]
    }
    df_usecase = pd.DataFrame(usecase_data)
    st.dataframe(df_usecase, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # SECTION 6: Putting It All Together
    # ============================================
    st.header("6. Putting It All Together: End-to-End ML Workflow")
    
    workflow_steps = [
        "1. Define the problem",
        "2. Gather and clean data",
        "3. Explore data (EDA)",
        "4. Select features",
        "5. Choose an algorithm",
        "6. Train the model",
        "7. Validate the model",
        "8. Test on unseen data",
        "9. Optimize with hyperparameter tuning",
        "10. Deploy the model",
        "11. Monitor and update regularly"
    ]
    
    for step in workflow_steps:
        st.write(f"- {step}")
    
    st.divider()
    
    # ============================================
    # SECTION 7: Comparison Summary
    # ============================================
    st.header("Summary: ML Types at a Glance")
    
    summary_data = {
        "Aspect": ["Learning Type", "Data Requirement", "Goal", "Common Algorithms"],
        "Supervised Learning": [
            "Labeled data",
            "Historical data with outcomes",
            "Predict outcomes",
            "Linear Regression, Random Forest, SVM, Neural Networks"
        ],
        "Unsupervised Learning": [
            "Unlabeled data",
            "No predefined outcomes",
            "Discover hidden patterns",
            "K-Means, PCA, Hierarchical Clustering"
        ],
        "Reinforcement Learning": [
            "Environment interaction",
            "Rewards and penalties",
            "Learn optimal actions",
            "Q-Learning, Deep Q-Networks (DQN), Policy Gradients"
        ]
    }
    
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)
    
    st.divider()
    
    # ============================================
    # SECTION 8: Best Practices
    # ============================================
    st.header("Best Practices for Machine Learning")
    
    st.markdown(
        """
        **1. Start with a Clear Objective**
        - Define the business problem before selecting algorithms
        - Establish success metrics aligned with business goals
        
        **2. Invest in Data Quality**
        - Garbage in, garbage out—clean data is more valuable than complex models
        - Document data sources and preprocessing steps
        
        **3. Split Data Properly**
        - Use train/validation/test splits
        - Maintain temporal order for time-series problems
        
        **4. Avoid Overfitting**
        - Use cross-validation
        - Apply regularization techniques
        - Keep models as simple as possible while meeting performance goals
        
        **5. Choose Metrics Wisely**
        - Accuracy alone is rarely sufficient
        - Consider precision/recall trade-offs for imbalanced datasets
        
        **6. Experiment Systematically**
        - Track all experiments (MLflow, Weights & Biases)
        - Document hyperparameters and results
        
        **7. Think About Deployment Early**
        - Consider inference latency, model size, and scalability
        - Plan for model monitoring and retraining
        """
    )
    
    st.divider()
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Conclusion")
    
    st.write(
        """
        Machine Learning helps organizations unlock insights, automate decisions, 
        and build intelligent systems. The quality of an ML solution depends on:
        
        - **Choice of the right model** for the problem type and data characteristics
        - **Training effectively** with clean, well-prepared data
        - **Evaluating correctly** using appropriate metrics
        - **Tuning for maximum performance** through systematic hyperparameter optimization
        
        As ML continues to evolve, the fundamentals remain constant: understand your data, define clear objectives, 
        and follow a disciplined workflow. Whether you're building a simple classifier or a complex deep learning system, 
        these principles form the foundation of successful machine learning projects.
        """
    )
    
    st.divider()
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Recommended Courses:**
        - [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
        - [DeepLearning.AI](https://www.deeplearning.ai/courses/)
        - [fast.ai Practical Deep Learning](https://www.fast.ai/)
        
        **Key Libraries:**
        - Scikit-learn: Traditional ML algorithms
        - XGBoost / LightGBM: Gradient boosting for tabular data
        - TensorFlow / PyTorch: Deep learning frameworks
        - Hugging Face Transformers: State-of-the-art NLP models
        """
    )