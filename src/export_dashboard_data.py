import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine


def export_dashboard_data():

    """
    Export cleaned PostgreSQL data for dashboard analytics.
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


    query = """

    SELECT
        date_time,
        source_key,
        dc_power,
        ac_power,
        daily_yield,
        total_yield,
        conversion_efficiency

    FROM solar_measurements;

    """


    df = pd.read_sql(
        query,
        engine
    )


    df.to_csv(
        "dashboards/solar_dashboard_data.csv",
        index=False
    )


    print(
        f"Exported {len(df)} rows for dashboard analytics"
    )



if __name__ == "__main__":

    export_dashboard_data()
