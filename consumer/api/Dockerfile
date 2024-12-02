FROM python:3.13.0-bookworm

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN sed -i "s/localhost:27020/mongo_db:27017/" main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]