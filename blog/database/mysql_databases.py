import streamlit as st


TITLE = "Understanding MySQL Databases"
CATEGORY = "Database"
KEYWORDS = ["mysql", "database", "sql", "data storage", "relational database"]


def show():

    st.title("🗄 Understanding MySQL Databases")

    st.caption("Category: Database | Level: Beginner")

    st.markdown("---")

    st.write(
        """
        MySQL is one of the most widely used **Relational Database Management Systems (RDBMS)** 
        in the world. It allows applications to store, retrieve, and manage structured data 
        efficiently using **Structured Query Language (SQL)**.
        """
    )

    st.header("Why MySQL is Important")

    st.write(
        """
        MySQL powers millions of systems including:

        - Web applications
        - Data analytics platforms
        - Enterprise software
        - E-commerce platforms
        - SaaS applications
        """
    )

    st.header("Core Components of MySQL")

    st.markdown(
        """
        **1️⃣ Database**  
        A container that holds tables and other objects.

        **2️⃣ Tables**  
        Structured data organized into rows and columns.

        **3️⃣ Rows**  
        Individual records.

        **4️⃣ Columns**  
        Attributes describing the data.
        """
    )

    st.header("Creating a MySQL Database")

    st.code(
        """
CREATE DATABASE analytics_portal;
        """,
        language="sql"
    )

    st.header("Selecting a Database")

    st.code(
        """
USE analytics_portal;
        """,
        language="sql"
    )

    st.header("Creating a Table")

    st.code(
        """
CREATE TABLE users (

    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password_hash VARCHAR(255),
    role VARCHAR(20)

);
        """,
        language="sql"
    )

    st.header("Inserting Data")

    st.code(
        """
INSERT INTO users (username, password_hash, role)
VALUES ('admin','encrypted_password','admin');
        """,
        language="sql"
    )

    st.header("Querying Data")

    st.code(
        """
SELECT * FROM users;
        """,
        language="sql"
    )

    st.success("You now understand the fundamentals of MySQL databases.")