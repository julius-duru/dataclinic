from blog.database import mysql_databases, mysql_vs_postgressql
from blog.machine_learning import ml_data_pipeline, ml_concept, choosing_ml_model, model_retraining_in_production  
from blog.misc import end_to_end_datascience, data_preprocessing, clean_other_data_sources, domain_knowledge,dashboard_kpi_design
from blog.data_engineering import data_cleanig_sql, missing_values
from blog.programming_tools import datascience_toolkit


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

    "Data Engineering": [
        {
            "title": data_cleanig_sql.TITLE,
            "keywords": data_cleanig_sql.KEYWORDS,
            "module": data_cleanig_sql
        },
        {
            "title": missing_values.TITLE,
            "keywords": missing_values.KEYWORDS,
            "module": missing_values
        }         
        ],

    "Deep Learning": [],

    "Machine Learning": [
        {
            "title": ml_data_pipeline.TITLE,
            "keywords": ml_data_pipeline.KEYWORDS,
            "module": ml_data_pipeline
        },
        {
            "title": choosing_ml_model.TITLE,
            "keywords": choosing_ml_model.KEYWORDS,
            "module": choosing_ml_model
        },
        {
            "title": ml_concept.TITLE,
            "keywords": ml_concept.KEYWORDS,
            "module": ml_concept
        },
        {
            "title": model_retraining_in_production.TITLE,
            "keywords": model_retraining_in_production.KEYWORDS,
            "module": model_retraining_in_production
        }
    ],

    "Programming Tools": [
        {
            "title": datascience_toolkit.TITLE,
            "keywords": datascience_toolkit.KEYWORDS,
            "module": datascience_toolkit
        }
    ],

    "Natural Language Processing": [],
    
    "Computer Vision": [],
    
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
        },
        {
            "title": clean_other_data_sources.TITLE,
            "keywords": clean_other_data_sources.KEYWORDS,
            "module": clean_other_data_sources
        },
        {
            "title": dashboard_kpi_design.TITLE,
            "keywords": dashboard_kpi_design.KEYWORDS,
            "module": dashboard_kpi_design
        },
        {
            "title": domain_knowledge.TITLE,
            "keywords": domain_knowledge.KEYWORDS,
            "module": domain_knowledge
        }
    ]
}