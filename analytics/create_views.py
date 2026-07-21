import psycopg2
from pathlib import Path
from config.database import DATABASE_CONFIG

BASE_DIR = Path(__file__).resolve().parent
schema_file = BASE_DIR / "views.sql"

connection = psycopg2.connect(
    **DATABASE_CONFIG
)

cursor = connection.cursor()

with open(schema_file, "r") as file:
    sql_script = file.read()

cursor.execute(sql_script)
connection.commit()

cursor.close()
connection.close()

print("Views created successfully!")