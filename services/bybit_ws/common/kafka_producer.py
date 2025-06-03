from kafka import KafkaProducer
import json
import os

def get_kafka_producer():
    bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    print(f'bootstrap_servers - {bootstrap_servers}')
    return KafkaProducer(
        # bootstrap_servers='kafka:29092',
        # bootstrap_servers='localhost:9092',
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )