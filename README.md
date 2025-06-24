# 🚖 NYC Taxi Data Pipeline with Azure & Snowflake

## 🚀 Overview

This project demonstrates a full cloud-based data engineering pipeline for NYC Taxi data using Azure Blob Storage and Snowflake. The goal is to simulate an industry-relevant ELT process with modular, scalable components.

---

## 🔧 Tech Stack

* Python
* Azure Blob Storage
* Snowflake
* dbt (planned)
* Airflow (planned)
* SQL
* Parquet
* Pandas / PyArrow

---

## 📂 Pipeline Steps

1. Download NYC Taxi data (Parquet format)
2. Upload to Azure Blob Storage using Python
3. Create external stage in Snowflake linked to Azure Blob
4. Load data into Snowflake tables using `COPY INTO` and/or `VARIANT` staging
5. (Planned) Use dbt for data transformation
6. (Planned) Orchestrate the pipeline using Apache Airflow

---

## 📊 Project Goals

* Build an end-to-end data pipeline with cloud components
* Practice working with real-world data formats (e.g., Parquet)
* Learn Snowflake data loading strategies
* Prepare the data for downstream analytics and BI tools

---

## 🔐 Environment Setup

Create a `.env` file based on the `.env.example`. This should include your credentials for Azure and Snowflake (do not commit actual secrets).

```env
AZURE_STORAGE_CONNECTION_STRING=your_connection_string
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account_url
SNOWFLAKE_DATABASE=NYC_TAXI_DB
SNOWFLAKE_SCHEMA=RAW
SNOWFLAKE_WAREHOUSE=COMPUTE_WH
```

---

## 📊 Folder Structure

```
nyc-taxi-pipeline/
├── upload_blob.py           # Upload raw data to Azure Blob
├── load_to_snowflake.py     # Load data from Azure to Snowflake
├── dbt/                     # dbt models and config (planned)
├── dags/                    # Airflow DAGs (planned)
├── .env.example             # Example environment config
├── requirements.txt         # Python dependencies
└── README.md
```

---

## ⏳ Next Steps

* Set up dbt project and create transformation models
* Build Airflow DAG to orchestrate the pipeline
* (Optional) Add BI layer using Power BI or Streamlit

---

## 🚀 Status

* ✅ Data uploaded to Azure Blob
* ✅ Data successfully loaded into Snowflake
* ⏳ dbt setup in progress
* ⏳ Airflow orchestration planned

---

## 🧵 Follow My Progress

I'll be sharing updates and learnings as I go — follow along on LinkedIn!

\#DataEngineering #Snowflake #Azure #NYCTaxi #ELT #LearningInPublic
