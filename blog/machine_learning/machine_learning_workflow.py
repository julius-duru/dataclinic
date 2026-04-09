import streamlit as st
import pandas as pd

TITLE = "Basic Steps in Machine Learning from Data to Evaluation"
CATEGORY = "machine_learning"
KEYWORDS = [
    "pandas", "numpy", "data preprocessing", "missing values", "machine learning workflow",
    "correlation", "outliers", "train-test split", "model serialization",
    "pickle", "joblib", "classification metrics", "DVC", "experiment tracking"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Beginner → Intermediate")
    st.markdown("---")

    # INTRO
    st.write(
        """
        This article is for: aspiring data scientists, ML beginners, and practitioners who want a structured, production‑aware workflow.  
        **Core themes**: data evaluation, missing value imputation, feature selection, model serialization, metrics, and experiment tracking.

        **Why follow a step‑by‑step ML workflow?**  
        - **Reproducibility** – Every step is documented and can be repeated.  
        - **Reliability** – Avoid common pitfalls like data leakage or improper validation.  
        - **Production readiness** – Save and load models, compare experiments, and track changes.

        > A clean workflow turns a chaotic notebook into a maintainable ML pipeline.
        """
    )
    st.markdown("---")

    # 1. IMPORT LIBRARIES
    st.header("1. Import Essential Libraries")
    st.code(
        """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_absolute_error, mean_squared_error, roc_auc_score,
    confusion_matrix, roc_curve, calibration_curve
)
import joblib
import dvc
        """,
        language="python"
    )
    st.info(" **Tip**: Use `joblib` for scikit‑learn models and `pickle` for generic Python objects. DVC will help with data versioning later.")
    st.markdown("---")

    # 2. GET DATASET
    st.header("2. Load the Dataset (CSV / Excel)")
    st.code(
        """
# CSV
df = pd.read_csv('data/customer_churn.csv')

# Excel
# df = pd.read_excel('data/sales_data.xlsx', sheet_name='Sheet1')

print(f"Shape: {df.shape}")
df.head()
        """,
        language="python"
    )
    st.markdown("---")

    # 3. EVALUATE DATA
    st.header("3. Evaluate Data: Distribution, Types, Missing Values, Consistency")
    st.write(
        """
        Before any cleaning, inspect the raw data thoroughly:
        - **Data types** – Are integers stored as strings? Dates as objects?
        - **Missing values** – Which columns have nulls and what percentage?
        - **Distribution** – Is the target balanced? Are numerical features skewed?
        - **Consistency** – Do categorical values have typos (e.g., 'Male' vs 'male')?
        """
    )
    st.code(
        """
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Distribution of target variable
sns.countplot(x='churn', data=df)
plt.title('Target Distribution')
plt.show()
        """,
        language="python"
    )
    st.markdown("---")

    # 4. HANDLE MISSING DATA
    st.header("4. Choose the Best Method to Fill Missing Data")
    st.write(
        """
        The imputation strategy depends on the feature type and its distribution.
        """
    )
    missing_table = pd.DataFrame({
        "Method": ["Mean", "Median", "Mode", "Forward Fill (time series)"],
        "When to use": [
            "Numerical, normally distributed, no outliers",
            "Numerical, skewed or with outliers",
            "Categorical features",
            "Sequential data with trend"
        ],
        "Example (pandas)": [
            "`df['age'].fillna(df['age'].mean())`",
            "`df['income'].fillna(df['income'].median())`",
            "`df['city'].fillna(df['city'].mode()[0])`",
            "`df['price'].fillna(method='ffill')`"
        ]
    })
    st.dataframe(missing_table, use_container_width=True)
    st.code(
        """
# Using SimpleImputer from sklearn (robust for pipelines)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')   # or 'mean', 'most_frequent'
df[['income']] = imputer.fit_transform(df[['income']])
        """,
        language="python"
    )
    st.markdown("---")

    # 5. CORRELATION, OUTLIERS, REMOVE UNNECESSARY FEATURES
    st.header("5. Correlation, Outliers & Feature Removal")
    st.subheader("Correlation Analysis")
    st.code(
        """
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

# Drop one of two highly correlated features (e.g., > 0.9)
df.drop('total_bill', axis=1, inplace=True)
        """,
        language="python"
    )
    st.subheader("Outlier Treatment (IQR method)")
    st.code(
        """
Q1 = df['transaction_amount'].quantile(0.25)
Q3 = df['transaction_amount'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df['transaction_amount'] = df['transaction_amount'].clip(lower, upper)
        """,
        language="python"
    )
    st.subheader("Remove Unnecessary Features")
    st.code(
        "df.drop(['customer_id', 'timestamp', 'row_number'], axis=1, inplace=True)",
        language="python"
    )
    st.markdown("---")

    # 6. SEPARATE DEPENDENT AND INDEPENDENT FEATURES
    st.header("6. Separate Dependent (Target) and Independent Features")
    st.code(
        """
X = df.drop('churn', axis=1)   # features
y = df['churn']                 # target
        """,
        language="python"
    )
    st.markdown("---")

    # 7. TRAIN-TEST SPLIT & HYPERPARAMETER TUNING
    st.header("7. Split Dataset & Hyperparameter Tuning")
    st.code(
        """
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Hyperparameter tuning with GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
}
rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='f1')
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
        """,
        language="python"
    )
    st.success(" Always use `stratify=y` for classification to preserve class balance.")
    st.markdown("---")

    # 8. CHOOSE CLASSIFIER & CREATE MODEL
    st.header("8. Choose a Classifier and Create the Model")
    st.write(
        """
        The choice depends on your data size, interpretability needs, and performance requirements.
        Common classifiers:
        - **Logistic Regression** – baseline, linear
        - **Random Forest** – robust, handles non‑linearity
        - **XGBoost / LightGBM** – high performance, often winning competitions
        - **Neural Networks** – for very large / complex data
        """
    )
    st.code(
        """
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)
        """,
        language="python"
    )
    st.markdown("---")

    # 9. SAVE SERIALIZED MODEL
    st.header("9. Save the Serialized Model (.pkl, .joblib, .h5, .onnx)")
    serial_table = pd.DataFrame({
        "Format": [".pkl (pickle)", ".joblib", ".h5", ".onnx"],
        "Best for": [
            "Small Python objects, custom classes",
            "Scikit‑learn, large NumPy arrays",
            "Keras / TensorFlow deep learning models",
            "Cross‑platform / cross‑language inference"
        ],
        "Pros / Cons": [
            "Built‑in, but slow & insecure for untrusted sources",
            "Faster, smaller files, preferred for sklearn",
            "Standard for DL, not for sklearn",
            "Open standard, portable, but conversion overhead"
        ]
    })
    st.dataframe(serial_table, use_container_width=True)
    st.code(
        """
import joblib
joblib.dump(best_model, 'models/churn_model.joblib')

# Alternative pickle
import pickle
with open('models/churn_model.pkl', 'wb') as f:
    pickle.dump(best_model, f)
        """,
        language="python"
    )
    st.info(" **Recommendation**: Use `joblib` for all scikit‑learn based models. For deep learning, rely on framework‑specific save methods (`model.save()` for TensorFlow).")
    st.markdown("---")

    # 10. CALCULATE METRICS
    st.header("10. Calculate Performance Metrics")
    st.write(
        """
        **Classification metrics** (when target is discrete):
        - **Accuracy** – overall correctness (not for imbalanced data)
        - **Precision** – “of predicted positives, how many are correct?”
        - **Recall** – “of actual positives, how many did we catch?”
        - **F1‑score** – harmonic mean of precision and recall
        - **AUC‑ROC** – ability to separate classes

        **Regression metrics** (when target is continuous):
        - **MAE** – mean absolute error
        - **RMSE** – root mean squared error (penalizes large errors)
        """
    )
    st.code(
        """
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, roc_auc_score
import numpy as np

y_pred = best_model.predict(X_test)
y_proba = best_model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)

# For regression tasks (example)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"Accuracy: {accuracy:.4f}, F1: {f1:.4f}, AUC: {auc:.4f}")
        """,
        language="python"
    )
    st.markdown("---")

    # 11. LOAD MODEL & PREDICT ON NEW DATA
    st.header("11. Load the Saved Model and Perform Predictions")
    st.code(
        """
# Load model
loaded_model = joblib.load('models/churn_model.joblib')

# New data (must have same features as X_train)
new_data = pd.DataFrame({
    'age': [35, 42],
    'income': [55000, 78000],
    'usage_frequency': [12, 5]
})
predictions = loaded_model.predict(new_data)
probabilities = loaded_model.predict_proba(new_data)

print(predictions, probabilities)
        """,
        language="python"
    )
    st.markdown("---")

    # 12. INTEGRATE MLOPS TOOLS FOR COMPARISON
    st.header("12. Integrate MLOps Tools: DVC, LakeFS, Pachyderm")
    st.write(
        """
        When you run multiple experiments (e.g., changing `n_estimators`), you need to track **which data + code + hyperparameters** produced which model. Tools like DVC, LakeFS, and Pachyderm bring Git‑like versioning to data and models.
        """
    )
    st.code(
        """
# Initialize DVC and track data
dvc init
dvc add data/customer_churn.csv
git add data/customer_churn.csv.dvc .gitignore

# Define pipeline in dvc.yaml
stages:
  train:
    cmd: python train.py --estimators 200
    deps:
      - data/customer_churn.csv
      - train.py
    outs:
      - models/model.joblib
    metrics:
      - metrics.json

# Run experiment
dvc exp run --set-param train.estimators=200
dvc exp show
        """,
        language="bash"
    )
    st.info("🔁 With DVC, every experiment is reproducible and comparable. LakeFS adds versioning at the data lake level, while Pachyderm automates pipelines based on data changes.")
    st.markdown("---")

    # 13. CHANGE PARAMETERS & TRACK EXPERIMENTS
    st.header("13. Change Parameters, Track Experiments, and Compare Results")
    st.write(
        """
        For each experiment, you should log:
        - **Validation metrics** (accuracy, F1, AUC, etc.)
        - **Confusion matrices**
        - **Error analysis** (where does the model fail?)
        - **ROC curves**
        - **Calibration curves** (for probabilistic models)
        """
    )
    st.code(
        """
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, calibration_curve

# Confusion matrix
ConfusionMatrixDisplay.from_estimator(best_model, X_test, y_test)
plt.title("Confusion Matrix")
plt.show()

# ROC curve
RocCurveDisplay.from_estimator(best_model, X_test, y_test)
plt.title("ROC Curve")
plt.show()

# Calibration curve
prob_true, prob_pred = calibration_curve(y_test, y_proba, n_bins=10)
plt.plot(prob_pred, prob_true, marker='o', label='Model')
plt.plot([0, 1], [0, 1], '--', label='Perfect')
plt.xlabel('Mean predicted probability')
plt.ylabel('Fraction of positives')
plt.legend()
plt.title('Calibration Curve')
plt.show()
        """,
        language="python"
    )
    st.success("📊 **Pro tip**: Use `MLflow` or `Weights & Biases` to automatically log all these plots and metrics. Then compare experiments with a single command.")
    st.markdown("---")

    # CONCLUSION & BEST PRACTICES
    st.header("Conclusion & Best Practices")
    st.write(
        """
        Mastering these basic steps turns ad‑hoc analysis into a repeatable, production‑ready workflow.

        **Key takeaways for every ML project:**
        1. **Always evaluate raw data** – missing values, types, distributions.
        2. **Choose imputation wisely** – median for skewed numeric, mode for categorical.
        3. **Remove redundant features** – high correlation or no predictive power.
        4. **Split before any preprocessing** – avoid data leakage.
        5. **Serialize with joblib** for scikit‑learn, and always version the model.
        6. **Use multiple metrics** – one number never tells the whole story.
        7. **Track experiments** – DVC + MLflow are your friends.
        8. **Visualise everything** – confusion matrices, ROC, calibration curves.

        **Next actions for you:**
        - Take a notebook you have written and refactor it into a script following the steps above.
        - Save the final model with `joblib` and write a short script to load it and predict on new data.
        - Install DVC, add your dataset, and run two experiments with different hyperparameters. Compare the results using `dvc exp show`.

        > A clean workflow is the foundation of reliable machine learning. Invest time in the basics – it will pay back tenfold when you move to production.
        """
    )
    st.markdown("---")

    # RESOURCES
    st.header("Best Resources to Go Deeper")
    st.markdown(
        """
        **Serialization & Model Saving**  
        - [Joblib documentation](https://joblib.readthedocs.io)  
        - [Python pickle (official)](https://docs.python.org/3/library/pickle.html)

        **Missing Data & Preprocessing**  
        - [Scikit‑learn Imputation guide](https://scikit-learn.org/stable/modules/impute.html)

        **Metrics**  
        - [Scikit‑learn metrics API](https://scikit-learn.org/stable/modules/model_evaluation.html)

        **Experiment Tracking**  
        - [DVC](https://dvc.org) – Data and model versioning  
        - [MLflow](https://mlflow.org) – Full lifecycle management  
        - [Evidently AI](https://evidentlyai.com) – Drift and performance monitoring

        **Books**  
        - "Introduction to Machine Learning with Python" by Andreas C. Müller & Sarah Guido  
        - "Hands‑On Machine Learning with Scikit‑Learn, Keras, and TensorFlow" by Aurélien Géron
        """
    )
    st.markdown("---")
    st.caption("© 2026 | Basic Steps in Machine Learning | Build workflows that are clean, reproducible, and ready for production.")

