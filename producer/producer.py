from kafka import KafkaProducer
import json
import time

# Kafka Config
BROKER = "localhost:9092"
TOPIC = "data_topic"
print("started", flush = True)
time.sleep(10)
# Initialize producer
producer = KafkaProducer(
    bootstrap_servers=BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_data():
    # Example JSON data
    return {
        "user_id": 123,
        "timestamp": time.time(),
        "action": "login",
        "details": "User logged in successfully"
    }

if __name__ == "__main__":
    print("Starting Kafka Producer...")
    while True:
        data = generate_data()
        producer.send(TOPIC, value=data)
        print(f"Sent: {data}", flush = True)
        time.sleep(30)  # Send a message every 30 second
