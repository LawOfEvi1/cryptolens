from kafka import KafkaProducer
import json

def get_kafka_producer():
    return KafkaProducer(
        # bootstrap_servers='kafka:29092',
        bootstrap_servers='localhost:9092',
        value_serializer=lambda m: json.dumps(m).encode('utf-8')
    )