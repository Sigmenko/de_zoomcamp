FROM python:3.9

RUN apt-get update && apt-get install -y wget 

WORKDIR /app

RUN pip install pandas sqlalchemy psycopg2

COPY ingest_data.py ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]