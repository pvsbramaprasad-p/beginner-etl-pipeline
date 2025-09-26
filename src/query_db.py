import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database (same path as ETL pipeline)
engine = create_engine("sqlite:///data/etl.db")

# 1. Count rows in 'users' table
df_count = pd.read_sql("SELECT COUNT(*) as row_count FROM users;", engine)
print("\n Row count in users table:")
print(df_count)

# 2. Preview first 10 rows
df_preview = pd.read_sql("SELECT * FROM users LIMIT 10;", engine)
print("\n Preview of users table:")
print(df_preview)

# 3. Example: average score by city
df_avg = pd.read_sql("""
    SELECT city, AVG(score) as avg_score
    FROM users
    GROUP BY city
    ORDER BY avg_score DESC;
""", engine)
print("\n Average score by city:")
print(df_avg)