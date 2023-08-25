from sqlalchemy import create_engine
import pandas as pd
import os

pwd = 'your password'
uid = 'your user id (by default postgre)'
server = "localhost"
db = "database name"
port = "5432"
dir = r'path\To\the\folder\jumia_ETL'

def extract():
    try:
        directory = dir
        for filename in os.listdir(directory):
            file_wo_ext = os.path.splitext(filename)[0]
            if filename.endswith(".xlsx"):
                f = os.path.join(directory, filename)
                if os.path.isfile(f):
                    df = pd.read_excel(f)
                    load(df, file_wo_ext)
    except Exception as e:
        print("Data extract error: " + str(e))

def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... ')
        df.to_sql(f"{tbl}", engine, if_exists='replace', index=False)
        rows_imported += len(df)
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))