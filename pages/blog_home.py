import streamlit as st

def show():

    st.title("📚 Data Analytics Blog")

    st.write("Explore blog articles grouped by category.")

    st.markdown("---")

    st.subheader("Categories")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🗄 Database")

        if st.button("View Database Articles"):
            st.session_state.blog_category = "database"

    with col2:
        st.markdown("### 🐍 Python")

        if st.button("View Python Articles"):
            st.session_state.blog_category = "python"

    with col3:
        st.markdown("### 🤖 Machine Learning")

        if st.button("View ML Articles"):
            st.session_state.blog_category = "ml"

    st.markdown("---")

    # Category Router
    if "blog_category" in st.session_state:

        if st.session_state.blog_category == "database":
            show_database_articles()


def show_database_articles():

    st.subheader("Database Articles")

    if st.button("Understanding MySQL Databases"):
        st.session_state.blog_post = "mysql_db"

    if "blog_post" in st.session_state:

        if st.session_state.blog_post == "mysql_db":
            from pages.blog.database import mysql_databases
            mysql_databases.show()
show()