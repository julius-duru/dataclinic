import streamlit as st

def blog_navigation():

    st.sidebar.title("📚 Blog Categories")

    if st.sidebar.button("🏠 Blog Home"):
        st.switch_page("pages/blog_home.py")

    if st.sidebar.button("Programming and Tools"):
        st.switch_page("pages/programming_tools.py")

    if st.sidebar.button("Machine Learning"):
        st.switch_page("pages/machine_learning.py")

    if st.sidebar.button("Deep Learning and AI"):
        st.switch_page("pages/deep_learning_ai.py")

    if st.sidebar.button("Big Data and Cloud"):
        st.switch_page("pages/big_data_cloud.py")

    if st.sidebar.button("Applied Data Science"):
        st.switch_page("pages/applied_data_science.py")

    if st.sidebar.button("Data Ethics and Governance"):
        st.switch_page("pages/data_ethics_governance.py")

    if st.sidebar.button("Career and Soft Skills"):
        st.switch_page("pages/career_soft_skills.py")