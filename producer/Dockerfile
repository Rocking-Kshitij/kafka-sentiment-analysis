FROM python:3.13.0-bookworm

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# RUN sed -i "s/localhost/kafka/" producer.py
RUN sed -i "s/localhost:9092/host.docker.internal:9092/" producer.py
# RUN sed -i "s/localhost:9092/kafka:9092/" producer.py

# Set the default command to run the Python script
CMD ["python", "producer.py"]
