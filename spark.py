from pyspark.sql import SparkSession
from pyspark import SparkContext


import pandas as pd   
import numpy as np
import os

from sqlalchemy import create_engine
from pyspark import SparkContext, SparkConf
from pyspark.sql.session import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession

if __name__ == "__main__":
    username = 'postgres'
    password = 'postgres'
    database = 'postgres'
    ip = '172.20.87.112'  

    try:
        engine = create_engine(f"postgresql://{username}:{password}@ip")
        print(f"[INFO] Success connect SPARK ENGINE .....")
    except:
        print(f"[INFO] Can't Connect SPARK ENGINE .....")

def spark_conn(app, config):
    master = config['ip']
    try:
        spark = SparkSession.builder \
            .appName(app)\
            .config("spark.jars", "postgresql-42.2.5.jar")\
            .config('spark.driver.extraClassPath','postgresql-42.2.5.jar')\
            .getOrCreate()
        df_prod = spark.read\
            .format("jdbc")\
            .option("url","jdbc:postgresql://localhost:5432/digitalskola")\
            .option("dbtable",'bigdata_transaction')\
            .option("user","postgres")\
            .option("password","postgres")\
            .load()
        print(f"[INFO] Success connect SPARK Table .....")
    
        df_prod.show(5)

        top_product=df_prod.sql("SELECT product_transaction, sum(amount_transaction) top product from bigdata_transaction")
        top_product.show(5)
    except:
        print(f"[INFO] Error Show Data .....")