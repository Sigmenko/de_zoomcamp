import os
import argparse
from time import time
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
    
    # Визначаємо назву файлу з URL (наприклад output.csv.gz)
    csv_name = 'output.csv.gz'

    # 1. Скачуємо файл
    print(f"⬇️ Качаю файл з {url}...")
    os.system(f"wget {url} -O {csv_name}")

    # 2. Підключаємось до бази
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # 3. Читаємо файл шматками (iterator=True)
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # Беремо перший шматок, щоб створити таблицю
    df = next(df_iter)

    # Конвертуємо дати з тексту в формат часу
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Створюємо таблицю (заголовки)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Заливаємо перший шматок
    df.to_sql(name=table_name, con=engine, if_exists='append')

    print("✅ Перший шматок залетів! Продовжуємо...")

    # 4. Цикл для решти шматків
    while True: 
        try:
            t_start = time()
            
            df = next(df_iter)

            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))

        except StopIteration:
            print("🎉 Фух, все завантажили!")
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)