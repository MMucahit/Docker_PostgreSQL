# Basic docker example!

This code do download dataset and upload to postgresql.

docker build -t taxi_ingest:v001 .

URL="https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2022-01.parquet"

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
