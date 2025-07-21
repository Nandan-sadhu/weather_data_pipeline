# 🌦️ Weather Data Pipeline
An end-to-end Python pipeline that fetches hourly weather data from a public API, processes it using Pandas, and stores the results in both a local SQLite database and Parquet format. Ideal for practicing data engineering concepts such as data ingestion, transformation, and storage.


Repository Name: weather_data_pipeline

🔸 Description:
An end-to-end Python pipeline that fetches hourly weather data from a public API, processes it using Pandas, and stores the results in both a local SQLite database and Parquet format. Ideal for practicing data engineering concepts such as data ingestion, transformation, and storage.

---

## 🚀 Features

- ✅ Fetches hourly weather data using an open API  
- ✅ Transforms and cleans the data using `pandas`  
- ✅ Saves data to:
  - Local SQLite database (`weather.db`)
  - Parquet file (`data/processed/weather.parquet`)  
- ✅ Modular pipeline structure (ETL style)
- ✅ Data exploration script included

---

## 🏗️ Project Structure

weather_data_pipeline/
│
├── data/                       # Raw and processed data
│   ├── raw/
│   └── processed/
│
├── logs/                       # Log files
│
├── config/                     # API keys, DB creds
│   └── config.env
│
├── pipeline/                   # Core ETL code
│   ├── __init__.py
│   ├── ingest.py               # API calls
│   ├── transform.py            # Clean & transform data
│   ├── load.py                 # Save to DB / Parquet
│
├── requirements.txt            # Python dependencies
├── run_pipeline.py             # Main script to run pipeline
├── explore_data.py             # analyze saved weather data:
└── README.md                   # Project overview

# Requirements
Python 3.10+
Libraries:
pandas
requests
sqlalchemy
pyarrow or fastparquet

🌐 API Used
Open-Meteo: https://open-meteo.com/
Free weather API (no authentication required)



