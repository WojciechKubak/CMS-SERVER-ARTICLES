from confluent_kafka import Producer, Consumer
from dataclasses import dataclass
from typing import Callable, Type
import json
import logging


@dataclass
class ConfluentKafkaManager:
    bootstrap_servers: str
    group_id: str

    def produce_message(self, topic_name: str, dto_class: Type) -> None:
        producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        producer.produce(topic_name, json.dumps(dto_class.to_dict()).encode('utf-8'))
        producer.flush()

    def consume_messages(self, topic_name: str, handler: Callable[[Type], None], dto_class: Type) -> None:
        consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'
        })
        consumer.subscribe([topic_name])

        logging.info(f"Consuming messages from topic: {topic_name}")

        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                logging.info(f"Consumer error: {msg.error()}")
                continue
            
            data = json.loads(msg.value().decode('utf-8'))
            logging.info(f"Received message: {data}")
            
            try:
                handler(dto_class.from_json(data))
                logging.info("Successfully handled")
            except Exception as e:
                logging.error(f"Error occured: {e}")
                continue

        consumer.close()
