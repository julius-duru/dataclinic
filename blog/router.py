import streamlit as st
from blog.categories import CATEGORIES
from blog.database import mysql_databases
from blog.database import mysql_vs_postgressql
from blog.misc import end_to_end_datascience, data_preprocessing, clean_other_data_sources, domain_knowledge

def show():

    st.title(" Data Analytics Blog")

    st.markdown("Search articles or browse by category.")

    st.markdown("---")

    # Search
    query = st.text_input(" Search Articles")

    if query:

        results = []

        for category, articles in CATEGORIES.items():
            for article in articles:

                if query.lower() in article["title"].lower() or any(
                    query.lower() in k.lower() for k in article["keywords"]
                ):
                    results.append(article)

        if results:

            st.subheader("Search Results")

            for article in results:

                if st.button(article["title"]):
                    st.session_state.article = article

        else:
            st.warning("No articles found.")

    st.markdown("---")

    # Category navigation
    st.subheader("Browse Categories")

    for category, articles in CATEGORIES.items():

        with st.expander(category):

            for article in articles:

                if st.button(article["title"], key=article["title"]):
                    st.session_state.article = article

    st.markdown("---")

    # Load article
    if "article" in st.session_state:

        st.markdown("---")
        st.session_state.article["module"].show()