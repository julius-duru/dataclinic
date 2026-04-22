import streamlit as st
import pandas as pd

TITLE = "Complete Guide to Handling Missing Data"
CATEGORY = "data_engineering"
KEYWORDS = ["missing data", "data imputation", "data cleaning", "KNN imputation", "MICE", "data preprocessing", "feature engineering", "missing value handling", "data quality", "ML preprocessing"]


def show():

    st.title("Complete Guide to Handling Missing Data")
    st.caption("Category: data_engineering | Level: Beginner → Advanced")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        Missing data is in data science. Whether you are working with a small CSV file 
        or a massive production pipeline, you will encounter incomplete records. How you handle these missing values can 
        make the difference between a robust, trustworthy model and one that fails.
        
        This guide covers everything from fundamental concepts to advanced techniques, ensuring that both 
        beginners and experienced practitioners can find actionable insights.
        
        **Why Missing Data Matters:**
        - **Algorithm Failure:** Most machine learning algorithms cannot handle missing values natively
        - **Bias Introduction:** Improper handling can skew your analysis and lead to incorrect conclusions
        - **Information Loss:** Deleting data indiscriminately means losing potentially valuable patterns
        - **Pattern Recognition:** Sometimes, missing data itself is signal pointing to some anomalies
        """
    )
    
    # ============================================
    # SECTION 0: Understanding the Nature of Missing Data
    # ============================================
    st.header("Understanding the Nature of Missing Data")
    
    st.write(
        """
        The best approach depends on why data is missing. Statisticians classify missingness into three types:
        """
    )
    
    missingness_data = {
        "Type": ["MCAR (Missing Completely at Random)", "MAR (Missing at Random)", "MNAR (Missing Not at Random)"],
        "Description": [
            "Missingness has no relationship with any data",
            "Missingness depends on observed data",
            "Missingness depends on the missing value itself"
        ],
        "Example": [
            "A sensor randomly fails to record",
            "Men are more likely to skip a survey question about emotions",
            "High-income individuals refuse to report salary"
        ],
        "Implication": [
            "Safe to delete or use simple imputation",
            "Can be modeled using other features",
            "Most challenging; requires domain expertise"
        ]
    }
    df_missingness = pd.DataFrame(missingness_data)
    st.dataframe(df_missingness, use_container_width=True)
    
    st.write(
        """
        **For beginners:** Start by asking whether missingness seems random or systematic.  
        **For advanced readers:** Use statistical tests (like Little's MCAR test) and visualizations to formally assess missingness patterns.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 1: Deletion Methods
    # ============================================
    st.header("1. Deletion Methods")
    
    st.write(
        """
        When missing data is minimal or concentrated, deletion is the simplest approach.
        """
    )
    
    st.subheader("a. Listwise Deletion (Drop Rows)")
    st.write(
        """
        Remove any row containing a missing value.
        
        **Best when:** Missing values are few (typically <5%) and MCAR.  
        **Risk:** Can discard up to 30–50% of data if multiple features have missing values.  
        **Pro tip:** In pandas, `df.dropna()` is your friend—but always check the shape before and after.
        """
    )
    
    st.subheader("b. Column Deletion")
    st.write(
        """
        Remove an entire feature from your dataset.
        
        **Best when:** A column has >70–80% missing values, or the feature is non-essential.  
        **Risk:** You may lose predictive power if the feature was important.  
        **Pro tip:** Consider the trade-off—sometimes a column with 70% missing data still contains valuable signal for the remaining 30%.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 2: Simple Imputation
    # ============================================
    st.header("2. Simple Imputation")
    
    st.write(
        """
        Simple imputation replaces missing values with statistical summaries. It's fast, easy to implement, 
        and often sufficient for baseline models.
        """
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Mean Imputation")
        st.write(
            """
            Replace missing values with the arithmetic mean.
            
            **Works for:** Approximately normal distributions.  
            **Sensitive to:** Outliers — a single extreme value can pull the mean significantly.  
            **For beginners:** Use only when you have confirmed your data is symmetric.
            """
        )
        
        st.subheader("Mode Imputation")
        st.write(
            """
            Replace missing values with the most frequent value.
            
            **Best for:** Categorical features.  
            **Risk:** Can artificially inflate the frequency of the modal class.  
            **Pro tip:** For high-cardinality categorical features, consider grouping rare categories before mode imputation.
            """
        )
    
    with col2:
        st.subheader("Median Imputation")
        st.write(
            """
            Replace missing values with the median (the 50th percentile).
            
            **Best for:** Skewed data, datasets with outliers, or when distribution is unknown.  
            **Robust:** Unaffected by extreme values.  
            **For advanced readers:** Median imputation preserves rank-order relationships better than mean imputation.
            """
        )
        
        st.subheader("Constant Imputation")
        st.write(
            """
            Replace missing values with a fixed value outside the normal range (e.g., -999, \"Unknown\").
            
            **Useful when:** Missingness itself is informative, or when you want certain models (like tree-based) to learn a separate branch for missing values.  
            **For advanced readers:** Some frameworks (like XGBoost) handle missing values natively—constant imputation may interfere with that capability.
            """
        )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 3: Time Series-Specific Methods
    # ============================================
    st.header("3. Time Series-Specific Methods")
    
    st.write(
        """
        Time series data has a natural order, making specialized techniques appropriate.
        """
    )
    
    st.subheader("a. Forward Fill (ffill)")
    st.write(
        """
        Carry the last observed value forward.
        
        **Best for:** Data that changes slowly or remains constant between observations.  
        **Not suitable for:** Erratic or frequently changing values.
        """
    )
    
    st.subheader("b. Backward Fill (bfill)")
    st.write(
        """
        Use the next available value to fill preceding gaps.
        """
    )
    
    st.subheader("c. Interpolation")
    st.write(
        """
        Estimate missing values by fitting a function through observed points.
        
        | Technique | Description |
        |-----------|-------------|
        | **Linear interpolation** | Straight line between known points |
        | **Polynomial interpolation** | Curved fit using higher-degree polynomials |
        | **Spline interpolation** | Piecewise polynomial for smoother transitions |
        
        **Best for:** Continuous signals like sensor readings, stock prices, or temperature data.  
        **For advanced readers:** Consider the trade-off between interpolation accuracy and overfitting—spline interpolation can introduce artificial oscillations if not properly constrained.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 4: Advanced Imputation Techniques
    # ============================================
    st.header("4. Advanced Imputation Techniques")
    
    st.write(
        """
        When simple methods fall short, advanced techniques leverage relationships within your data to produce 
        more accurate imputations.
        """
    )
    
    st.subheader("a. k-Nearest Neighbors (KNN) Imputation")
    st.write(
        """
        For each sample with missing values, find the k most similar complete samples and impute using their 
        values (typically the mean or median).
        
        **Strengths:** Non-parametric, works with mixed data types, captures local structure.  
        **Weaknesses:** Computationally expensive for large datasets; sensitive to feature scaling.  
        **Implementation:** `KNNImputer` in scikit-learn.
        """
    )
    
    st.subheader("b. Multivariate Imputation by Chained Equations (MICE)")
    st.write(
        """
        Also known as Fully Conditional Specification (FCS). MICE iteratively models each feature with missing 
        values using all other features, cycling through multiple times to converge on stable imputations.
        
        **Strengths:** Handles complex relationships; preserves uncertainty through multiple imputations.  
        **Weaknesses:** Computationally heavy; requires careful convergence diagnostics.  
        **For advanced readers:** Use MICE when you need statistically valid inference (e.g., confidence intervals) 
        rather than just a single completed dataset for prediction.
        """
    )
    
    st.subheader("c. Machine Learning-Based Imputation")
    st.write(
        """
        Train supervised models to predict missing values using other features as inputs.
        
        **Common algorithms:**
        - **Linear Regression:** Simple, interpretable, but assumes linear relationships
        - **Random Forest:** Captures non-linear relationships; robust to outliers
        - **XGBoost/LightGBM:** State-of-the-art for tabular data; handles mixed data types well
        
        **Strengths:** Can achieve high accuracy when relationships exist.  
        **Weaknesses:** Risk of overfitting; computationally intensive.  
        **Best practice:** Use cross-validation when training imputation models to avoid leaking information from the test set.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 5: Domain-Specific Imputation
    # ============================================
    st.header("5. Domain-Specific Imputation")
    
    st.write(
        """
        Sometimes the best imputation comes from real-world knowledge, not statistical formulas.
        
        **Examples:**
        - **Missing salary:** Impute based on job title, years of experience, and geographic location
        - **Missing gender:** Use name databases or existing demographic patterns
        - **Missing medical readings:** Use clinical guidelines or expected ranges for similar patients
        - **Missing product category:** Infer from product description or SKU patterns
        
        **Why it matters:** Domain-specific imputation often yields values that are not only statistically plausible 
        but also contextually correct.  
        **For advanced readers:** Combine domain knowledge with machine learning by using domain-derived features 
        as inputs to predictive imputation models.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 6: Adding Missingness Indicators
    # ============================================
    st.header("6. Adding Missingness Indicators")
    
    st.write(
        """
        Instead of imputing, or in addition to imputation, you can create a binary feature that flags whether a 
        value was originally missing.
        """
    )
    
    st.code("df['age_was_missing'] = df['age'].isnull().astype(int)", language="python")
    
    st.write(
        """
        **Why it works:** Models can learn whether missingness itself is predictive.  
        **Especially useful for:** MAR and MNAR scenarios where missingness carries signal.  
        **For beginners:** Always add missingness indicators when using simple imputation — it gives your model 
        the chance to adjust.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 7: Probabilistic and Bayesian Imputation
    # ============================================
    st.header("7. Probabilistic and Bayesian Imputation")
    
    st.write(
        """
        For the highest level of sophistication, probabilistic methods treat imputed values as uncertain 
        quantities to be estimated within a statistical framework.
        """
    )
    
    st.subheader("a. Expectation-Maximization (EM) Imputation")
    st.write(
        """
        Iteratively estimates missing values (E-step) and updates parameters (M-step) until convergence.
        
        **Strengths:** Produces maximum likelihood estimates; theoretically grounded.  
        **Weaknesses:** Assumes multivariate normality; can be complex to implement.
        """
    )
    
    st.subheader("b. Bayesian Imputation")
    st.write(
        """
        Treats missing values as parameters with prior distributions, sampling from posterior distributions to 
        generate plausible imputed values.
        
        **Strengths:** Captures uncertainty naturally; works well with small datasets.  
        **Weaknesses:** Computationally intensive; requires expertise in Bayesian methods.  
        **For advanced readers:** Multiple imputation (MI) combines the benefits of probabilistic methods—you 
        create several imputed datasets, analyze each, and pool results to account for imputation uncertainty.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION 8: Best Practices and Decision Framework
    # ============================================
    st.header("8. Best Practices and Decision Framework")
    
    tab1, tab2 = st.tabs(["For Beginners", "For Advanced Practitioners"])
    
    with tab1:
        st.write(
            """
            ### A Simple Workflow
            
            1. **Assess proportion:** If <5% missing and MCAR → drop rows
            2. **For numerical features:** Check skewness → use median if skewed, mean if normal
            3. **For categorical features:** Use mode imputation
            4. **For time series:** Use forward fill or linear interpolation
            5. **Always add missingness indicators**
            """
        )
    
    with tab2:
        st.write(
            """
            ### A Refined Approach
            
            1. **Characterize missingness:** Use visualizations (missingno library), statistical tests (Little's MCAR), 
               and domain knowledge to classify as MCAR, MAR, or MNAR
            2. **Start with baseline:** Simple imputation + missingness indicators often performs surprisingly well
            3. **Experiment with advanced methods:** Compare KNN, MICE, and ML-based imputation using cross-validation
            4. **Consider downstream task:** 
               - For inference (understanding relationships) → use MICE or multiple imputation
               - For prediction (maximizing accuracy) → simple imputation with indicators or ML-based imputation
            5. **Validate:** Always test your imputation strategy on a holdout set with artificially introduced missingness
            """
        )
    
    st.markdown("---")
    
    # ============================================
    # SUMMARY TABLE
    # ============================================
    st.header("Summary Table: Methods at a Glance")
    
    summary_data = {
        "Method": [
            "Drop rows", "Drop columns", "Mean imputation", "Median imputation", 
            "Mode imputation", "Forward/Backward fill", "Interpolation", 
            "KNN imputation", "MICE", "ML regression", 
            "Missingness indicator", "Probabilistic"
        ],
        "Category": [
            "Deletion", "Deletion", "Simple", "Simple",
            "Simple", "Time series", "Time series",
            "Advanced", "Advanced", "Advanced",
            "Augmentation", "Advanced"
        ],
        "Best For": [
            "Few missing values, MCAR", ">60-80% missing, non-essential", "Normal distribution",
            "Skewed data, outliers", "Categorical features", "Sequential data", "Continuous signals",
            "Mixed data types, local structure", "Complex relationships, inference", "Predictable patterns",
            "MAR/MNAR scenarios", "Uncertainty quantification"
        ],
        "Weakness": [
            "Loss of data", "May lose important signal", "Sensitive to outliers",
            "May hide structure", "Distorts frequency", "May propagate errors", "Not for categorical data",
            "Slow for large datasets", "Computationally heavy", "Risk of overfitting",
            "Adds dimensionality", "Complex, intensive"
        ]
    }
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True)
    
    st.markdown("---")
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header(" Conclusion")
    
    st.write(
        """
        There is no universal "best" method — only the method best suited to your data, your problem, and your constraints.
        
        **For beginners:** Start simple. Median imputation for numerical data and mode for categorical data, 
        combined with missingness indicators, will serve you well in most cases.
        
        **For advanced readers:** Dive deeper. Characterize your missingness, experiment with MICE and ML-based 
        approaches, and consider probabilistic methods when uncertainty matters. Remember that imputation is 
        part of your modeling pipeline—validate it as rigorously as you validate your models.
        
        The goal is not to perfectly reconstruct missing values — that is often impossible. The goal is to create 
        a dataset that allows your analysis or model to perform reliably and generalize well to new data. 
        With the techniques outlined here, you are well-equipped to achieve that goal.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # ADDITIONAL RESOURCES
    # ============================================
    st.header("Additional Resources")
    
    st.markdown(
        """
        **Python Libraries:**
        - [missingno](https://github.com/ResidentMario/missingno): Visualize missing data patterns
        - [scikit-learn's impute module](https://scikit-learn.org/stable/modules/impute.html): KNNImputer, SimpleImputer
        - [fancyimpute](https://github.com/iskandr/fancyimpute): Advanced imputation algorithms
        - [statsmodels](https://www.statsmodels.org/): MICE implementation
        
        **Further Reading:**
        - [scikit-learn Guide: Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html)
        - [Multiple Imputation by Chained Equations (MICE)](https://stefvanbuuren.name/publications/MICE%20V1.0%20Manual%20TNO00038%202000.pdf)
        
        **Visualization Tools:**
        - Missingno heatmaps and dendrograms for missing pattern analysis
        - Pandas profiling reports for automated missing data detection
        """
    )