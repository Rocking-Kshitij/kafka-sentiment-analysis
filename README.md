# Project Name

## Description
Distributed systems using kafka fastapi and docker

This project is a kafka based application which creates:
- Dockerized kafka server
- Dockerized producer which sends data to topic
- A dockerized receiver which gets the data, does sentiment analysis and stores it to db. Then a fastapi app provides the endpoints

fastapi url: localhost:8000/
Example:
    - http://localhost:8000/data/filter?sentiment_label=POSITIVE
mongodb url: mongodb://localhost:27020/


## Directory
- Kafka/
    - docker-compose.yml
- producer/
    - docker-compose.yml
- consumer/
    - api/
    - consumer-app/
    - database/
    - docker-compose.yml

## Installation
   ```bash
   docker compose -f ./kafka/docker-compose.yml up -d --build
   docker compose -f ./producer/docker-compose.yml up -d --build
   docker compose -f ./consumer/docker-compose.yml up -d --build
