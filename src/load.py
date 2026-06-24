import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine



def load_to_postgres(df):
    """
    Load cleaned solar data into PostgreSQL database.

    Args:
        df (DataFrame): Clean solar data
    """


    load_dotenv()


    database = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")


    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{database}"
    )


    df.to_sql(
        "solar_measurements",
        engine,
        if_exists="append",
        index=False
    )


    print(
        f"Loaded {len(df)} records into PostgreSQL"
    )



if __name__ == "__main__":


    file_path = (
        "data/processed/clean_solar_data.csv"
    )


    df = pd.read_csv(file_path)


    load_to_postgres(df)

