import pandas as pd
from pathlib import Path

def extract_sales_data() -> pd.DataFrame:
    file_path = (
        Path(__file__)
        .resolve()
        .parent.parent
        / "data"
        / "raw"
        / "sales.csv"
    )
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = extract_sales_data()

    print(df.head())
    print("\nColumns:")
    print(df.columns)