import streamlit as st


def show():

    # Page Title
    st.title("🚀 Advanced Data Science & AI")

    # Hero Image
    st.image(
        "https://images.unsplash.com/photo-1518770660439-4636190af475",
        use_container_width=True
    )

    st.markdown(
        """
        Welcome to the **Advanced Data Science Path**.

        This stage focuses on building **production-ready machine learning systems**,
        deploying models, and managing scalable data pipelines used in modern
        AI-powered organizations.
        """
    )

    st.markdown("---")

    # Advanced Learning Modules (SaaS Cards)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>🤖 Machine Learning Pipelines</h4>
        <p>Design automated pipelines for training,
        validation, and deployment of ML models.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>⚙ Model Optimization</h4>
        <p>Improve model performance using techniques
        such as hyperparameter tuning and cross-validation.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>📦 Model Deployment</h4>
        <p>Deploy machine learning models using APIs,
        dashboards, and cloud-based services.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>🔄 MLOps Workflows</h4>
        <p>Build automated systems for continuous
        training, testing, and monitoring of ML models.</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>☁ Cloud Data Platforms</h4>
        <p>Work with scalable cloud environments
        for big data processing and AI workloads.</p>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div style="background-color:#1c1f26;padding:20px;border-radius:10px;">
        <h4>📡 Real-Time Analytics</h4>
        <p>Build systems capable of processing
        and analyzing streaming data in real time.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Advanced Projects

    st.header("🚀 Advanced Data Science Projects")

    st.markdown("""
    Apply your knowledge by building real AI systems:

    • End-to-End Machine Learning Pipeline  
    • Fraud Detection System  
    • AI Recommendation Engine  
    • Predictive Maintenance Model  
    • Real-Time Data Analytics Dashboard  
    """)

    st.markdown("---")

    # Tools Section

    st.header("🧰 Tools & Technologies")

    st.markdown("""
    In this stage you will work with advanced tools used by professional data scientists:

    • Python ML libraries (Scikit-learn, XGBoost)  
    • Deep learning frameworks  
    • Data pipelines and orchestration tools  
    • Containerization and deployment platforms  
    • Cloud AI platforms
    """)

    st.markdown("---")

    # Career Section

    st.header("💼 Career Opportunities")

    st.markdown("""
    After completing the advanced learning path, you can pursue roles such as:

    • Data Scientist  
    • Machine Learning Engineer  
    • AI Engineer  
    • Data Platform Engineer  
    • Analytics Architect
    """)

    st.markdown("---")

    # Motivation Section

    st.success(
        "🎯 Mastering this level means you can design and deploy production AI systems that solve real-world problems."
    )

    # Footer
    st.caption("Advanced Learning Path • Data Analytics Hub")