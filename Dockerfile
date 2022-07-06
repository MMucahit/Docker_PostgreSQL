FROM python:3.6.8

RUN pip3 install --upgrade pip==20.0.1

RUN apt-get install wget

RUN pip install pandas sqlalchemy psycopg2 fastparquet

WORKDIR /app
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]
