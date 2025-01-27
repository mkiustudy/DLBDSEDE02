#!/bin/bash
#Startup Script for transforming CSV to JSON and importing JSON to MongoDB
set -e

echo "Starting CSV to JSON transformation..."
python3 /app/scripts/convert_json_to_csv.py
echo "Succeeded in transforming CSV to JSON."

echo "Importing JSON to mongoDB collection..."
python3 /app/scripts/import_json_to_mongo.py
echo "Succeeded in importing JSON to mongoDB collection."

echo "Startup script completed successfully."