# ETL Pipeline – JSONPlaceholder Users API

## 📌 Project Overview

This project implements a **production-style ETL (Extract, Transform, Load) pipeline** using Python. The pipeline extracts user data from a public API, cleans and validates it, stores it in a relational database (SQLite), and generates meaningful business insights using SQL.

The project is intentionally designed to handle **real-world data engineering concerns** such as unreliable APIs, nested JSON transformation, data validation, logging, and schema-aware analytics.

---

## 🏗️ Overall Architecture

```
API (JSONPlaceholder)
        ↓
Extract (Python + Requests)
        ↓
Transform & Clean (Pandas)
        ↓
Validate Data
        ↓
Save CSV
        ↓
Load into SQLite
        ↓
Run SQL Business Insights
```

---

## 🔗 Data Source

* **API**: [https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users)
* **Format**: Nested JSON
* **Records**: 10 users

---

## 📂 Project Structure

```
etl_pipeline/
│
├── main.py            # Pipeline orchestrator
├── extract.py         # API extraction with retry & timeout handling
├── transform.py       # JSON flattening & transformation
├── validate.py        # Data quality rules
├── load.py            # CSV export & SQLite insertion
├── insights.py        # SQL-based business insights
├── logger.py          # Centralized logging configuration
├── users.db           # SQLite database (auto-created)
├── users_clean.csv    # Cleaned dataset (auto-generated)
└── README.md
```

---

## ⚙️ Technologies Used

* **Python 3**
* **Requests** – API calls
* **Pandas** – Data transformation
* **SQLite** – Relational database
* **SQL** – Business insights
* **Logging** – Pipeline observability

---

## ✅ Data Validation Rules

| Rule                | Action |
| ------------------- | ------ |
| Duplicate `user_id` | Reject |
| Email without `@`   | Reject |
| City is NULL        | Reject |
| Zipcode length < 5  | Reject |

Invalid records are **excluded** from downstream processing to maintain data quality.

---

## 🔄 Transformation Highlights

* Flattens nested JSON fields (`address`, `geo`, `company`)
* Standardizes column naming
* Extracts latitude & longitude for geo insights
* Produces a structured tabular dataset

---

## 🗄️ Database Schema (`users` table)

| Column       | Description            |
| ------------ | ---------------------- |
| user_id      | Unique user identifier |
| name         | User full name         |
| username     | Username               |
| email        | Email address          |
| city         | City name              |
| zipcode      | Postal code            |
| phone_no     | Phone number           |
| website      | Website                |
| company_name | Company name           |
| latitude     | Geographic latitude    |
| longitude    | Geographic longitude   |

---

## 📊 Business Insights Generated

The pipeline generates insights using **pure SQL**, including:

1. Total valid users
2. Users per company
3. Users per city
4. Users per city per company
5. Phone number coverage
6. Email vs website domain mismatch
7. Hemisphere distribution (Northern vs Southern)
8. Email domain classification (Work vs Personal)
9. Website domain distribution (.com, .org, .net, etc.)

These insights are designed to handle **high-cardinality datasets** where naive aggregation would be misleading.

---

## 🧠 Key Design Decisions

* **Fail-fast extraction**: Pipeline stops if API extraction fails
* **Retry & timeout handling** for unreliable APIs
* **Schema-aware analytics** to avoid invalid assumptions
* **Pattern-based insights** instead of fake aggregation

---

## ▶️ How to Run

### 1️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install dependencies

```bash
pip install requests pandas
```

### 3️⃣ Run the pipeline

```bash
python main.py
```

SQLite database and CSV will be generated automatically.

---

## 🧪 Example Use Cases

* ETL pipeline demonstration
* Data engineering portfolio project
* SQL analytics practice
* API-to-database ingestion

---

## 📌 Notes

* This project uses a **public demo API**; data values are synthetic
* Designed for **clarity, correctness, and interview readiness**

---

## 👤 Author

Daksh Yadav
*Data Engineering / ETL Pipeline Project*

---


