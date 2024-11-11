#!/bin/bash

# DB
DB_NAME="geotiff_viewer"
DB_USER="postgres"
DB_HOST="localhost"
DB_PORT="5432"
SCHEMA="public"

#path to my EVI tiffs
TIFF_DIR="/mnt/c/Users/pfrid/PycharmProjects/data_viz/data/EVI"

# loop tiffs in folder
for file in "$TIFF_DIR"/*.tif; do
    echo "Importujem súbor: $file"
    
    # extract namee without ext.
    filename=$(basename "$file" .tif)
    
    #import to DB
    raster2pgsql -s 4326 -I -C -M "$file" "$SCHEMA.$filename" | psql -U $DB_USER -d $DB_NAME -h $DB_HOST -p $DB_PORT
    
    echo "Dokončené: $filename"
done
