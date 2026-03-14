# pip install mysql-connector-python
import mysql.connector
import pandas as pd


def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database="analytics_portal"
    )

    return conn


def get_contents(category):

    conn = connect_db()

    query = "SELECT * FROM contents WHERE category = %s"

    df = pd.read_sql(query, conn, params=(category,))

    conn.close()

    return df
