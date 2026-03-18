import streamlit as st

def show():  # ← wrap all page content in a show() function

    # -----------------------------
    # Page Title & Hero
    # -----------------------------
    st.title("📊 Home for Data Science & Analytics")

    st.image(
        "images/data_analytics_hub.jpg",
        use_container_width=True
    )

    st.markdown("""
    Welcome to the **Data Analytics Hub** — a learning platform designed to help
    you progress from **Beginner → Intermediate → Advanced Data Science** through
    structured tutorials, projects, and blog insights.
    """)

    st.markdown("---")

    # -----------------------------
    # Feature Cards (Clickable)
    # -----------------------------
    st.subheader("Explore Key Sections")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📘 Introduction / Beginner"):
            st.switch_page("beginner.py")

    with col2:
        if st.button("🗺 Learning Roadmap / Intermediate"):
            st.switch_page("intermediate.py")

    with col3:
        if st.button("🚀 Featured Projects / Advanced"):
            st.switch_page("advanced.py")

    with col4:
        if st.button("📰 Blog"):
            st.switch_page("blog_home.py")

    st.markdown("---")

    # -----------------------------
    # Featured Projects Section
    # -----------------------------
    st.subheader("🚀 Featured Projects")

    st.markdown("""
    • Sales Analytics Dashboard  
    • Customer Churn Prediction Model  
    • Fraud Detection System  
    • Recommendation System  
    """)

    st.markdown("---")

    # -----------------------------
    # Latest Blog Posts
    # -----------------------------
    st.subheader("📰 Latest Blog Posts")

    st.markdown("""
    • Getting Started with Data Analytics  
    • 10 Essential Data Cleaning Techniques  
    • Building Interactive Dashboards with Streamlit  
    • Machine Learning Explained for Beginners  
    """)

    st.markdown("---")

    # -----------------------------
    # Footer
    # -----------------------------
    st.caption("© 2026 Data Analytics Hub | Learn • Build • Deploy")