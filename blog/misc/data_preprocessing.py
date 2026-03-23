import streamlit as st
import pandas as pd

TITLE = "Guide to Data Preparation and Processing"
CATEGORY = "misc"
KEYWORDS = ["data cleaning", "feature engineering", "data preprocessing", "machine learning", "ML", "data leakage", "algorithm"]


def show():

    st.title(" Guide to Data Preparation and Processing")
    st.caption("Category: misc | Level: Beginner → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
       In machine learning, "garbage in, garbage out" also holds an immutable truth. While algorithms often capture the spotlight, 
       the true differentiator between a successful model and a failed one lies in the rigorous preparation of data. 
       Data preparation is not merely a preliminary step; it is the foundational engineering upon which all insights are built.
       
       Data preparation is a systematic discipline that forms the backbone of any successful machine learning project. By following a 
       structured approach—cleaning diligently, engineering creatively, encoding appropriately, scaling correctly, and, most 
       importantly, preventing data leakage through strict separation of concerns, practitioners can build models that are not only 
       accurate but also robust and reliable in production.
       
       Skipping these steps might yield a high score on paper, but it is the disciplined adherence to this process that delivers 
       real-world business value. This article outlines a systematic, step-by-step approach to transforming raw, dirty data into a 
       polished, algorithm-ready asset.
        """
    )

    # DATA CLEANING
    # -------------------------
    st.header(" Data Cleaning")

    st.write("The first step is to sanitize the dataset. Raw data is often plagued with inconsistencies, inaccuracies, and gaps. The goal here is to ensure the data is accurate, consistent, and usable.")

    st.subheader("Handling Missing Values")
    st.markdown(
        """
        Missing data may be found in records. The strategy for dealing with it depends on the mechanism of missingness and the volume of data.  	
        
        **Deletion:**
        
        **Listwise Deletion**: Removing entire rows that contain any missing value. This is suitable when the missing data is random and the sample size is large, but it can lead to significant data loss.
        
        **Column Deletion**: Removing a feature entirely if it has a very high percentage of missing values (at least 60%), as imputing such a 
        feature may introduce more noise than signal.
        
        **Imputation:**
        
        **Statistical Imputation**: Filling missing values with the mean, median (for numeric data), or mode (for categorical data).
        
        **Forward/Backward Fill**: Commonly used in time series to propagate the last valid observation.
        
        **Model-Based Imputation**: Using algorithms like K-Nearest Neighbors (KNN) or Iterative Imputer (MICE) to predict missing values based on other features. This is computationally expensive but often yields the best results for complex relationships.
        """
    )

    st.subheader("Correcting Data Types")
    st.markdown(
        """
        Data may arrive with incorrect schema definitions. Numeric values may be loaded as 
        strings (e.g., "1,000" as text) or dates stored as integers.
        
        Convert columns to proper types: int or float for numerical, datetime for date data, 
        and category for categorical variables to reduce memory usage.
        
        **Removing Duplicates**
        
        Duplicate records can affect certain observations, biasing the model.
        Use duplicated() checks to identify and remove duplicate rows. Often, a subset of 
        columns is used to define uniqueness rather than the entire row.
        
        **Handling Outliers**
        
        Outliers are extreme values that can skew statistical measures and destabilize 
        models like linear regression or neural networks.
        """
    )

    st.subheader("Statistical Methods")
    st.markdown(
        """
        **Z-Score:**
        
        Assumes normal distribution. Data points with a Z-score > 3 (or < -3) 
        are flagged as outliers.
        
        **Interquantile Range (IQR):**
        
        A non-parametric method. Any data point below Q1 - 1.5*IQR or above Q3 + 1.5*IQR 
        is considered an outlier.
        
        **Domain Knowledge:**
        
        Sometimes an "outlier" is the most important signal (e.g., fraud detection). 
        Always validate with business context.
        
        **Treatment:**
        
        **Capping/Flooring (Winsorizing):**
        
        Limiting extreme values to a specified percentile (e.g., capping at the 99th percentile).
        
        **Transformation:**
        
        Applying a log or square root transformation can reduce the impact of outliers.
        
        **Separation:** 
        
        Isolating outliers for a separate model (anomaly detection) rather than deleting them.
        """
    )

    # -------------------------
    # FEATURE ENGINEERING
    # -------------------------
    st.header("Feature Engineering")

    st.write("Feature engineering is about creating new columns with calculated data. It is the most creative and iterative process in the pipeline, where raw data is transformed into features that better represent the underlying problem to the predictive model.")

    st.markdown(
        """
        **Domain-Specific Aggregations:**
        
        **For time series:** Rolling averages, lag features, day of the week, hour of the day, or time since the last event.
        
        **For transactional data:** Aggregating user behavior into features like "average purchase value," "frequency of logins," 
        or "recency of last activity" (RFM analysis).
        
        **Binning (Discretization):** Converting continuous variables into categorical bins (e.g., age groups 0-18, 19-35, 36+). 
        This helps models handle non-linear relationships and reduces the impact of sensor noise.
        
        **Feature Splitting:** Decomposing complex fields into atomic features (e.g., splitting "Name" into "First Name" and 
        "Last Name"; parsing "URL" into "Protocol," "Domain," and "Path").

        """
    )

    # -------------------------
    # ENCODING
    # -------------------------
    st.header("Encoding Categorical Data")

    st.markdown(
        """
        Most machine learning algorithms require numerical input. Encoding is the process of converting text categories into numbers.
        
        **Label Encoding (Ordinal):**
        
        Concept: Assign each unique category an integer (e.g., Low=1, Medium=2, High=3).
        
        Use Case: Only suitable for ordinal data where there is a natural ranking (e.g., "Low," "Medium," "High"). 
        Applying this to nominal data (e.g., "Canada," "Mexico," "USA") introduces a false ordinal hierarchy that 
        models may misinterpret.
        
        **One-Hot Encoding (Nominal):**
        
        Concept: Creates binary columns for each category. For a "Color" column with three unique values, it creates three columns:
        is_Red, is_Blue, is_Green.
        
        Use Case: Ideal for nominal data without ranking.
        Constraint: Can lead to the "Curse of Dimensionality" if a feature has hundreds of unique categories.
        
        **Advanced Encodings:**
        
        Target Encoding (Mean Encoding): Replaces a category with the mean of the target variable for that category. 
        Useful for high-cardinality categorical features but prone to overfitting (requires smoothing).
        
        Frequency Encoding: Replaces categories with their count or frequency in the dataset. A good fallback for high-cardinality 
        features where one-hot is infeasible.
        """
    )

    # -------------------------
    # SCALING
    # -------------------------
    st.header("Scaling")

    st.markdown(
        """
        Algorithms that compute distances (e.g., KNN, SVM, K-Means) or rely on gradient descent are sensitive to the magnitude of 
        features. If "Age" (range 0-100) and "Salary" (range 0-100,000) are left unscaled, the model will implicitly treat Salary 
        as the more important feature.
        
        **Standardization (Z-score):**
        
        Result: Transforms features to have a mean of 0 and a standard deviation of 1.
        
        Use Case: Assumes data follows a Gaussian distribution. Best for algorithms like Linear Regression, Logistic Regression, 
        and Neural Networks.
        
        **Normalization (Min-Max Scaling):**
        
        Result: Scales features to a fixed range, usually [0, 1].
        Use Case: Best for algorithms that do not assume any distribution of the data, such as K-Nearest Neighbors or Convolutional
        Neural Networks (CNNs) where pixel values need to be bounded.
        """
    )

    # -------------------------
    # DATA SPLITTING
    # -------------------------
    st.header(" Data Splitting")

    st.markdown(
        """
        To evaluate a model's ability to generalize to unseen data, we must partition the dataset. This is done before any scaling 
        or encoding to prevent data leakage.
        
        1.	Training Set (70%-80%): The data used to train the model.
        
        2.	Validation Set (20%-30%): Used during model development for hyperparameter tuning and model selection. 
        The model sees this data indirectly through the tuning process, but does not learn weights from it.
        
        3.	Test Set (10%-20%): A completely isolated set used only once at the very end to provide an unbiased final 
        evaluation of the model’s performance.
        
        Always split BEFORE scaling or encoding to prevent leakage.
        """
    )

    # -------------------------
    # VALIDATION
    # -------------------------
    st.header("Evaluation and Validation Techniques")

    st.markdown(
        """
        To ensure the model is robust and not simply memorizing the training data, we use specific validation techniques.
        
        **Cross-Validation (K-Fold):**
        Instead of a single static train/validation split, K-Fold splits the training data into n subsets. The model is trained n 
        times, each time using a different fold as the validation set and the remaining n-1 as the training set. The performance 
        is averaged.
        
        It reduces variance in performance estimation and ensures the model is stable across different data subsets.
        Stratification: When splitting, ensure that the proportion of target classes is preserved across training, validation, 
        and test sets. 
        
        Crucial for imbalanced classification problems to prevent the validation set from missing minority classes 
        entirely.
        """
    )

    # -------------------------
    # DATA LEAKAGE
    # -------------------------
    st.header(" Prevent Data Leakage")

    st.markdown(
        """
        Data leakage is the most dangerous and subtle pitfall in data preparation. It occurs when information from outside the 
        training dataset (specifically, the validation or test sets) "leaks" into the training process, causing optimistic and 
        non-generalizable results.
        
        **Common Leakage Scenarios and Prevention:**
        
        **Scaling Leakage:**
        
        Wrong: Fit MinMaxScaler on the entire dataset (train + test), then split.
        
        Correct: Fit the scaler (calculate mean, min, max) only on the training set. Transform the training set using the fitted 
        scaler. Transform the test set using the same fitted scaler (do not re-fit).
        
        **Imputation Leakage:**
        
        Wrong: Computing the median of a column using the entire dataset.
        Correct: Compute the median using the training set only. Use that median to fill missing values in both the training and 
        test sets.
        
        **Feature Engineering Leakage:**
        
        Wrong: Using global statistics (e.g., average revenue of all users) to create a feature before splitting.
        Correct: If creating aggregated features (like "mean purchase per user"), compute these aggregates using only the training 
        data, then join these pre-computed aggregates to the validation and test sets.
        """
    )
    
    # -------------------------
    # ALGORITHM CHOICE
    # -------------------------
    st.header(" Choosing the Right Algorithm")
    
    st.markdown(
        """
        The final choice of algorithm depends on the prepared data and the insight sought. The preprocessing steps taken 
        (e.g., scaling, encoding) should align with the algorithm’s assumptions.
        
        **Linear Models**
        - Require scaling and encoding
        
        **Tree-Based Models**
        - No scaling needed
        - Handle non-linearity well
        
        **Distance-Based Models (KNN, K-Means)**
        - Require normalization
        
        **Neural Networks**
        - Require scaling
        - Work well with large data
        """
    )
    st.title("Algorithm Categories & Data Preparation Requirements")
    st.write("This table summarizes different machine learning algorithm categories and their data preparation needs.")

    # Create DataFrame
    data = {
        "Algorithm Category": [
            "Linear Models",
            "Tree-Based Models",
            "Distance-Based Models",
            "Neural Networks"
        ],
        "Models": [
            "Linear Regression, Logistic Regression, SVM",
            "Random Forest, XGBoost, LightGBM",
            "KNN, K-Means, DBSCAN",
            "MLP, CNNs, RNNs"
        ],
        "Data Preparation Requirements": [
            "Strict: Requires scaled data (Standardization), handling of multicollinearity and encoded categorical variables (One-Hot).",
            "Flexible: No scaling required. Handles non-linear relationships automatically.",
            "Strict: Requires scaling (Normalization preferred). Sensitive to the curse of dimensionality.",
            "Strict: Requires scaling (Standardization or Normalization). Often requires target encoding."
        ]
    } 

    df = pd.DataFrame(data)

    # Display table
   # st.dataframe(df, use_container_width=True)
    st.table(df)

    # -------------------------
    # SUMMARY
    # -------------------------
    st.header("Data Preparation Workflow")

    st.code(
        """
Clean → Transform → Encode → Scale → Split 
→ Validate → Train → Evaluate
        """,
        language="text"
    )

    st.success(
        "Mastering data preparation is the fastest way to improve your machine learning results."
    )