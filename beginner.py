import streamlit as st


def show():

    # Page Title
    st.title("📘 Beginner Data Analytics")

    # Hero Image
    st.image(
        "images/beginner_data_analytics.jpg",
        use_container_width=True
    )

    st.markdown(
        """
        Welcome to the **Beginner Data Analytics Learning Path**.

        This section is designed to help you build a **strong foundation in data analysis**
        using Python, visualization tools, and real-world datasets.
        """
    )

    st.markdown("---")

    # SaaS-style cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>🐍 Python for Data Analysis</h4>
        <p>Learn the basics of Python including variables, loops,
        and data structures used in analytics.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>🧹 Data Cleaning</h4>
        <p>Handle missing values, remove duplicates, and prepare
        datasets for meaningful analysis.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>📊 Exploratory Data Analysis</h4>
        <p>Understand patterns, relationships, and distributions
        in your dataset.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>📈 Data Visualization</h4>
        <p>Create insightful charts using libraries like
        Matplotlib and Seaborn.</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>📂 Working with Datasets</h4>
        <p>Learn how to load, explore, and manipulate datasets
        using Pandas.</p>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>🖥 Building Dashboards</h4>
        <p>Build interactive dashboards using Streamlit
        to present your analysis.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Beginner Projects Section
    st.header("🚀 Beginner Projects")

    st.markdown("""
    Start practicing with simple real-world projects:

    • Sales data analysis dashboard  
    • COVID-19 data visualization  
    • Movie dataset analysis  
    • Customer spending analysis  
    • Simple KPI business dashboard
    """)

    st.markdown("---")

    # Call to Action
    st.success(
        "💡 Tip: Complete the beginner projects before moving to the Intermediate Data Science section."
    )

    # Footer
    st.caption("Beginner Learning Path • Data Analytics Hub")