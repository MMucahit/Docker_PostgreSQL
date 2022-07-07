# Basic docker example!

This code do download dataset(Parquet) and upload to postgresql.

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
