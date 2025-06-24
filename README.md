# NYC Taxi Trip Pipeline and Dashboard

## Introduction

This project is an **end‑to‑end data engineering and analytics solution** for NYC Taxi Trip data.
It demonstrates extracting, loading, transforming, and visualizing data across modern data platforms:

* **Azure Blob Storage** for raw data
* **Snowflake** for storage and analytics
* **dbt** for data modeling
* **Power BI** for interactive dashboards
* **Future**: Apache Airflow for orchestration

> Currently, the project is fully functional for ingestion, modeling, and dashboards. Apache Airflow will be added in the future.

---

## Features

- Azure Blob Storage as the data lake
- Snowflake as the data warehouse
- dbt for data modeling and transformations
- Power BI for interactive dashboards
- Apache Airflow for orchestration (Planned)

---

## 🗂️ Project Architecture

```
├─ 📁 dags/                # Apache Airflow DAG files (Planned)
├─ 📁 dashboard/           # Power BI .pbix files
├─ 📁 data/                # Source data files
├─ 📁 dbt_nyc_yellow/      # dbt project (models, seeds, snapshots, schema.yml, etc.)
├─ 📁 docker/              # Dockerfiles, docker compose
├─ 📁 scripts/             # Scripts for data upload and utilities
├─ 📁 logs/                # Logs for dbt, future airflow
├─ .gitignore              # Git ignore rules
├─ requirements.txt        # Python dependencies
├─ README.md               # Project readme
```

---

## 🛠️ Technologies

* **Python 3.9+**
* **Azure Blob Storage**
* **Snowflake**
* **dbt**
* **Power BI**
* **Apache Airflow (Future)**

---

## Getting Started

### Prerequisites

* Python 3.9+
* Snowflake account
* Azure Blob Storage account
* dbt
* Power BI
* `.env` files configured Azure Connection

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run dbt Models

```bash
cd dbt_nyc_yellow
dbt run
```

### View the Dashboard

Open the `.pbix` files located in the `dashboard/` directory.

---

## Created By

**Rizky Zaqi Megantara**
[LinkedIn](https://www.linkedin.com/in/zaqi-megantara-4989ab2a2/) | [GitHub](https://github.com/zaqimegantara)

---

