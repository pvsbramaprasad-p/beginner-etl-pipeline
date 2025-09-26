# ETL Pipeline Project

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python. The pipeline reads data from a CSV file, processes/transforms the data, and loads it into a SQLite database.

## Project Structure

```
requirements.txt         # Python dependencies
src/
  etl_pipeline.py        # Main ETL pipeline script
  query_db.py            # Script to query the database

data/
  medium_sample.csv      # Sample input data (CSV)
  etl.db                 # SQLite database file

tests/
  test_etl.py            # Unit tests for the ETL pipeline
```

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd beginner-etl-pipeline
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the ETL Pipeline
Run the ETL pipeline to process the CSV and load data into the SQLite database:
```sh
python src/etl_pipeline.py --source data/medium_sample.csv --db data/etl.db --table users
```

### Querying the Database
You can query the loaded data using:
```sh
python src/query_db.py
```

### Running Tests
To run the unit tests:
```sh
python -m unittest discover tests
```

## License
This project is for educational purposes.
