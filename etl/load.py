import pandas as pd
from sqlalchemy import create_engine
from config.database import DATABASE_CONFIG

def create_connection():
    engine = create_engine(
        f"postgresql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}"
        f"@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}"
        f"/{DATABASE_CONFIG['database']}"
    )
    return engine

def load_table(df: pd.DataFrame, table_name: str):
    engine = create_connection()
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )
    print(f"Loaded table: {table_name}")