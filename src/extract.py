import pandas as pd


def extract_csv(file_path):
    """
    Extract raw solar data from CSV file.

    Args:
        file_path (str): Location of raw CSV file

    Returns:
        pandas.DataFrame: Raw solar dataset
    """

    try:
        data = pd.read_csv(file_path)

        print("Data extraction successful")
        print(f"Rows extracted: {len(data)}")
        print(f"Columns found: {len(data.columns)}")

        return data


    except FileNotFoundError:
        print("ERROR: File not found")
        return None


    except Exception as error:
        print(f"Extraction failed: {error}")
        return None



if __name__ == "__main__":

    file_path = "data/raw/Plant_1_Generation_Data.csv"

    df = extract_csv(file_path)

    if df is not None:
        print(df.head())
