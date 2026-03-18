import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="Career & Soft Skills", layout="wide")

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

    st.title("💼 Soft Skills for Data Professionals")
    st.write("Develop the essential **soft skills** and career capabilities to excel in data-related roles.")

    # Hero Image
    st.image(
        "images/soft_skills.jpg",
        use_container_width=True
    )

    st.markdown("""
Success in data roles requires not only **technical expertise** but also strong **communication, problem-solving, and collaboration skills**.  
This page provides a detailed guide to the **soft skills and career competencies** required for various data professions.
""")

    st.markdown("---")

    # ------------------------------------------------
    # Embedded Navigation Links
    # ------------------------------------------------
    st.subheader("Jump to Learning Paths")
    colA, colB, colC = st.columns(3)
    with colA:
        st.page_link("pages/beginner.py", label="🟢 Beginner")
    with colB:
        st.page_link("pages/proficient.py", label="🟡 Proficient")
    with colC:
        st.page_link("pages/advanced.py", label="🔴 Advanced")

    st.markdown("---")

    # ---------------------------------------
    # Career Roles and Soft Skills
    # ---------------------------------------

    st.header("Soft Skills & Career Competencies by Role")

    # Data Analyst
    st.subheader("📊 Data Analyst")
    st.markdown("""
**Core Soft Skills:**
- Communication: Translate technical insights into business decisions  
- Critical Thinking: Identify trends and anomalies in data  
- Problem Solving: Suggest actionable recommendations  
- Attention to Detail: Spot inconsistencies and errors in datasets  
- Time Management: Meet deadlines for reports and dashboards

**Career Competencies:**
- Excel and SQL mastery  
- Data visualization tools (Tableau, Power BI, Plotly)  
- Domain knowledge (finance, healthcare, retail, etc.)  
- Dashboard and KPI design
""")

    # Data Engineer
    st.subheader("🛠 Data Engineer")
    st.markdown("""
**Core Soft Skills:**
- Collaboration: Work closely with data scientists, analysts, and ML engineers  
- Communication: Document data pipelines clearly  
- Problem Solving: Optimize ETL processes and data storage  
- Critical Thinking: Understand system bottlenecks and scaling needs  
- Adaptability: Keep up with evolving cloud and data technologies

**Career Competencies:**
- ETL design and pipeline orchestration  
- Big data frameworks (Hadoop, Spark, Kafka)  
- SQL and NoSQL databases  
- Cloud platforms (AWS, GCP, Azure)  
- Data governance and security practices
""")

    # Data Scientist
    st.subheader("🧠 Data Scientist")
    st.markdown("""
**Core Soft Skills:**
- Analytical Thinking: Solve complex business problems using data  
- Communication: Present statistical insights to non-technical stakeholders  
- Creativity: Explore innovative ways to model and interpret data  
- Problem-Solving: Tackle data quality, model limitations, and ambiguity  
- Collaboration: Work with engineers, analysts, and business teams

**Career Competencies:**
- Machine learning & statistical modeling  
- Data wrangling and feature engineering  
- Visualization and storytelling  
- Model evaluation and validation  
- Python/R, SQL, and relevant ML libraries
""")

    # MLOps Engineer
    st.subheader("🤖 MLOps Engineer")
    st.markdown("""
**Core Soft Skills:**
- Communication: Coordinate between data science and engineering teams  
- Problem-Solving: Debug and optimize ML pipelines in production  
- Collaboration: Ensure smooth deployment of ML models  
- Critical Thinking: Monitor model drift and system performance  
- Adaptability: Integrate new tools and frameworks as ML stacks evolve

**Career Competencies:**
- CI/CD pipelines for ML  
- Model deployment with Docker, Kubernetes  
- Monitoring and logging of ML workflows  
- Cloud services for ML (AWS SageMaker, GCP AI Platform)  
- Automation of retraining and validation pipelines
""")

    # Other Roles
    st.subheader("🔧 Other Data Roles")
    st.markdown("""
**Business Intelligence Developer:** Focus on visualization, reporting, and dashboards. Requires **storytelling, communication, and attention to detail**.

**Data Product Manager:** Leads data product strategy. Requires **leadership, communication, and cross-functional collaboration**.

**AI Engineer / Deep Learning Specialist:** Works on neural networks and production AI. Requires **problem-solving, creativity, and continuous learning**.
""")

    st.markdown("---")

    # ------------------------------------------------
    # Continue Learning Section
    # ------------------------------------------------

    st.header("Continue Learning")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.page_link("pages/machine_learning.py", label="🤖 Machine Learning")
    with col2:
        st.page_link("pages/projects.py", label="🚀 Data Projects")
    with col3:
        st.page_link("pages/advanced.py", label="🔴 Advanced Analytics")

    st.markdown("---")

    st.success("Mastering these **soft skills and career competencies** will help you thrive in the data ecosystem.")


# Run Page
show()