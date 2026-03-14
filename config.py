# config.py

import os

# ===============================
# DATABASE CONFIGURATION (MySQL)
# ===============================

DB_CONFIG = {

    "host": "localhost",
    "user": "",
    "password": "",
    "database": "analytics_portal",
    "port": 3306

}


# ===============================
# STREAMLIT APP SETTINGS
# ===============================

APP_CONFIG = {

    "site_name": "Data Analytics Hub",
    "admin_email": "decency08@gmailcom",
    "default_page": "Home",
    "theme_color": "#4CAF50"

}


# ===============================
# SECURITY SETTINGS
# ===============================

SECURITY_CONFIG = {

    "bcrypt_rounds": 12,
    "session_timeout_minutes": 60

}


# ===============================
# FILE UPLOAD SETTINGS
# ===============================

UPLOAD_CONFIG = {

    "upload_folder": "uploads",
    "allowed_extensions": ["csv", "xlsx", "json", "txt"],
    "max_file_size_mb": 10

}


# ===============================
# CONTENT CATEGORIES
# ===============================

CONTENT_CATEGORIES = [

    "beginner",
    "proficient",
    "database",
    "deep learning",
    "machine learning",
    "tools",
    "soft skills",
    "computer vision",
    "advanced"

]


# ===============================
# PAGE MENU
# ===============================

NAVIGATION_MENU = [

    "Home",
    "Beginner",
    "Proficient",
    "Advanced",
    "ML",
    "Blog"

]