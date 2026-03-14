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
    st.title("💻 Programming Tools for Data Analytics")

    st.write("""
If you're getting into **data analytics**, one of the first questions you might ask is:

**“What tools do data professionals actually use?”**

The good news is that the ecosystem is fairly consistent.  
Most data analysts, data scientists, and machine learning engineers rely on a common set of **programming languages, development environments, and libraries**.

This page walks you through the most important tools — and explains **when and why you might use each one**.
""")

    st.image(
        "images/analytics_hero5.jpg",
        use_container_width=True
    )

    st.markdown("---")

    st.write("""
Think of this page as a **friendly cheat sheet**.  
Instead of memorizing everything at once, focus on understanding **what each tool is good for**.
""")

    st.markdown("---")

    # ==============================
    # Programming Languages
    # ==============================
    st.subheader("📝 Programming Languages")

    st.write("""
Every data professional starts with at least **one core programming language**.

These languages help you clean data, run analysis, build models, and automate tasks.
""")

    languages = [
        ["Python", "General data analytics, machine learning, automation", "General-purpose", "Most popular language in data science. Beginner friendly."],
        ["R", "Statistical analysis and visualization", "Statistics-focused", "Widely used in academia and research."],
        ["SQL", "Querying and managing databases", "Database language", "Essential for working with structured data."],
        ["Julia", "High-performance numerical computing", "Scientific computing", "Very fast for heavy mathematical computations"]
    ]

    df_languages = pd.DataFrame(languages, columns=["Tool", "Purpose", "Category", "Notes"])
    st.table(df_languages)

    st.markdown("---")

    # ==============================
    # Development Environments
    # ==============================
    st.subheader("⚙️ Development Environments")

    st.write("""
Once you choose a programming language, you'll need a **place to write and run your code**.

These tools make coding easier by offering features like debugging, extensions, and interactive notebooks.
""")

    environments = [
        ["Jupyter Notebook", "Interactive coding and data exploration", "Notebook Environment", "Perfect for experimentation and visual storytelling"],
        ["VS Code", "Lightweight but powerful code editor", "IDE/Editor", "Extremely popular with data professionals"],
        ["PyCharm", "Professional Python development environment", "IDE", "Advanced debugging and project tools"],
        ["Google Colab", "Cloud-based notebook environment", "Cloud IDE", "Run Python without installing anything locally"]
    ]

    df_env = pd.DataFrame(environments, columns=["Tool", "Purpose", "Category", "Notes"])
    st.table(df_env)

    st.markdown("---")

    # ==============================
    # Libraries
    # ==============================
    st.subheader("📚 Libraries & Frameworks")

    st.write("""
Programming languages become truly powerful when you combine them with **libraries**.

Libraries are collections of pre-written code that make it much easier to perform complex tasks.
""")

    libraries = [
        ["Pandas", "Data cleaning and manipulation", "Python Library", "The core tool for working with tables and datasets"],
        ["NumPy", "Numerical computing and arrays", "Python Library", "Provides fast operations for mathematical calculations"],
        ["Matplotlib / Seaborn", "Data visualization", "Visualization Libraries", "Create charts, graphs, and statistical visuals"],
        ["Scikit-learn", "Machine learning algorithms", "ML Library", "Used for regression, classification, clustering"],
        ["TensorFlow / PyTorch", "Deep learning and neural networks", "AI Framework", "Used for advanced machine learning and AI"]
    ]

    df_lib = pd.DataFrame(libraries, columns=["Tool", "Purpose", "Category", "Notes"])
    st.table(df_lib)

    st.markdown("---")

    # ==============================
    # Best Practices
    # ==============================
    st.subheader("✅ Recommended Practices")

    st.write("""
Beyond tools, successful data professionals also follow **good engineering habits**.

These practices help you write cleaner code, collaborate with others, and avoid costly mistakes.
""")

    practices = [
        ["Use Git for version control", "Track changes in your code", "Best Practice", "Essential for teamwork and collaboration"],
        ["Write modular and reusable code", "Make projects easier to maintain", "Coding Practice", "Reusable code saves time"],
        ["Document your work", "Explain what your code does", "Documentation", "Important for future you and teammates"],
        ["Test your scripts", "Ensure code works correctly", "Testing", "Prevents bugs in production"],
        ["Use online documentation", "Learn and troubleshoot faster", "Learning Strategy", "Official docs and communities are invaluable"]
    ]

    df_practices = pd.DataFrame(practices, columns=["Practice", "Purpose", "Category", "Notes"])
    st.table(df_practices)

    st.markdown("---")

    # ==============================
    # Sample Projects
    # ==============================
    st.subheader("💡 Sample Projects to Practice")

    st.write("""
The best way to learn these tools is by **building projects**.

Start small, then gradually increase complexity as your confidence grows.
""")

    projects = [
        ["Data cleaning and preprocessing", "Python & Pandas", "Beginner", "Practice handling messy datasets"],
        ["Exploratory data analysis dashboard", "Jupyter Notebook", "Beginner/Intermediate", "Summarize and visualize datasets"],
        ["Machine learning prediction model", "Scikit-learn", "Intermediate", "Build and evaluate predictive models"],
        ["Deep learning experiment", "TensorFlow / PyTorch", "Advanced", "Train neural networks on large datasets"],
        ["Interactive visualization dashboard", "Plotly / Streamlit", "Intermediate", "Create interactive analytics apps"]
    ]

    df_projects = pd.DataFrame(projects, columns=["Project", "Tools", "Difficulty", "Notes"])
    st.table(df_projects)

    st.markdown("---")

    # ==============================
    # Learning Resources
    # ==============================
    st.subheader("📖 Helpful Learning Resources")

    st.write("""
If you'd like to go deeper, these platforms provide excellent tutorials and practice environments.
""")

    st.markdown("""
- **DataCamp** – Interactive data science courses  
- **Kaggle Learn** – Free hands-on micro courses  
- **Streamlit Documentation** – Learn to build data apps  
- **Python Official Documentation** – Reference for Python programming
""")


show()