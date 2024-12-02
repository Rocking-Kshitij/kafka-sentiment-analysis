from kafka import KafkaConsumer
from pymongo import MongoClient
from transformers import pipeline
import json
import os

# Kafka Config
BROKER = "localhost:9092"
TOPIC = "data_topic"


# MongoDB Config

MONGO_URI = f"mongodb://localhost:27020/"
print(f"Connecting via {MONGO_URI}", flush = True)
DB_NAME = "pipeline_db"
COLLECTION_NAME = "data_collection"

# Initialize MongoDB client
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]

# Initialize Kafka consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BROKER,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Initialize Sentiment Analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

if __name__ == "__main__":
    print("Starting Kafka Consumer with AI Integration...")
    for message in consumer:
        data = message.value
        print(f"Received: {data}", flush = True)

        # Perform sentiment analysis on the "details" field
        if "details" in data:
            sentiment = sentiment_analyzer(data["details"])[0]
            data["sentiment"] = {
                "label": sentiment["label"],
                "score": sentiment["score"]
            }
            print(f"Sentiment Analysis: {data['sentiment']}", flush = True)

        # Insert enhanced data into MongoDB
        collection.insert_one(data)
        print("Data with sentiment stored in MongoDB.", flush = True)
