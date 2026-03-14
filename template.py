import streamlit as st

def apply_template():

    st.set_page_config(
        page_title="Data Analytics Hub",
        layout="wide"
    )

    st.markdown("""
        <style>

        .main {
            background-color: #0e1117;
            color: white;
        }

        h1 {
            color: #4CAF50;
        }

        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }

        .card {

            background-color:#1c1f26;
            padding:20px;
            border-radius:10px;
            margin-bottom:20px;

        }

        </style>
    """, unsafe_allow_html=True)