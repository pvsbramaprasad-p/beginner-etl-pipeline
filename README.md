# Beginner ETL Pipeline with Python

This project demonstrates a **basic ETL (Extract, Transform, Load) pipeline** built in Python.  

It ingests a CSV dataset, applies cleaning & transformations, and loads the results into a SQLite database.

---

## Features
- **Extract**: Read raw data from a CSV file (`medium_sample.csv` with 1000 rows).  
- **Transform**:  
  - Standardizes column names  
  - Removes duplicates  
  - Handles missing values  
  - Converts dates and enforces proper data types  
- **Load**: Writes the cleaned dataset into a SQLite database (`etl.db`).  
- **Testing**: Unit tests for transformations (`pytest`).  
- **Logging**: Console logging for visibility into ETL steps.  

---
