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
    st.title("📊 Big Data Explained")
    
    st.image("images/big_data.jpg", use_container_width=True)

    st.write("""
If you have ever wondered how companies like **Netflix, Amazon, Google, or Facebook**
handle billions of data points every single day, the answer usually involves **Big Data technologies**.

Big Data refers to **extremely large and complex datasets that traditional databases
cannot easily process or analyze**.

These datasets are often generated from sources such as:

• Social media platforms  
• E-commerce websites  
• Mobile applications  
• Financial transactions  
• IoT sensors and devices  
• Video streaming platforms  

As the digital world grows, the amount of data generated globally is increasing at an **astonishing rate**.
Organizations need powerful tools and systems to **store, process, and analyze this data efficiently**.
""")

    st.markdown("---")

    st.write("""
To put things into perspective, imagine the following:

Every minute on the internet:

• Millions of Google searches happen  
• Thousands of videos are uploaded to YouTube  
• Millions of messages are sent on social media  
• Massive numbers of online purchases occur  

All of this activity produces **enormous volumes of data**.

Traditional systems were never designed to handle this scale,
which is why **Big Data technologies were created**.
""")

    st.markdown("---")

    # ------------------------------------------------
    # The 5 V's of Big Data
    # ------------------------------------------------
    st.subheader("🔑 The 5 V’s of Big Data")

    st.write("""
When people describe Big Data, they often talk about the **5 V’s**.
These characteristics explain what makes Big Data unique.
""")

    data = [
        ["Volume", "Massive amounts of data generated daily"],
        ["Velocity", "Speed at which new data is generated and processed"],
        ["Variety", "Different types of data including structured and unstructured"],
        ["Veracity", "Quality and reliability of data"],
        ["Value", "The useful insights that organizations can gain from data"]
    ]

    df = pd.DataFrame(data, columns=["Characteristic", "Explanation"])
    st.table(df)

    st.markdown("---")

    # ------------------------------------------------
    # Types of Big Data
    # ------------------------------------------------
    st.subheader("📂 Types of Data in Big Data Systems")

    st.write("""
Big Data systems handle many different types of data.

Understanding these categories helps data professionals choose the right tools.
""")

    types = [
        ["Structured Data", "Highly organized data stored in relational databases (tables, rows, columns)"],
        ["Semi-Structured Data", "Data with some organization such as JSON or XML"],
        ["Unstructured Data", "Images, videos, emails, audio files, and social media posts"]
    ]

    df_types = pd.DataFrame(types, columns=["Data Type", "Description"])
    st.table(df_types)

    st.markdown("---")

    # ------------------------------------------------
    # Big Data Technologies
    # ------------------------------------------------
    st.subheader("⚙️ Popular Big Data Technologies")

    st.write("""
To handle massive datasets efficiently, engineers rely on specialized frameworks.

These tools are designed to process data **across distributed computing clusters**.
""")

    tech = [
        ["Hadoop", "Distributed storage and processing of massive datasets"],
        ["Apache Spark", "Fast in-memory data processing engine"],
        ["Kafka", "Real-time data streaming platform"],
        ["Hive", "SQL-like querying for large datasets"],
        ["HBase", "NoSQL database designed for big data storage"]
    ]

    df_tech = pd.DataFrame(tech, columns=["Technology", "Purpose"])
    st.table(df_tech)

    st.markdown("---")

    # ------------------------------------------------
    # Big Data Architecture
    # ------------------------------------------------
    st.subheader("🏗 Typical Big Data Architecture")

    st.write("""
A typical big data pipeline includes several stages.

Each stage plays a role in turning raw data into useful insights.
""")

    pipeline = [
        ["Data Sources", "Web apps, IoT devices, social media, transactions"],
        ["Data Ingestion", "Tools like Kafka collect and move data"],
        ["Data Storage", "Distributed systems such as Hadoop or cloud storage"],
        ["Data Processing", "Spark or similar tools analyze data"],
        ["Data Analytics", "Machine learning models and BI dashboards"]
    ]

    df_pipe = pd.DataFrame(pipeline, columns=["Stage", "Description"])
    st.table(df_pipe)

    st.markdown("---")

    # ------------------------------------------------
    # Real World Applications
    # ------------------------------------------------
    st.subheader("🌍 Real-World Applications of Big Data")

    st.write("""
Big Data is transforming many industries.

Organizations use it to make smarter decisions and improve customer experiences.
""")

    apps = [
        ["Healthcare", "Predict diseases and analyze medical records"],
        ["Finance", "Fraud detection and risk analysis"],
        ["Retail", "Personalized product recommendations"],
        ["Transportation", "Traffic prediction and route optimization"],
        ["Marketing", "Customer behavior analysis"]
    ]

    df_apps = pd.DataFrame(apps, columns=["Industry", "Example Applications"])
    st.table(df_apps)

    st.markdown("---")

    # ------------------------------------------------
    # Skills for Big Data Professionals
    # ------------------------------------------------
    st.subheader("🧠 Skills Needed for Big Data Careers")

    st.write("""
Working with big data requires a mix of technical and analytical skills.

Some of the most important skills include:
""")

    skills = [
        ["Python / Scala / Java", "Programming languages used in big data systems"],
        ["SQL", "Querying structured data"],
        ["Distributed Computing", "Understanding cluster computing systems"],
        ["Data Engineering", "Designing pipelines and data workflows"],
        ["Machine Learning", "Extracting insights from large datasets"]
    ]

    df_skills = pd.DataFrame(skills, columns=["Skill", "Description"])
    st.table(df_skills)

    st.markdown("---")

    # ------------------------------------------------
    # Beginner Learning Path
    # ------------------------------------------------
    st.subheader("🚀 How to Start Learning Big Data")

    st.write("""
If you're just starting out, don't worry — you don't need to learn everything at once.

A practical learning path might look like this:
""")

    st.markdown("""
1️⃣ Learn **Python and SQL**  

2️⃣ Understand **data analytics fundamentals**

3️⃣ Study **data engineering basics**

4️⃣ Learn **Apache Spark and distributed computing**

5️⃣ Explore **cloud platforms like AWS, Azure, or Google Cloud**

6️⃣ Build projects such as **large-scale data pipelines or streaming analytics systems**
""")

    st.markdown("---")

    st.info("""
Big Data is one of the most important technologies powering the modern digital economy.

Whether you're a **data analyst, data engineer, data scientist, or machine learning engineer**,
understanding Big Data systems will open the door to many exciting opportunities.
""")


show()