import addressbook_pb2
import sys
from kafka.errors import KafkaError
from kafka import KafkaProducer
from typing import Dict
import json

address_book = addressbook_pb2.AddressBook()

person = address_book.people.add()

person.id = int(1)
person.name = "ABC"
person.email = "asda@asdas.dasd"

phone = person.phones.add()
phone.number = "123123"
phone.type = addressbook_pb2.Person.PhoneType.MOBILE

serPerson = address_book.SerializeToString()

print(serPerson)

# # produce json messages
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'])
producer.send('demo-topic', serPerson)

# # block until all async messages are sent
producer.flush()
