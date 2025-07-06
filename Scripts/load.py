import os
import pandas as pd
from dotenv import load_dotenv


#First load data to csv
def load_tocsv(df):
    df.to_csv("Data/records_random_api.csv", index=False)
    print("Data loaded to csv")


load_dotenv()

def load_to_postgres(df, table_name):
    DB_USER = os.getenv("POSTGRES_USER")
    DB_PASS = os.getenv("POSTGRES_PASS")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

   
