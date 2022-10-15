import pandas as pd
import numpy as np

from sqlalchemy import create_engine

if __name__ == "__main__":
    username = 'postgres'
    password = 'POST1234'
    database = 'postgres'
    ip = '172.27.214.55'

    try:
        engine = create_engine(f"postgresql://{username}:{password}@{ip}:5432/postgres")
        print(f"[INFO] Sukses konek postgresSQL...")
    except:
        print(f"[INFO] Gagal konek postgresSQL...")

    listf_filename = ['customer','product','transaction']
    for file in listf_filename:
        pd.read_csv(f"bigdata_{file}.csv").to_sql(f"bigdata_{file}", con=engine)
        print(f"[INFO] sukses Dump File {file}....")