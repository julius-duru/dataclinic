import streamlit as st


def show():

    st.title("📊 Data Analytics Learning Hub")

    # Hero Image
    st.image(
        "images/analytics_hero3.jpg",
        use_container_width=True
    )

    st.markdown(
        """
Welcome to the **Data Analytics Learning Hub**, a platform designed to guide learners
from beginner to advanced levels in **data science, analytics, and AI**.

Whether you are starting your journey or looking to deepen your knowledge,
this platform provides structured learning resources, real-world projects,
and expert insights.
"""
    )

    st.markdown("---")

    # Introduction Section
    st.header("Introduction to Data Analytics")

    st.markdown(
        """
Data analytics involves examining raw data to uncover patterns, trends,
and insights that can help organizations make better decisions.

Key components include:

• Data collection and preparation  
• Exploratory data analysis  
• Statistical modeling  
• Machine learning  
• Data visualization  
• Communication of insights  

With the explosion of data across industries, data analytics has become
one of the **most valuable skills in the modern workforce**.
"""
    )

    st.markdown("---")

    # Learning Roadmap
    st.header("Learning Roadmap")

    st.markdown(
        """
Our learning roadmap is structured into **three progressive levels**:

**Beginner**

• Introduction to data analytics  
• Python and R basics  
• Data visualization fundamentals  
• Understanding datasets

**Proficient**

• Machine learning concepts  
• Data wrangling and feature engineering  
• SQL and database analysis  
• Building dashboards

**Advanced**

• Deep learning  
• Big data technologies  
• Cloud data engineering  
• AI-powered analytics systems
"""
    )

    st.markdown("---")

    # Featured Projects
    st.header("Featured Projects")

    st.markdown(
        """
Hands-on projects help reinforce learning. Some examples include:

• Sales performance dashboard  
• Customer segmentation using clustering  
• Predictive model for loan approval  
• Data visualization dashboard with Streamlit  
• End-to-end machine learning pipeline

These projects help learners build **real portfolio-ready experience**.
"""
    )

    st.markdown("---")

    # Blog Section
    st.header("Latest Blog Posts")

    st.markdown(
        """
Stay updated with tutorials, insights, and practical guides on
data science and analytics.
"""
    )
show()