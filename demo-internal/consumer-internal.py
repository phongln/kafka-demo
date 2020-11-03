from kafka import KafkaConsumer
from json import loads
# import sys

consumer = KafkaConsumer(
    'demo-topic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-1',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['kafka:9093'])

for m in consumer:
    print(m.value)
