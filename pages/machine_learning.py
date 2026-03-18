import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="Machine Learning", layout="wide")

# ------------------------------------------------
# Top Navigation Links
# ------------------------------------------------

nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns(7)

with nav1:
    st.page_link("app.py", label="🏠 Home", use_container_width=True)

with nav2:
    st.page_link("pages/beginner.py", label="Beginner", use_container_width=True)

with nav3:
    st.page_link("pages/proficient.py", label="Proficient", use_container_width=True)

with nav4:
    st.page_link("pages/advanced.py", label="Advanced", use_container_width=True)

with nav5:
    st.page_link("pages/machine_learning.py", label="ML", use_container_width=True)

with nav6:
    st.page_link("pages/projects.py", label="Projects", use_container_width=True)

with nav7:
    st.page_link("pages/career_soft_skills.py", label="Soft Skills", use_container_width=True)

st.markdown("---")


# ------------------------------------------------
# Page Content
# ------------------------------------------------

def show():

    # ---------------------------------------
    # Page Title
    # ---------------------------------------

    st.title("🤖 Machine Learning")

    st.write("Master predictive modeling, algorithms, and real-world AI applications.")

    # ---------------------------------------
    # Hero Image
    # ---------------------------------------

    st.image(
        "images/machine_learning.jpg",
        use_container_width=True
    )

    st.markdown("""
**Machine Learning Path** is designed for learners who want to develop the ability to **build predictive models, analyze patterns in data, and deploy intelligent systems**.

Machine learning enables organizations to **predict outcomes, automate decisions, and uncover hidden insights from large datasets**.
""")

    st.markdown("---")

    # ------------------------------------------------
    # Embedded Navigation Links
    # ------------------------------------------------

    st.subheader("Explore Other Learning Paths")

    colA, colB, colC = st.columns(3)

    with colA:
        st.page_link("pages/beginner.py", label="🟢 Beginner Path")

    with colB:
        st.page_link("pages/proficient.py", label="🟡 Proficient Path")

    with colC:
        st.page_link("pages/advanced.py", label="🔴 Advanced Path")

    st.markdown("---")

    # ---------------------------------------
    # Learning Modules
    # ---------------------------------------

    st.header("Machine Learning Modules")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### 🧠 Module 1: Introduction to Machine Learning

• What is machine learning  
• Types of ML: Supervised, Unsupervised, Reinforcement  
• ML applications in business and science  
• ML workflow from data collection to deployment
""")

        st.markdown("""
### 📊 Module 2: Data Preparation & Feature Engineering

• Data cleaning and preprocessing  
• Handling missing values and outliers  
• Feature scaling and encoding  
• Splitting datasets into training and testing sets
""")

        st.markdown("""
### 🐍 Module 3: Python Libraries for Machine Learning

• **NumPy** and **Pandas** – Data manipulation  
• **Scikit-learn** – Machine learning algorithms  
• **Matplotlib / Seaborn** – Data visualization  
• **Joblib / Pickle** – Saving trained models
""")

    with col2:

        st.markdown("""
### 📈 Module 4: Supervised Learning

• Linear and logistic regression  
• Decision trees and random forests  
• Support vector machines (SVM)  
• Model evaluation: accuracy, precision, recall, F1-score
""")

        st.markdown("""
### 🔍 Module 5: Unsupervised Learning

• Clustering: K-Means and hierarchical clustering  
• Dimensionality reduction: PCA and t-SNE  
• Anomaly detection  
• Pattern discovery in large datasets
""")

        st.markdown("""
### 🤖 Module 6: Advanced Machine Learning

• Ensemble learning (Bagging, Boosting)  
• Gradient boosting models (XGBoost, LightGBM)  
• Time series forecasting  
• Introduction to neural networks and deep learning
""")

    st.markdown("---")

    # ---------------------------------------
    # Recommended Tools
    # ---------------------------------------

    st.header("Machine Learning Tools")

    st.markdown("""
• **Python** – Primary language for machine learning workflows  
• **Scikit-learn** – Core machine learning library  
• **TensorFlow / Keras / PyTorch** – Deep learning frameworks  
• **Pandas / NumPy** – Data manipulation and analysis  
• **Jupyter Notebook / VS Code** – Development environments  
• **Matplotlib / Seaborn / Plotly** – Visualization tools
""")

    st.markdown("---")

    # ---------------------------------------
    # Projects
    # ---------------------------------------

    st.header("Machine Learning Projects")

    st.markdown("""
Hands-on practice is essential for mastering machine learning.

Example projects include:

• House price prediction using regression models  
• Customer churn prediction for telecom companies  
• Market segmentation using clustering algorithms  
• Sentiment analysis on social media data  
• Sales forecasting using time series models  
• Recommendation systems for e-commerce platforms
""")

    st.markdown("---")

    # ------------------------------------------------
    # Continue Learning
    # ------------------------------------------------

    st.header("Continue Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link("pages/advanced.py", label="🔴 Advanced Analytics")

    with col2:
        st.page_link("pages/projects.py", label="🚀 Machine Learning Projects")

    with col3:
        st.page_link("pages/career_soft_skills.py", label="💼 Data Career Skills")

    st.markdown("---")

    st.success("You are now exploring **Machine Learning and AI-driven analytics**.")


# Run Page
show()