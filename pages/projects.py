import streamlit as st


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
    # Page Title and Hero Image
    # ------------------------------------------------
    st.title("🚀 Data Science Projects")
    st.write("Explore practical, real-world projects across different areas of Data Science.")

    st.image(
        "images/data_science_projects.jpg",
        use_container_width=True
    )

    st.markdown("""
    Showcasing **Data Science Project **examples demonstrates mastery in the application of data science skills to solve real-world problems.

    This section highlights **hands-on projects** across multiple domains of data science including:

    - Data Analytics  
    - Machine Learning  
    - Data Engineering  
    - Artificial Intelligence & Deep Learning  
    - Data Visualization  

    Each project demonstrates **practical applications of skills** you learn in the learning paths.
    """)

    st.markdown("---")

    # ------------------------------------------------
    # Data Analytics Projects
    # ------------------------------------------------
    st.header("📊 Data Analytics Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sales Data Analysis Dashboard")
        st.markdown("""
        Analyze retail sales data to uncover trends, seasonality, and actionable insights.

        **Skills Used**
        - Python  
        - Pandas  
        - Data Visualization  
        - Streamlit Dashboards  

        **Highlights**
        - Analyze sales performance by region and product  
        - Visualize KPIs and trends  
        - Build interactive dashboards
        """)
        st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/sales-analysis)")

    with col2:
        st.subheader("Customer Segmentation Analysis")
        st.markdown("""
        Segment customers based on purchasing behavior.

        **Skills Used**
        - Data Cleaning  
        - Exploratory Data Analysis  
        - K-Means Clustering  

        **Highlights**
        - Identify high-value customer segments  
        - Build marketing insights from clusters  
        - Visualize clusters
        """)
        st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/customer-segmentation)")

    st.markdown("---")

    # ------------------------------------------------
    # Machine Learning Projects
    # ------------------------------------------------
    st.header("🤖 Machine Learning Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("House Price Prediction")
        st.markdown("""
        Build regression models to predict housing prices.

        **Skills Used**
        - Python  
        - Scikit-Learn  
        - Feature Engineering  

        **Highlights**
        - Train regression models  
        - Evaluate models using RMSE and R²  
        - Interpret predictions
        """)
        st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/house-price-prediction)")

    with col2:
        st.subheader("Spam Email Classifier")
        st.markdown("""
        Classify emails as spam or not spam.

        **Skills Used**
        - NLP  
        - Logistic Regression  
        - TF-IDF  

        **Highlights**
        - Process email text  
        - Train classification models  
        - Deploy prediction system
        """)
        st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/spam-classifier)")

    st.markdown("---")

    # ------------------------------------------------
    # Data Engineering Projects
    # ------------------------------------------------
    st.header("⚙ Data Engineering Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("ETL Data Pipeline")
        st.markdown("""
        Build an automated ETL pipeline.

        **Skills Used**
        - Python  
        - SQL  
        - Data Transformation  

        **Highlights**
        - Extract data from APIs  
        - Transform datasets  
        - Load into analytics databases
        """)
        st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/etl-pipeline)")

    with col2:
        st.subheader("Real-Time Data Streaming")
        st.markdown("""
        Process streaming data in real-time.

        **Skills Used**
        - Apache Kafka  
        - Spark Streaming  
        - Python  

        **Highlights**
        - Capture real-time events  
        - Process streaming analytics  
        - Visualize live dashboards
        """)
        st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/data-streaming)")

    st.markdown("---")

    # ------------------------------------------------
    # AI & Deep Learning Projects
    # ------------------------------------------------
    st.header("🧠 AI & Deep Learning Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Image Classification Model")
        st.markdown("""
        Train a CNN to classify images.

        **Skills Used**
        - TensorFlow / Keras  
        - CNN Architectures  

        **Highlights**
        - Train deep learning models  
        - Improve performance with data augmentation  
        - Visualize confusion matrix
        """)
        st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/image-classification)")

    with col2:
        st.subheader("AI Chatbot")
        st.markdown("""
        Build an intelligent chatbot using NLP.

        **Skills Used**
        - Transformers  
        - NLP  
        - Streamlit Deployment  

        **Highlights**
        - Process text queries  
        - Generate responses  
        - Integrate with web applications
        """)
        st.markdown("[🔗 View Project on GitHub](https://github.com/yourusername/ai-chatbot)")

    st.markdown("---")

    # ------------------------------------------------
    # Call to Action
    # ------------------------------------------------
    st.header("Start Building Your Own Projects")

    st.markdown("""
    Projects are the **best way to learn data science**.

    Building projects helps you:

    - Strengthen analytical skills  
    - Solve real-world problems  
    - Build a portfolio  
    - Impress employers
    """)

    st.info("💡 Tip: Upload your projects to GitHub to showcase your work.")
show()