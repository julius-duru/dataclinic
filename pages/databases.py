import streamlit as st
import pandas as pd


def show():

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
    # Page Header
    # ------------------------------------------------
    st.title("🗄 Databases for Data Scientists and Data Analysts")

    st.write("""
Data is the foundation of every analytics and machine learning project.
Before data can be analyzed, visualized, or used to train models,
it must first be **stored and organized efficiently**.

This is where **databases** come in.

Databases allow organizations to:

• Store massive amounts of data  
• Retrieve data efficiently  
• Manage relationships between datasets  
• Maintain data integrity and security  

For data professionals such as **data analysts, data scientists,
data engineers, and machine learning engineers**, understanding
different types of databases is a critical skill.
""")

    st.markdown("---")

    st.write("""
Not all databases are designed for the same purpose.

Some databases work best for **structured data**, while others are designed
to handle **unstructured or semi-structured data**.

In this guide, we will explore some of the most important databases
used in the data science ecosystem and discuss **when to use each one**.
""")

    st.markdown("---")

    # ------------------------------------------------
    # Relational Databases
    # ------------------------------------------------
    st.subheader("📊 Relational Databases (SQL Databases)")

    st.write("""
Relational databases store data in **tables composed of rows and columns**.
They use **SQL (Structured Query Language)** to retrieve and manipulate data.

These databases are ideal for structured data where relationships between
different tables need to be maintained.
""")

    relational_data = [
        ["MySQL", "Popular open-source relational database", "Web applications, dashboards, analytics"],
        ["PostgreSQL", "Advanced relational database with strong analytics features", "Data science pipelines, large analytical workloads"],
        ["SQLite", "Lightweight embedded database", "Small applications and local analysis"],
        ["Microsoft SQL Server", "Enterprise-level relational database", "Large corporate systems"]
    ]

    df_relational = pd.DataFrame(relational_data,
                                columns=["Database", "Description", "Typical Use Cases"])

    st.table(df_relational)

    st.markdown("---")

    # ------------------------------------------------
    # NoSQL Databases
    # ------------------------------------------------
    st.subheader("📦 NoSQL Databases")

    st.write("""
Unlike relational databases, **NoSQL databases** are designed to handle
large volumes of **unstructured or semi-structured data**.

They are commonly used in applications that require **high scalability,
flexible schemas, and fast performance**.
""")

    nosql_data = [
        ["MongoDB", "Document-based database using JSON-like documents", "Web applications, big data, flexible schemas"],
        ["Cassandra", "Highly scalable distributed database", "Large-scale data platforms"],
        ["Redis", "In-memory key-value store", "Caching and real-time analytics"],
        ["Elasticsearch", "Search and analytics engine", "Log analysis and search systems"]
    ]

    df_nosql = pd.DataFrame(nosql_data,
                            columns=["Database", "Description", "Typical Use Cases"])

    st.table(df_nosql)

    st.markdown("---")

    # ------------------------------------------------
    # Databases Most Used by Data Scientists
    # ------------------------------------------------
    st.subheader("🧠 Databases Most Used by Data Scientists")

    st.write("""
Data scientists frequently work with databases to retrieve and prepare data
before performing analysis or building machine learning models.

Some databases are particularly popular within the data science community.
""")

    ds_data = [
        ["PostgreSQL", "Advanced analytics queries and large datasets"],
        ["MySQL", "Commonly used in many business systems"],
        ["MongoDB", "Handling flexible and semi-structured datasets"],
        ["BigQuery", "Cloud data warehouse for large-scale analytics"],
        ["Snowflake", "Modern cloud-based analytics database"]
    ]

    df_ds = pd.DataFrame(ds_data, columns=["Database", "Why Data Scientists Use It"])
    st.table(df_ds)

    st.markdown("---")

    # ------------------------------------------------
    # Choosing the Right Database
    # ------------------------------------------------
    st.subheader("🎯 Choosing the Right Database")

    st.write("""
Selecting the right database depends on several factors:

• Type of data (structured vs unstructured)  
• Scale of the data  
• Query complexity  
• Real-time requirements  
• Analytics needs
""")

    choice_data = [
        ["Structured business data", "MySQL or PostgreSQL"],
        ["Flexible document data", "MongoDB"],
        ["Large-scale analytics", "Snowflake or BigQuery"],
        ["High-speed caching", "Redis"],
        ["Massive distributed systems", "Cassandra"]
    ]

    df_choice = pd.DataFrame(choice_data,
                             columns=["Scenario", "Recommended Database"])

    st.table(df_choice)

    st.markdown("---")

    # ------------------------------------------------
    # Learning Path
    # ------------------------------------------------
    st.subheader("🚀 Learning Path for Databases")

    st.write("""
If you are learning data analytics or data science, you do not need
to master every database at once.

Instead, follow a gradual learning path.
""")

    learning_path = [
        ["Beginner", "Start with SQL and MySQL"],
        ["Intermediate", "Learn PostgreSQL and advanced SQL queries"],
        ["Intermediate", "Explore MongoDB and NoSQL databases"],
        ["Advanced", "Work with cloud data warehouses like Snowflake or BigQuery"],
        ["Expert", "Understand distributed databases and big data systems"]
    ]

    df_learning = pd.DataFrame(learning_path,
                               columns=["Level", "Recommended Focus"])

    st.table(df_learning)

    st.markdown("---")

    # ------------------------------------------------
    # General Advice
    # ------------------------------------------------
    st.subheader("💡 Practical Advice for Data Professionals")

    st.write("""
Here are some general recommendations for choosing databases during
your data science journey.
""")

    st.markdown("""
**For beginners**

Start with **MySQL or PostgreSQL**.  
These databases will teach you SQL and relational data modeling.

**For intermediate learners**

Learn **PostgreSQL deeply** and begin exploring **MongoDB** for flexible data storage.

**For advanced data professionals**

Work with **cloud data warehouses** such as:

• Snowflake  
• Google BigQuery  
• Amazon Redshift  

These systems power modern analytics platforms.

**For large-scale data engineering**

You may eventually work with:

• Apache Hive  
• Cassandra  
• Distributed data lakes
""")

    st.markdown("---")

    st.info("""
Understanding databases is one of the most important skills
for anyone working in data.

A strong foundation in SQL and database design will make you
far more effective as a **data analyst, data scientist, or data engineer**.
""")


show()