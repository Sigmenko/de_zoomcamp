# NYC Taxi Data Pipeline 🚖

Цей проєкт — частина курсу Data Engineering Zoomcamp.
Я побудував ETL пайплайн, який забирає дані про поїздки таксі в Нью-Йорку, обробляє їх і кладе в Data Warehouse.

## 🛠 Технології
* **Google Cloud Platform:** GCS (Data Lake), BigQuery (DWH).
* **Infrastructure as Code:** Terraform.
* **Containerization:** Docker & Docker Compose.
* **Language:** Python (Pandas, SQLAlchemy).
* **Database:** PostgreSQL.

## 🚀 Як це працює
1. **Terraform** розгортає інфраструктуру в хмарі (Bucket + Dataset).
2. **Docker Compose** піднімає локальну базу даних Postgres та pgAdmin.
3. **Python-скрипт** завантажує дані, очищує їх та зберігає в базу.