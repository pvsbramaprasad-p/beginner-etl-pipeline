import pandas as pd
from src.etl_pipeline import transform

def test_transform_removes_empty_rows():
    df = pd.DataFrame({"id": [1, None], "name": ["Alice", None]})
    result = transform(df)
    # No fully empty rows
    assert not result.isnull().all(axis=1).any()
    # Columns are lowercase
    assert all(c.islower() for c in result.columns)
