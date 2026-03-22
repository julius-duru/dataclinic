from blog.database import mysql_databases
from blog.misc import end_to_end_datascience

CATEGORIES = {
    "Database": [
        {
            "title": mysql_databases.TITLE,
            "keywords": mysql_databases.KEYWORDS,
            "module": mysql_databases
        }
    ],

    "Data Engineering": [],

    "Deep Learning": [],

    "Machine Learning": [],

    "Programming Tools": [],

    "Python": [],
    
    "Misc": [
         {
            "title": end_to_end_datascience.TITLE,
            "keywords": end_to_end_datascience.KEYWORDS,
            "module": end_to_end_datascience
        }
    ]
}