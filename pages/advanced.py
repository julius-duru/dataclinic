import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="Advanced Data Analytics", layout="wide")

# ------------------------------------------------
# Top Navigation Bar
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

    st.title("🔴 Advanced Data Analytics")

    st.write("Welcome to the **Advanced Learning Path**.")

    # Hero Banner
    st.image(
        "images/analytics_hero2.jpg",
        use_container_width=True
    )

    st.markdown("""
Welcome to the **Advanced Data Analytics Learning Path**.

This track is designed for **experienced data analysts** ready to work with:

- Machine Learning
- Big Data Platforms
- Artificial Intelligence
- Enterprise Analytics Systems
""")

    st.markdown("---")

    # Embedded Navigation Links
    st.subheader("Explore Other Learning Paths")

    colA, colB, colC = st.columns(3)

    with colA:
        st.page_link("pages/beginner.py", label="🟢 Beginner Path")

    with colB:
        st.page_link("pages/proficient.py", label="🟡 Proficient Path")

    with colC:
        st.page_link("pages/machine_learning.py", label="🤖 Machine Learning")

    st.markdown("---")

    # Learning Modules
    st.header("Advanced Learning Modules")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### 🤖 Module 1: Machine Learning & Predictive Analytics

• Supervised & Unsupervised Learning  
• Regression and Classification Models  
• Feature Engineering  
• Model Evaluation and Tuning
""")

        st.markdown("""
### 🗄 Module 2: Big Data & Databases

• Hadoop and Spark Ecosystem  
• Data Warehousing Concepts  
• NoSQL Databases (MongoDB, Cassandra)  
• Query Optimization
""")

    with col2:

        st.markdown("""
### 📊 Module 3: Advanced Data Visualization

• Interactive dashboards with Plotly  
• Executive Data Storytelling  
• Advanced KPI dashboards  
• Python BI integrations
""")

        st.markdown("""
### 📈 Module 4: Advanced AI & Analytics

• Time Series Forecasting  
• Natural Language Processing (NLP)  
• Recommendation Systems  
• Deep Learning with TensorFlow & PyTorch
""")

    st.markdown("---")

    # Tools
    st.header("Advanced Tools to Master")

    st.markdown("""
• **Python (Scikit-learn, TensorFlow, PyTorch)**  
• **Spark / Hadoop** for big data processing  
• **Advanced SQL / NoSQL** databases  
• **Tableau / Power BI / Dash** dashboards  
• **Git & Version Control**
""")

    st.markdown("---")

    # Projects
    st.header("Advanced Data Analytics Projects")

    st.markdown("""
Practice with real-world analytics problems:

• Predictive maintenance systems  
• Customer churn prediction models  
• Real-time analytics dashboards  
• NLP sentiment analysis systems  
• E-commerce recommendation engines
""")

    st.markdown("---")

    # Embedded Links Section
    st.header("Continue Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link("pages/projects.py", label="🚀 View Projects")

    with col2:
        st.page_link("pages/machine_learning.py", label="🤖 ML Learning Path")

    with col3:
        st.page_link("pages/career_soft_skills.py", label="💼 Data Career Skills")

    st.markdown("---")

    st.success("You are now in the **Advanced Tier** of the Data Analytics Learning Hub.")


# Run Page
show()