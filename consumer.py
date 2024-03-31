import json
from kafka import KafkaConsumer

env = {
    "kafka_server": ['localhost:9092'],
    "topic": "testingTopic",
}

consumer = KafkaConsumer(
    bootstrap_servers=env.get('kafka_server'),
    value_deserializer=json.loads,
    auto_offset_reset="latest",
    api_version=(0, 10, 1),
)

consumer.subscribe(env.get("topic"))

print("subscribing topic: {}".format(env.get('topic')))
while True:
    for data in consumer:
        print(data.value)
