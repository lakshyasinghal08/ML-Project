import os
import sys
from src.MLProject.exception import CustomException
from src.MLProject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pyodbc

load_dotenv()

server = os.getenv('server')
database = os.getenv('database')
driver = os.getenv('driver', '{ODBC Driver 17 for SQL Server}')
trusted_connection = os.getenv('trusted_connection', 'yes')

def read_sql_data():
    logging.info("Reading SQL data Started from MSSQL using Windows Authentication")
    try:
        connection_string = (
            f"DRIVER={driver};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"Trusted_Connection={trusted_connection};"
        )
        mydb = pyodbc.connect(connection_string)
        logging.info(f"connection established : {mydb}")
        
        # Note: Ensure table name matches 'Students'
        df = pd.read_sql('SELECT * FROM Students', mydb)
        print(df.head())
        
        mydb.close()
        return df
    except Exception as ex:
        raise CustomException(ex, sys)