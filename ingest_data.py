import argparse
import pandas as pd
from sqlalchemy import create_engine
from time import time 

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    
    csv_name = 'yellow_tripdata_2021-01.csv.gz'

    db_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    engine = create_engine(db_url)
    engine.connect()
    print("connect access")

    df_iter = pd.read_csv(csv_name, iterator= True, chunksize=100000)
    
    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')
    print("First part download")


    while True:
        try:
            t_start = time()
            
            df = next(df_iter)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name= table_name, con=engine, if_exists='append')

            t_end = time()
            print(f"part added {t_end - t_start:.3f}")


        except StopIteration:
            print("data loaded")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest csv data to Postgres')
    
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')

    args = parser.parse_args(
    )

    main(args)