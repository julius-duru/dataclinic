from blog.database import mysql_databases, mysql_vs_postgressql
from blog.misc import end_to_end_datascience
from blog.misc import data_preprocessing


CATEGORIES = {
    "Database": [
        {
            "title": mysql_databases.TITLE,
            "keywords": mysql_databases.KEYWORDS,
            "module": mysql_databases
        },
         {
            "title": mysql_vs_postgressql.TITLE,
            "keywords": mysql_vs_postgressql.KEYWORDS,
            "module": mysql_vs_postgressql
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
        },
        {
            "title": data_preprocessing.TITLE,
            "keywords": data_preprocessing.KEYWORDS,
            "module": data_preprocessing
        }
    ]
}