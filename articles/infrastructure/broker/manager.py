from articles.infrastructure.broker.dto import TranslatedArticleDTO
from confluent_kafka import Producer, Consumer
from dataclasses import dataclass
from typing import Any, Callable
import datetime
import json
import logging


class DateTimeEncoder(json.JSONEncoder):
    
    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)


@dataclass
class ConfluentKafkaManager:
    bootstrap_servers: str
    group_id: str

    def produce_message(self, topic_name: str, message: dict[str, Any]) -> None:
        producer = Producer({'bootstrap.servers': self.bootstrap_servers})
        producer.produce(topic_name, json.dumps(message, cls=DateTimeEncoder).encode('utf-8'))
        producer.flush()

    def consume_messages(self, topic_name: str, handler: Callable) -> None:
        consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'
        })
        consumer.subscribe([topic_name])

        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                logging.info(f"Consumer error: {msg.error()}")
                continue
            
            logging.info(f"Received message: {msg.value().decode('utf-8')}")
            handler(TranslatedArticleDTO.from_dto(json.loads(msg.value().decode('utf-8'))))

        consumer.close()
