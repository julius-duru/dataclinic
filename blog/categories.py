from blog.database import mysql_databases, mysql_vs_postgressql
from blog.machine_learning import ml_data_pipeline, ml_concept, choosing_ml_model, model_retraining_in_production, machine_learning_workflow, mlops_pipeline
from blog.misc import storytelling_with_data, end_to_end_datascience, data_preprocessing, clean_other_data_sources, domain_knowledge,dashboard_kpi_design, power_bi_report, mlops_workflow, data_governance, mlops_frameworks, securing_model, data_story,time_series_models,api_and_business_softwares, api_automation_and_security
from blog.data_engineering import data_cleanig_sql, missing_values, model_lifecycle_management, etl_and_elt_pipelines, data_pipelines
from blog.programming_tools import datascience_toolkit
from blog.data_visualization import power_bi, power_bi_visualization_tools
from blog.deep_learning import deep_learning_guide, cnn_and_rnn, ann_end_to_end, ann_cnn_rnn_lstm
from blog.docker import docker_setup, docker_guide, flask_mysql_in_docker, flask_postgresql_in_docker

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
            "title": model_lifecycle_management.TITLE,
            "keywords": model_lifecycle_management.KEYWORDS,
            "module": model_lifecycle_management
        },
        {
            "title": etl_and_elt_pipelines.TITLE,
            "keywords": etl_and_elt_pipelines.KEYWORDS,
            "module": etl_and_elt_pipelines
        },
        {
            "title": data_pipelines.TITLE,
            "keywords": data_pipelines.KEYWORDS,
            "module": data_pipelines
        },
        {
            "title": missing_values.TITLE,
            "keywords": missing_values.KEYWORDS,
            "module": missing_values
        }         
    ],

    "Deep Learning": [
        {
            "title": deep_learning_guide.TITLE,
            "keywords": deep_learning_guide.KEYWORDS,
            "module": deep_learning_guide
        },
        {
            "title": cnn_and_rnn.TITLE,
            "keywords": cnn_and_rnn.KEYWORDS,
            "module": cnn_and_rnn
        },
        {
            "title": ann_end_to_end.TITLE,
            "keywords": ann_end_to_end.KEYWORDS,
            "module": ann_end_to_end
        },
        {
          "title": ann_cnn_rnn_lstm.TITLE,
            "keywords": ann_cnn_rnn_lstm.KEYWORDS,
            "module": ann_cnn_rnn_lstm  
        }
        ],
    
    "Data Visualization": [
        {
            "title": power_bi.TITLE,
            "keywords": power_bi.KEYWORDS,
            "module": power_bi
        },
        {
            "title": power_bi_visualization_tools.TITLE,
            "keywords": power_bi_visualization_tools.KEYWORDS,
            "module": power_bi_visualization_tools
        }
    ],
    
      "Docker": [
        {
            "title": docker_setup.TITLE,
            "keywords": docker_setup.KEYWORDS,
            "module": docker_setup
        },
        {
            "title": flask_mysql_in_docker.TITLE,
            "keywords": flask_mysql_in_docker.KEYWORDS,
            "module": flask_mysql_in_docker
        },
        {
            "title": flask_postgresql_in_docker.TITLE,
            "keywords": flask_postgresql_in_docker.KEYWORDS,
            "module": flask_postgresql_in_docker
        },
        {
            "title": docker_guide.TITLE,
            "keywords": docker_guide.KEYWORDS,
            "module": docker_guide
        }
    ],

    "Machine Learning": [
        {
            "title": ml_data_pipeline.TITLE,
            "keywords": ml_data_pipeline.KEYWORDS,
            "module": ml_data_pipeline
        },
        {
            "title": machine_learning_workflow.TITLE,
            "keywords": machine_learning_workflow.KEYWORDS,
            "module": machine_learning_workflow
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
            "title": mlops_pipeline.TITLE,
            "keywords": mlops_pipeline.KEYWORDS,
            "module": mlops_pipeline
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
    
    "Misc": [
         {
            "title": end_to_end_datascience.TITLE,
            "keywords": end_to_end_datascience.KEYWORDS,
            "module": end_to_end_datascience
        },
         {
           "title": data_story.TITLE,
            "keywords": data_story.KEYWORDS,
            "module": data_story  
         },
         {
            "title": api_and_business_softwares.TITLE,
            "keywords": api_and_business_softwares.KEYWORDS,
            "module": api_and_business_softwares
         },
         {
            "title": time_series_models.TITLE,
            "keywords": time_series_models.KEYWORDS,
            "module": time_series_models
         },
        {
            "title": data_preprocessing.TITLE,
            "keywords": data_preprocessing.KEYWORDS,
            "module": data_preprocessing
        },
        {
            "title": api_automation_and_security.TITLE,
            "keywords": api_automation_and_security.KEYWORDS,
            "module": api_automation_and_security
        },
        {
            "title": securing_model.TITLE,
            "keywords": securing_model.KEYWORDS,
            "module": securing_model
        },
        {
            "title": mlops_frameworks.TITLE,
            "keywords": mlops_frameworks.KEYWORDS,
            "module": mlops_frameworks
        },
        {
            "title": data_governance.TITLE,
            "keywords": data_governance.KEYWORDS,
            "module": data_governance
        },
        {
            "title": storytelling_with_data.TITLE,
            "keywords": storytelling_with_data.KEYWORDS,
            "module": storytelling_with_data
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
            "title": power_bi_report.TITLE,
            "keywords": power_bi_report.KEYWORDS,
            "module": power_bi_report
        },
        {
            "title": mlops_workflow.TITLE,
            "keywords": mlops_workflow.KEYWORDS,
            "module": mlops_workflow
        },
        {
            "title": domain_knowledge.TITLE,
            "keywords": domain_knowledge.KEYWORDS,
            "module": domain_knowledge
        }
    ]
}