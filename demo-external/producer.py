from kafka.errors import KafkaError
from kafka import KafkaProducer
from typing import Dict
import json


def message_encode(message: Dict):
    return json.dumps(message).encode('utf-8')


# # produce json messages
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'], value_serializer=message_encode)
producer.send('demo-topic', {'key': 'value'})

# # block until all async messages are sent
producer.flush()
