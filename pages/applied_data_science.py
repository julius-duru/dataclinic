import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="Applied Data Science", layout="wide")

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

    st.title("🧠 Applied Data Science")

    st.write("Turning data science theory into **real-world solutions**.")

    # Hero Image
    st.image(
        "images/applied_datascience.jpg",
        use_container_width=True
    )

    st.markdown("""

Applied data science focuses on **using data, algorithms, and machine learning models
to solve real business problems**.

While theoretical data science explores algorithms and mathematical models,
applied data science emphasizes **building practical solutions that drive decisions
and automation**.
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

    # Learning Modules
    st.header("Applied Data Science Modules")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### 📊 Module 1: Data Collection & Data Engineering

• Data collection from APIs, databases, and files  
• Data cleaning and preprocessing  
• Handling missing and inconsistent data  
• Building ETL pipelines  
• Working with structured and unstructured data
""")

        st.markdown("""
### 🤖 Module 2: Machine Learning in Practice

• Regression and classification models  
• Clustering and segmentation  
• Feature engineering  
• Model evaluation and cross-validation  
• Hyperparameter tuning
""")

    with col2:

        st.markdown("""
### 📈 Module 3: Data Visualization & Decision Support

• Data storytelling  
• Interactive dashboards  
• Business intelligence tools  
• KPI and metric design  
• Communicating insights to stakeholders
""")

        st.markdown("""
### 🚀 Module 4: Model Deployment & Production Systems

• Deploying models using APIs  
• Real-time prediction systems  
• Monitoring models in production  
• Model retraining pipelines  
• MLOps workflows
""")

    st.markdown("---")

    # Tools Section
    st.header("Essential Tools for Applied Data Science")

    st.markdown("""
• **Python (Pandas, NumPy, Scikit-learn)** – Data analysis and ML  
• **SQL & Databases** – Managing structured data  
• **Jupyter Notebook** – Data exploration  
• **Docker & APIs** – Model deployment  
• **Streamlit / Dash** – Analytics applications  
• **Cloud Platforms (AWS, Azure, GCP)** – Scalable workflows
""")

    st.markdown("---")

    # Applications
    st.header("Real-World Applications")

    st.markdown("""
Applied data science powers many industries:

• **Healthcare** – Predicting disease risk  
• **Finance** – Fraud detection and risk modeling  
• **Retail** – Recommendation systems  
• **Transportation** – Demand forecasting  
• **Marketing** – Customer segmentation
""")

    st.markdown("---")

    # Projects
    st.header("Example Applied Data Science Projects")

    st.markdown("""
• Customer churn prediction  
• Fraud detection systems  
• Recommendation engines  
• Retail demand forecasting  
• Sentiment analysis for product reviews  
• Predictive maintenance systems
""")

    st.markdown("---")

    # Future Section
    st.header("Future of Applied Data Science")

    st.markdown("""
Emerging trends include:

• AI-powered decision systems  
• Automated Machine Learning (AutoML)  
• Real-time analytics platforms  
• Responsible AI and explainable models  
• AI integration across business operations
""")

    st.markdown("---")

    # Embedded Links
    st.header("Continue Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link("pages/machine_learning.py", label="🤖 Machine Learning")

    with col2:
        st.page_link("pages/projects.py", label="🚀 Data Projects")

    with col3:
        st.page_link("pages/career_soft_skills.py", label="💼 Career Skills")

    st.markdown("---")

    st.success("You are exploring **Applied Data Science**, where analytics meets real-world impact.")


# Run Page
show()