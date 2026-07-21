from etl.extract import extract_sales_data
from etl.transform import transform_sales_data
from etl.load import load_table

def run_pipeline():
    print("Starting ETL pipeline")

    # Extract
    df = extract_sales_data()
    print("Data extracted")

    # Transform
    tables = transform_sales_data(df)
    print("Data transformed")

    # Load
    for table_name, dataframe in tables.items():
        load_table(
            dataframe,
            table_name
        )

    print("ETL completed successfully")

if __name__ == "__main__":
    run_pipeline()