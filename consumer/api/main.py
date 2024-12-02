from fastapi import FastAPI, Query
from pymongo import MongoClient
from typing import Optional, List

# MongoDB Config
MONGO_URI = "mongodb://localhost:27020/"
DB_NAME = "pipeline_db"
COLLECTION_NAME = "data_collection"

# Initialize MongoDB client
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Data Pipeline API"}

@app.get("/data")
def get_all_data(limit: int = 10):
    """
    Retrieve all data from MongoDB with a limit on the number of documents.
    """
    data = list(collection.find().limit(limit))
    for item in data:
        item["_id"] = str(item["_id"])  # Convert ObjectId to string
    return {"data": data}

@app.get("/data/filter")
def filter_data(
    sentiment_label: Optional[str] = Query(None, description="Filter by sentiment label (e.g., POSITIVE, NEGATIVE)"),
    user_id: Optional[int] = Query(None, description="Filter by user ID"),
    limit: int = 10
):
    """
    Retrieve filtered data based on sentiment label or user ID.
    """
    query = {}
    if sentiment_label:
        query["sentiment.label"] = sentiment_label
    if user_id:
        query["user_id"] = user_id

    data = list(collection.find(query).limit(limit))
    for item in data:
        item["_id"] = str(item["_id"])  # Convert ObjectId to string
    return {"data": data}
