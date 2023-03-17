import os

DATABASE_USER = "root"
DATABASE_PASSWORD = os.getenv"dattebayo_002"
DATABASE_HOST = "localhost"
DATABASE_NAME = "car_db"
CSV_FILE_NAME = "MASHINA_KG.csv"

# Ссылка на базу данных
MYSQL_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
