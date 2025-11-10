FROM python:3.12-slim

WORKDIR /app
RUN apt-get update && apt-get install -y git && apt-get clean

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir || true

COPY . /app
