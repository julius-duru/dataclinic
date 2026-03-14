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
    # Page Title
    # ------------------------------------------------
    st.title("⚖️ Data Ethics and Data Governance")

    st.write("""
In today's digital world, **data is one of the most valuable assets** an organization can possess.
Every online interaction — whether it is a purchase, a social media post, or a healthcare record —
creates data.

Organizations use this data to make decisions, build machine learning models,
and improve customer experiences.

However, with this growing power comes **serious responsibilities**.

If data is misused, it can lead to:

• Privacy violations  
• Discrimination and bias in algorithms  
• Security breaches  
• Loss of public trust  

This is why **Data Ethics and Data Governance** are essential topics for anyone working in
data analytics, data engineering, data science, or artificial intelligence.
""")

    st.markdown("---")

    # ------------------------------------------------
    # Data Ethics
    # ------------------------------------------------
    st.subheader("🧠 What is Data Ethics?")

    st.write("""
**Data Ethics** refers to the moral principles and guidelines that determine
how data should be collected, processed, stored, and used.

Simply put, data ethics asks an important question:

**“Just because we can collect or use data, does that mean we should?”**

Ethical data practices ensure that data is used in ways that are:

• Responsible  
• Transparent  
• Fair  
• Respectful of privacy  
• Beneficial to society
""")

    ethics_data = [
        ["Privacy", "Protecting personal data from unauthorized access"],
        ["Transparency", "Being clear about how data is collected and used"],
        ["Fairness", "Ensuring algorithms do not discriminate"],
        ["Accountability", "Organizations taking responsibility for data use"],
        ["Data Minimization", "Collecting only the data that is truly necessary"]
    ]

    df_ethics = pd.DataFrame(ethics_data, columns=["Principle", "Explanation"])
    st.table(df_ethics)

    st.markdown("---")

    # ------------------------------------------------
    # Data Governance
    # ------------------------------------------------
    st.subheader("🏛 What is Data Governance?")

    st.write("""
While data ethics focuses on **moral responsibility**, data governance focuses on
**how organizations manage and control data assets**.

Data governance provides the **framework, policies, and standards**
that ensure data is properly handled throughout its lifecycle.

A strong governance framework helps organizations answer questions like:

• Who owns the data?  
• Who can access it?  
• How long should it be stored?  
• How is the data protected?
""")

    governance = [
        ["Data Ownership", "Assigning responsibility for data assets"],
        ["Data Quality Management", "Ensuring data is accurate and reliable"],
        ["Data Security", "Protecting data through encryption and access controls"],
        ["Compliance", "Ensuring regulations and legal standards are followed"],
        ["Data Stewardship", "Managing data integrity and governance policies"]
    ]

    df_gov = pd.DataFrame(governance, columns=["Governance Component", "Description"])
    st.table(df_gov)

    st.markdown("---")

    # ------------------------------------------------
    # Major Trends
    # ------------------------------------------------
    st.subheader("📈 Trends in Data Ethics and Governance")

    st.write("""
The rapid growth of artificial intelligence and big data has made
ethical data practices more important than ever.

Several major trends are shaping the future of data governance.
""")

    trends = [
        ["Responsible AI", "Ensuring AI systems make fair and transparent decisions"],
        ["Explainable AI", "Making machine learning models understandable to humans"],
        ["Stronger Data Privacy Laws", "New regulations protecting consumer data"],
        ["AI Ethics Committees", "Organizations creating oversight boards for AI systems"],
        ["Automated Governance Tools", "Software platforms managing compliance and data quality"]
    ]

    df_trends = pd.DataFrame(trends, columns=["Trend", "Description"])
    st.table(df_trends)

    st.markdown("---")

    # ------------------------------------------------
    # Key Issues
    # ------------------------------------------------
    st.subheader("⚠️ Common Issues and Challenges")

    st.write("""
Despite growing awareness of ethical data use, organizations still face
several challenges when managing large-scale data systems.
""")

    issues = [
        ["Algorithmic Bias", "Machine learning models producing unfair outcomes"],
        ["Data Privacy Violations", "Unauthorized exposure of personal information"],
        ["Lack of Transparency", "Users not knowing how their data is used"],
        ["Poor Data Governance", "Unstructured data management across departments"],
        ["Security Breaches", "Cyberattacks exposing sensitive information"]
    ]

    df_issues = pd.DataFrame(issues, columns=["Issue", "Explanation"])
    st.table(df_issues)

    st.markdown("---")

    # ------------------------------------------------
    # Innovations
    # ------------------------------------------------
    st.subheader("🚀 Innovations Improving Ethical Data Management")

    st.write("""
Researchers and technology companies are developing innovative solutions
to improve ethical data management and responsible AI.
""")

    innovations = [
        ["Federated Learning", "Training models without sharing raw data"],
        ["Differential Privacy", "Protecting individual identities in datasets"],
        ["AI Bias Detection Tools", "Automatically identifying unfair algorithms"],
        ["Data Lineage Systems", "Tracking where data comes from and how it is used"],
        ["Privacy-Preserving Machine Learning", "Analyzing data while maintaining privacy"]
    ]

    df_innov = pd.DataFrame(innovations, columns=["Innovation", "Description"])
    st.table(df_innov)

    st.markdown("---")

    # ------------------------------------------------
    # Importance for Data Professionals
    # ------------------------------------------------
    st.subheader("👩‍💻 Why Data Ethics Matters for Data Professionals")

    st.write("""
If you work in any data-related role such as:

• Data Analyst  
• Data Scientist  
• Data Engineer  
• Machine Learning Engineer  
• MLOps Engineer  

you must understand ethical data practices.

Modern data professionals must think beyond technical skills and consider:

• Whether data contains bias  
• Whether personal data is protected  
• Whether algorithms are transparent  
• Whether decisions made using data are fair
""")

    st.info("""
Ethical data practices are not just about compliance — they are about
building technology that **benefits society and earns public trust**.
""")

    st.markdown("---")

    # ------------------------------------------------
    # Final Section
    # ------------------------------------------------
    st.subheader("🌍 The Future of Ethical Data")

    st.write("""
As artificial intelligence and big data continue to expand,
the importance of ethical data management will only grow.

Future developments may include:

• Global AI governance frameworks  
• Automated fairness testing in ML pipelines  
• Stronger international data privacy regulations  
• Ethical AI certification standards  

Organizations that prioritize responsible data practices will gain
greater trust, better compliance, and long-term sustainability.
""")


show()