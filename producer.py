import time
import json
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

env = {
    "kafka_server": ['localhost:9092'],
    "topic": "testingTopic",
}


def create_dummy_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year(),
    }


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(
    bootstrap_servers=env.get('kafka_server'),
    value_serializer=json_serializer,
    api_version=(0, 10, 1),
)

while True:
    user = create_dummy_user()
    producer.send(env.get('topic'), user)
    print("sending {}".format(user))
    producer.flush()
    time.sleep(3)
