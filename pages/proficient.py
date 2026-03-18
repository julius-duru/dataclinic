import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="Proficient Data Analytics", layout="wide")

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

    st.title("🟡 Proficient Data Analytics")

    st.write("Strengthen your data analytics skills and move toward professional expertise.")

    # ---------------------------------------
    # Hero Image
    # ---------------------------------------

    st.image(
        "images/proficient_analytics.jpg",
        use_container_width=True
    )

    st.markdown("""
 **Proficient Data Analytics Learning Path** is designed for learners who already understand **basic analytics
concepts and Python fundamentals** and want to deepen their ability to
**analyze data, create insights, and build professional dashboards**.

At this level you will begin working with **real datasets, advanced
data manipulation techniques, and exploratory data analysis (EDA)**.
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
        st.page_link("pages/advanced.py", label="🔴 Advanced Path")

    with colC:
        st.page_link("pages/machine_learning.py", label="🤖 Machine Learning")

    st.markdown("---")

    # ---------------------------------------
    # Learning Modules
    # ---------------------------------------

    st.header("Proficient Learning Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
### 📊 Module 1: Data Cleaning & Preparation

• Handling missing values  
• Data transformation and normalization  
• Data aggregation and filtering  
• Handling inconsistent datasets  
• Preparing data for analysis
""")

        st.markdown("""
### 🐼 Module 2: Advanced Pandas & Data Manipulation

• DataFrames and advanced indexing  
• Merging and joining datasets  
• Groupby operations  
• Pivot tables and reshaping data  
• Efficient data processing techniques
""")

    with col2:
        st.markdown("""
### 📈 Module 3: Exploratory Data Analysis (EDA)

• Understanding dataset structure  
• Identifying patterns and correlations  
• Statistical summaries and distributions  
• Detecting anomalies and outliers  
• Hypothesis exploration
""")

        st.markdown("""
### 📊 Module 4: Business Intelligence & Dashboards

• Designing analytics dashboards  
• KPI tracking and reporting  
• Data storytelling techniques  
• Using Plotly and interactive charts  
• Integrating dashboards with business tools
""")

    st.markdown("---")

    # ---------------------------------------
    # Recommended Tools
    # ---------------------------------------

    st.header("Tools to Master at the Proficient Level")

    st.markdown("""
At this level you should become comfortable using professional
data analytics tools.

• **Python (Pandas, NumPy)** – Advanced data analysis  
• **SQL** – Querying relational databases  
• **Plotly / Seaborn / Matplotlib** – Data visualization  
• **Excel Advanced Features** – Pivot tables and data models  
• **Power BI / Tableau** – Business intelligence dashboards
""")

    st.markdown("---")

    # ---------------------------------------
    # Proficient Projects
    # ---------------------------------------

    st.header("Proficient-Level Projects")

    st.markdown("""
Practice is essential for mastering data analytics.

Example proficient-level projects:

• Sales performance dashboard  
• Customer segmentation analysis  
• Marketing campaign analytics  
• Financial data trend analysis  
• Data cleaning automation pipeline
""")

    st.markdown("---")

    # ---------------------------------------
    # Career Development
    # ---------------------------------------

    st.header("Career Development at This Stage")

    st.markdown("""
At the proficient level you should start building a **professional
portfolio**.

Key activities include:

• Publishing analytics projects on GitHub  
• Writing case studies explaining your analysis  
• Practicing SQL interview questions  
• Participating in Kaggle competitions  
• Building data dashboards for real datasets
""")

    st.markdown("---")

    # ------------------------------------------------
    # Continue Learning
    # ------------------------------------------------

    st.header("Continue Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link("pages/advanced.py", label="🔴 Move to Advanced Level")

    with col2:
        st.page_link("pages/projects.py", label="🚀 Data Analytics Projects")

    with col3:
        st.page_link("pages/career_soft_skills.py", label="💼 Career Skills")

    st.markdown("---")

    st.success("You are building **professional-level data analytics skills**.")


# Run Page
show()