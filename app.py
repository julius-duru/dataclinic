import streamlit as st

# Import pages
from pages import home
from pages import beginner
from pages import proficient
from pages import advanced
from pages import machine_learning
from pages import projects
from blog import router

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------

st.set_page_config(
    page_title="Data Analytics Learning Hub",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------
# Hide Sidebar
# ------------------------------------------------

st.markdown(
    """
    <style>

    section[data-testid="stSidebar"] {display: block;} # none
    header[data-testid="stHeader"] {display: block;}
    footer {visibility: visible;} # hidden

    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------
# ------------------------------------------------
# Navigation Bar
# ------------------------------------------------

nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns(7)

with nav1:
    if st.button("Home", key="nav_home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

with nav2:
    if st.button("Beginner", key="nav_beginner", use_container_width=True):
        st.session_state.page = "beginner"
        st.rerun()

with nav3:
    if st.button("Proficient", key="nav_proficient", use_container_width=True):
        st.session_state.page = "proficient"
        st.rerun()

with nav4:
    if st.button("Advanced", key="nav_advanced", use_container_width=True):
        st.session_state.page = "advanced"
        st.rerun()

with nav5:
    if st.button("ML", key="nav_ml", use_container_width=True):
        st.session_state.page = "ml"
        st.rerun()

with nav6:
    if st.button("Projects", key="nav_projects", use_container_width=True):
        st.session_state.page = "projects"
        st.rerun()

with nav7:
    if st.button("Blog", key="nav_blog", use_container_width=True):
        st.session_state.page = "blog"
        st.rerun()

st.markdown("---")

# ------------------------------------------------
# Default Page
# ------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# ------------------------------------------------
# Router
# ------------------------------------------------

if st.session_state.page == "home":
    home.show()

elif st.session_state.page == "beginner":
    beginner.show()

elif st.session_state.page == "proficient":
    proficient.show()

elif st.session_state.page == "advanced":
    advanced.show()

elif st.session_state.page == "ml":
    machine_learning.show()
    
elif st.session_state.page == "projects":
    projects.show()
    
elif st.session_state.page == "blog":
    router.show()

else:
    home.show()