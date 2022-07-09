This code do download dataset(Parquet) and upload to postgresql.

Firstly, you should run in postgresql and pg-admin.
You can follow postgresql-pgadmin files.

docker build -t taxi_ingest:v001 .

URL=""

sudo docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL}
