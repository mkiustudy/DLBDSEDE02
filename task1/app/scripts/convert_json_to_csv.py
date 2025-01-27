import pandas as pd
import json
import os

#define paths for the source (kaggle dataset) and the target (json file for mongodb)
#Local python3 execution from project-root/app/!
base_dir = os.getcwd()
print(f"Base-Directory: {base_dir}")
csv_file = f"{base_dir}/data/iot_telemetry_data.csv"
json_file = f"{base_dir}/data/iot_telemetry_data.json"


# read csv to pandas dataframe
try:
    print("")
    print(f"Reading {csv_file}...")
    df = pd.read_csv(csv_file)
    print(f"{df.shape[0]} rows and {df.shape[1]} columns loaded from {csv_file}.")
except Exception as e:
    print("Loading failed.")
    print(f"Error: {e}")
    exit(1)

# write dataframe to json file
try:
    print("")
    print(f"Transforming to {json_file}...")
    df.to_json(json_file, orient="records", indent=4)
    print("Transformation succeeeded.")
except Exception as e:
    print("Transformation failed.")
    print(f"Error: {e}")
    exit(1)

exit(0)