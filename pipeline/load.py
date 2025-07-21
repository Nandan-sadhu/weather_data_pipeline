import pandas as pd
import os
from sqlalchemy import create_engine

def save_to_db(df, db_path="sqlite:///weather.db"):
    engine = create_engine(db_path)
    df.to_sql('weather_data', con=engine, if_exists='append', index=False)

def save_to_parquet(df, path="data/processed/weather.parquet"):
    if os.path.exists(path):
        old_df = pd.read_parquet(path)
        df = pd.concat([old_df, df], ignore_index=True)

    df.to_parquet(path, index=False)