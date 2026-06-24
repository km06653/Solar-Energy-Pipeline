import pandas as pd


def inspect_data(df):
    """
    Inspect raw dataset quality before transformation.

    Args:
        df (DataFrame): Raw solar data
    """

    print("\n--- DATA PREVIEW ---")
    print(df.head())


    print("\n--- DATA TYPES ---")
    print(df.dtypes)


    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())


    print("\n--- DUPLICATE ROWS ---")
    print(df.duplicated().sum())


    print("\n--- BASIC STATISTICS ---")
    print(df.describe())



def clean_solar_data(df):
    """
    Clean and standardize solar generation data.

    Returns:
        Clean DataFrame
    """


    # Protect original raw data
    clean_df = df.copy()


    # Standardize column names for database
    clean_df.columns = (
        clean_df.columns
        .str.lower()
        .str.strip()
    )


    # Convert timestamp column
    clean_df["date_time"] = pd.to_datetime(
        clean_df["date_time"],
        errors="coerce"
    )


    # Remove duplicate sensor readings
    clean_df = clean_df.drop_duplicates()


    # Validate solar measurements
    clean_df = clean_df[
        clean_df["dc_power"] >= 0
    ]


    clean_df = clean_df[
        clean_df["ac_power"] >= 0
    ]


    # Create engineering metric
    clean_df["conversion_efficiency"] = (
        clean_df["ac_power"] /
        clean_df["dc_power"]
    )


    # Replace invalid calculations
    clean_df.replace(
        [float("inf"), -float("inf")],
        0,
        inplace=True
    )


    # Handle missing values
    clean_df.fillna(
        0,
        inplace=True
    )


    print("\nTransformation completed")
    print(f"Clean rows: {len(clean_df)}")


    return clean_df



if __name__ == "__main__":

    file_path = "data/raw/Plant_1_Generation_Data.csv"


    # Extract raw data
    df = pd.read_csv(file_path)


    # Inspect
    inspect_data(df)


    # Transform
    clean_df = clean_solar_data(df)


    # Save processed output
    clean_df.to_csv(
        "data/processed/clean_solar_data.csv",
        index=False
    )


    print("\n--- CLEAN DATA ---")
    print(clean_df.head())
