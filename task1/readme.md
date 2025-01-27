# Project DLBDSEDE02

## Project Description
The objective of this project is to store IoT telemetry data in batches within a suitable database that operates independently of the host system and is transferrable. The database must be capable of handling schema drifts and variations in column datatypes, as the telemetry data may change over time. The overall system should be scalable, reliable, and maintainable, with the setup versioned in a repository such as GitHub.

The kaggle-dataset "Environmental Sensor Telemetry Data" by Gary A. Stafford `https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k` is used for this project includes metrics like temperature, smoke density, humidity and carbon dioxide from various IoT sensors. It spans 405,184 rows and covers the period from July 12, 2020, 00:00:00 UTC to July 19, 2020, 23:59:59 UTC.

To achieve host-system independence, Docker containerization will utilize the official DockerHub image for MongoDB. Typically, database data is stored as a volume outside the container and is not erased during a restart. In this prototype, the database and IoT dataset need to be included and imported automatically when the container boots. 

Since the source data is provided as a .CSV file, it must be transformed into a JSON structure first and then imported into the MongoDB server. This will use a custom Docker image with Python scripts for transformation and loading. 

Additionally, MongoDB-Express will be used to provide a lightweight web frontend to the MongoDB server for querying and troubleshooting data.


## Installation
To install the project, follow these steps:
1. Clone the repository: `git clone https://github.com/mkiustudy/DLBDSEDE02`
2. Navigate to the project directory: `cd DLBDSEDE02`

## Usage
After installation, you can use the project as follows:
1. Download and install Docker, if neccessary `https://docs.docker.com/get-started/get-docker/`
1. Compose and start this repository by `docker-compose build --no-cache && docker-compose up -d`
2. Open your browser and navigate to `http://localhost:8081/db/sensor_data/iot_telemetry_data`
3. Browse the kaggle dataset imported to mongodb sensor_data.iot_telemetry_data collection

## Contributors
- Martin Kalusa

## License
