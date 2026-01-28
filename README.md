#  Delhi Metro ETL Pipeline

##  Project Overview

This project implements an **ETL (Extract–Transform–Load) pipeline** for **Delhi Metro data** using publicly available DMRC backend APIs.

The pipeline dynamically fetches:

* **Station metadata** (location, facilities, connectivity)
* **Route & fare information** between stations

The transformed data is stored as **CSV files** for analytics, reporting, or downstream ingestion into databases or BI tools.

---

## Objectives

* Fetch **station codes dynamically** instead of hardcoding
* Extract **detailed station-level attributes**
* Extract **route-level metrics** such as:

  * Fare
  * Total travel time
  * Number of stations
  * Platform, direction, and timings
* Store clean, normalized datasets
* Follow **real-world ETL best practices**

---

## 🧱 Project Architecture (ETL Flow)

```
Delhi Metro APIs
      ↓
[Extract]
- Station by Line API
- Station Detail API
- Station Route API
      ↓
[Transform]
- Normalize nested JSON
- Handle inconsistent data types
- Derive features (lift/escalator availability, previous/next station)
      ↓
[Load]
- stations.csv
- metro_routes_data.csv
```

---

## 🌐 APIs Used

### 1️⃣ Station Codes by Line

Fetches all station codes dynamically for a metro line.

```
GET https://backend.delhimetrorail.com/api/v2/en/station_by_line_linepage/LN11
```

---

### 2️⃣ Station Details

Fetches complete information about a station.

```
GET https://backend.delhimetrorail.com/api/v2/en/station/{station_code}
```

**Extracted Fields**

* Station name & type
* Latitude / Longitude
* Line color
* Lift & escalator availability
* Parking availability
* Previous & next station
* Interchange status
* Landline number

---

### 3️⃣ Station Route & Fare

Fetches fare, travel time, and route details between two stations.

```
GET https://backend.delhimetrorail.com/api/v2/en/station_route/{FROM}/{TO}/least-distance/{timestamp}
```

**Extracted Fields**

* Fare
* Total travel time
* Number of stations
* Line name
* Platform number
* Direction & destination
* First & last train time
* Station status

---

## 📂 Project Structure

```
delhi_metro_etl/
│
├── src/
│   ├── station_etl.py        # Station-level ETL
│   ├── route_etl.py          # Route & fare ETL
│
├── output/
│   ├── stations.csv
│   ├── metro_routes_data.csv
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Requests** – API calls
* **Pandas** – Data transformation & CSV output
* **Datetime** – Dynamic timestamps

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/delhi_metro_etl.git
cd delhi_metro_etl
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
requests
pandas
```

---

### 4️⃣ Run Station ETL

```bash
python src/station_etl.py
```

✔ Generates:
`stations.csv`

---

### 5️⃣ Run Route & Fare ETL

```bash
python src/route_etl.py
```

✔ Generates:
`metro_routes_data.csv`

---

## 📊 Output Files

### 🗂️ stations.csv

Contains one row per station with:

* Coordinates
* Facilities (lift, escalator, parking)
* Connectivity (previous/next station)
* Line & interchange info

---

### 🗂️ metro_routes_data.csv

Contains one row per **station pair** with:

* Fare
* Travel time
* Number of stations
* Platform & direction
* First & last train timings

---


## 👤 Author

**Daksh Yadav**
Data Engineering Intern
Delhi Metro ETL Assignment


