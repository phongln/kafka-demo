from kafka import KafkaConsumer
from json import loads
import addressbook_pb2
import sys

address_book = addressbook_pb2.AddressBook()


def parseMess(person):
    parsePerson = address_book.ParseFromString(person)
    for person in address_book.people:
        print(person)
        print(person.phones)


consumer = KafkaConsumer(
    'demo-topic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-1',
    value_deserializer=parseMess,
    bootstrap_servers=['localhost:9092'])

for m in consumer:
    print(m.value)
