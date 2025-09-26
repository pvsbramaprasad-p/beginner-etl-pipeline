import argparse
import logging
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("etl")

def extract_csv(path_or_url: str) -> pd.DataFrame:
    logger.info(f"Extracting data from {path_or_url}")
    return pd.read_csv(path_or_url)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming dataframe")
    
    df.columns = [c.strip().lower() for c in df.columns]

    df = df.drop_duplicates(subset=["id"])

    df["name"] = df["name"].fillna("Unknown")
    df["city"] = df["city"].fillna("Unknown")
    df["age"] = df["age"].fillna(df["age"].median())
    df["score"] = df["score"].fillna(df["score"].mean())

    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

    return df

def load_to_sqlite(df: pd.DataFrame, db_path: str, table: str):
    logger.info("Loading to sqlite db=%s table=%s", db_path, table)
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql(table, engine, if_exists="replace", index=False)
    logger.info("Loaded %d rows", len(df))

def main(args):
    df = extract_csv(args.source)
    df = transform(df)
    load_to_sqlite(df, args.db, args.table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/medium_sample.csv")
    parser.add_argument("--db", default="data/etl.db")
    parser.add_argument("--table", default="users")
    main(parser.parse_args())