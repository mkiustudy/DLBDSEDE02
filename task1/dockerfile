FROM python:3.11

# Set container working directory
WORKDIR /app

# Install python dependencies via pip
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy local data to container
COPY ./app/scripts /app/scripts
COPY ./app/data /app/data

# Initialize the startup script
CMD ["bash", "/app/scripts/start.sh"]
