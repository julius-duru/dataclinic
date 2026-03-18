import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="Beginner Data Analytics", layout="wide")

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

    st.title("🟢 Beginner Data Analytics")

    st.write("Welcome to the **Beginner Learning Path**.")

    # ---------------------------------------
    # Image
    # ---------------------------------------

    st.image(
        "images/beginner_data_analytics.jpg",
        use_container_width=True
    )

    st.markdown("""

This section is designed for individuals who are **new to data analytics
or data science**.

You will learn the **fundamental concepts, tools, and techniques**
required to begin a successful career in data analytics.
""")

    st.markdown("---")

    # ------------------------------------------------
    # Embedded Navigation Links
    # ------------------------------------------------

    st.subheader("Explore Other Learning Paths")

    colA, colB, colC = st.columns(3)

    with colA:
        st.page_link("pages/proficient.py", label="🟡 Proficient Path")

    with colB:
        st.page_link("pages/advanced.py", label="🔴 Advanced Path")

    with colC:
        st.page_link("pages/machine_learning.py", label="🤖 Machine Learning")

    st.markdown("---")

    # ---------------------------------------
    # Learning Modules
    # ---------------------------------------

    st.header("Beginner Learning Modules")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
### 📘 Module 1: Introduction to Data Analytics

• What is Data Analytics  
• Types of Data Analytics  
• Real-world applications  

### 🐍 Module 2: Introduction to Python

• Python basics  
• Variables and data types  
• Control structures  
• Functions
""")

    with col2:
        st.markdown("""
### 📊 Module 3: Data Visualization

• Introduction to data visualization  
• Charts and graphs  
• Using Matplotlib and Seaborn  

### 🗄 Module 4: Introduction to Databases

• What is a database  
• Introduction to SQL  
• Basic queries
""")

    st.markdown("---")

    # ---------------------------------------
    # Recommended Tools
    # ---------------------------------------

    st.header("Beginner Tools to Learn")

    st.markdown("""
• **Python** – Core programming language for data analytics  
• **Excel** – Basic data analysis and cleaning  
• **Jupyter Notebook** – Interactive coding environment  
• **Pandas** – Data manipulation library  
• **Matplotlib / Seaborn** – Data visualization libraries
""")

    st.markdown("---")

    # ---------------------------------------
    # Beginner Projects
    # ---------------------------------------

    st.header("Beginner Projects")

    st.markdown("""
Working on small projects is one of the best ways to learn.

Example beginner projects:

• Sales data analysis  
• Customer data visualization dashboard  
• COVID-19 dataset exploration  
• Movie dataset analysis  
• Financial dataset visualization
""")

    st.markdown("---")

    # ------------------------------------------------
    # Continue Learning
    # ------------------------------------------------

    st.header("Continue Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.page_link("pages/proficient.py", label="🟡 Move to Proficient Level")

    with col2:
        st.page_link("pages/projects.py", label="🚀 Practice Projects")

    with col3:
        st.page_link("pages/career_soft_skills.py", label="💼 Career Skills")

    st.markdown("---")

    st.success("You are starting your **Data Analytics journey**. Keep learning and building projects!")


# Run Page
show()