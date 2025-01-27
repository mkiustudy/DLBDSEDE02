import pymongo
import json
import os


#define paths for the transformed json file and the target mongodb collection
#Local python3 execution from project-root/app/!
base_dir = os.getcwd()
print(f"Base-Directory: {base_dir}")
var_json_file = f"{base_dir}/data/iot_telemetry_data.json"
var_db_name = "sensor_data"
var_collection_name = "iot_telemetry_data"

# local debugging only
#var_json_file = "/Users/martinkalusa/Desktop/Studium/Projekte/DLBDSEDE02/app/data/iot_telemetry_data.json"

# Connect to mongodb server
try:
    mongo_uri = os.getenv("MONGO_URI", "mongodb://root:example@localhost:27017/")
    client = pymongo.MongoClient(mongo_uri)
    db = client[var_db_name]
    collection = db[var_collection_name]
    print("Connected to MongoDB.")
except Exception as e:
    print("Failed to connect to MongoDB.")
    print(f"Error: {e}")
    exit(1)

# Load data from JSON file, created in the previous step
try:
    with open(var_json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"{len(data)} documents loadad from {var_json_file}")
except Exception as e:
    print("Failed to open JSON file.")
    print(f"Error: {e}")
    exit(1)

# Insert data to mongodb collection
try:
    if isinstance(data, list):
        collection.insert_many(data)
        print(f"{len(data)} documents inserted to MongoDB {var_db_name}.{var_collection_name}")
except Exception as e:
    print("Failed to insert documents into MongoDB.")
    print(f"Error: {e}")
finally:
    #anyway, close the connection to mongodb
    client.close()

exit(0)

