
# SIMPLE CDC WITH KAFKA AND ELK USING DOCKER-COMPOSE



## Getting Started

- First terminal tab:

```bash
  docker compose -f kafka-docker-compose.yml up -d
```


- Second terminal tab:

```bash
  docker compose -f elk-docker-compose.yml up -d
```

Now Kafka and ELK services are running, open another terminal tab then:

- Installed all the required packages:
```bash
  pip install -r requirements.txt 
```

- Run the consumer first:
```bash
  python consumer.py
```

- Now, run the producer:
```bash
  python producer.py
```


## Used By

This project is used by everyone that going to have the very first step in kafka, elk.

Enjoy yourself!!

