FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2-binary

WORKDIR /app

COPY ingest_data.py ingest_data.py
COPY yellow_tripdata_2021-01.csv.gz yellow_tripdata_2021-01.csv.gz

ENTRYPOINT [ "python", "ingest_data.py" ]
