import json
from kafka import KafkaConsumer

env = {
    "topic": "duchuytesting",
    "kafka_server": ['localhost:9092'],
}

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    value_deserializer=json.loads,
    auto_offset_reset="latest",
    api_version=(0, 10, 1),
)

consumer.subscribe(['duchuytesting'])

while True:
    for data in consumer:
        print(data.value)
