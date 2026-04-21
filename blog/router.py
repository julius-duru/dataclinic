import streamlit as st
from blog.categories import CATEGORIES
from blog.database import mysql_vs_postgressql, mysql_databases
from blog.misc import data_story,storytelling_with_data, end_to_end_datascience, data_preprocessing, clean_other_data_sources, domain_knowledge,dashboard_kpi_design, power_bi_report, mlops_workflow, data_governance
from blog.machine_learning import ml_data_pipeline, ml_concept, choosing_ml_model, model_retraining_in_production, machine_learning_workflow, mlops_pipeline
from blog.programming_tools import datascience_toolkit 
from blog.data_engineering import missing_values, data_cleanig_sql, model_lifecycle_management
from blog.data_visualization import power_bi, power_bi_visualization_tools
from blog.misc import mlops_frameworks, securing_model
from blog.deep_learning import deep_learning_guide, cnn_and_rnn, ann_end_to_end, ann_cnn_rnn_lstm
from blog.docker import docker_setup, docker_guide, flask_mysql_in_docker, flask_postgresql_in_docker

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