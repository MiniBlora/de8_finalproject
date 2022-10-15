#!python3

import pandas as pd
import numpy as np

from sqlalchemy import create_engine

if __name__ == "__main__":
    username = 'postgres'
    password = 'postgres'
    database = 'postgres'
    ip = 'localhost'

    try:
        engine = create_engine(f"postgresql://postgres:postgres@localhost:5432/postgres")
        print(f"[INFO] Success Connect PostgreSQL .....")
    except:
        print(f"[INFO] Error Connect PostgreSQL ...")
    list_filename =['customer','product','transaction']
    for file in list_filename:
        print(file)
        pd.read_csv(f"bigdata_{file}.csv").to_sql(f"bigdata_{file}", con=engine)
        print(f"[INFO] Success Dump {file} .....")
