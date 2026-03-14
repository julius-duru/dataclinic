import streamlit as st


def show():

    # Page Title
    st.title("📊 Intermediate Data Analytics")

    # Hero Image
    st.image(
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f",
        use_container_width=True
    )

    st.markdown(
        """
        Welcome to the **Intermediate Data Analytics Path**.

        At this stage you move beyond basic analysis and begin building
        **data-driven solutions used in real business environments**.
        """
    )

    st.markdown("---")

    # Learning Modules (Modern SaaS Cards)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>🗄 SQL for Data Analytics</h4>
        <p>Learn how to query databases, aggregate data,
        and extract insights from relational systems.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>📊 Business Intelligence</h4>
        <p>Create KPI dashboards and performance reports
        used by business leaders for decision making.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>⚙ Feature Engineering</h4>
        <p>Transform raw data into meaningful features
        that improve machine learning performance.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>📈 Statistical Analysis</h4>
        <p>Apply hypothesis testing, correlations,
        and regression analysis to understand patterns.</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>🤖 Machine Learning Basics</h4>
        <p>Understand classification, regression,
        and clustering algorithms.</p>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>📊 Data Storytelling</h4>
        <p>Communicate insights effectively using
        compelling visualizations and dashboards.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Intermediate Projects Section

    st.header("🚀 Intermediate Data Analytics Projects")

    st.markdown("""
    Practice your skills by building real-world analytics solutions:

    • Customer segmentation using clustering  
    • Sales forecasting dashboard  
    • Marketing campaign performance analysis  
    • Customer churn prediction model  
    • Financial performance analytics dashboard  
    """)

    st.markdown("---")

    # Tools Section

    st.header("🧰 Tools You Will Use")

    st.markdown("""
    During the intermediate stage, you will begin working with industry tools such as:

    • Python (Pandas, NumPy, Scikit-learn)  
    • SQL databases  
    • Interactive dashboards with Streamlit  
    • Data visualization libraries  
    """)

    st.markdown("---")

    # Progress Note

    st.success(
        "🎯 Goal: After mastering this section, you will be ready to move into Advanced Data Science, Machine Learning pipelines, and MLOps."
    )

    # Footer

    st.caption("Intermediate Learning Path • Data Analytics Hub")