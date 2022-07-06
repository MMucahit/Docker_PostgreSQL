import argparse

import os

import pandas as pd 
from sqlalchemy import create_engine

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    file_name = 'output.parquet'

    os.system(f'wget {url} -O {file_name}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    df = pd.read_parquet(file_name)
    
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

    df.to_sql(con=engine, name=table_name, if_exists='replace')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='User name for Postgres')
    parser.add_argument('--password', help='Password for Postgres')
    parser.add_argument('--host', help='Host for Postgres')
    parser.add_argument('--port', help='Port for Postgres')
    parser.add_argument('--db', help='Database name for Postgres')
    parser.add_argument('--table_name', help='Name of the table')
    parser.add_argument('--url', help='Url of the csv file')

    args = parser.parse_args()

    main(args)