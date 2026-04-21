import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(page_title="About Me", page_icon="👤", layout="wide")


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
# Banner Section
# ------------------------------------------------

st.image(
    "images/data_banner.jpg",
    use_container_width=True
)

st.markdown(
"""
# A resource center for Data Science ideas.

I am **Julius Duru**, a Data Science professional
focused on transforming raw data into actionable insights.

Through data analytics, machine learning, deep learning, MLOps and data visualization,
I help organizations make data-driven decisions and build
scalable analytics solutions.
"""
)

st.markdown("---")


# ------------------------------------------------
# Profile Section
# ------------------------------------------------

col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "images/duruj.jpeg",
        use_container_width=True
    )

with col2:
    st.header("About Me")

    st.write("""
Data Science professional passionate about
transforming raw data into meaningful insights.

Experienced in building **data analytics platforms, data cleaning, machine learning models, deep learning, designing python web apps based on data analytics and insights,
and interactive dashboards**.
""")

    st.write("Location: Lagos, Nigeria")
    st.write("Roles: Data Analyst / Data Scientist / Presales")

st.markdown("---")


# ------------------------------------------------
# Skills Section
# ------------------------------------------------

st.header("Technical Skills")

skill1, skill2, skill3, skill4 = st.columns(4)

with skill1:
    st.subheader("Data Science")
    st.write("""
•Python and R 
•Data Analysis  
•Machine Learning 
•Deep Learning  
•Kafka 
•Pyspark 
""")

with skill2:
    st.subheader("Databases")
    st.write("""
•MongoDB  
•MySQL  
•PostgreSQL  
•SQL Server  
""")

with skill3:
    st.subheader("Visualization")
    st.write("""
•Power BI  
•Tableau  
•Matplotlib  
•Seaborn 
""")

with skill4:
    st.subheader("Deployment")
    st.write("""
•Docker 
•VMware
•AWS EKS, EC2, S3 storage
•Streamlit  
•FastAPI  
•Flask   
""")

st.markdown("---")


# ------------------------------------------------
# Portfolio Links
# ------------------------------------------------

st.header("Portfolio")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🔗 [GitHub](https://github.com/julius-duru)")

with col2:
    st.markdown("🔗 [LinkedIn](https://linkedin.com/in/duruj)")

with col3:
    st.markdown("🔗 [Portfolio](https://julius-duru.github.io/)")