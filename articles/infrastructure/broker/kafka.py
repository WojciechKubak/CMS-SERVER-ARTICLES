from articles.infrastructure.broker.errors import ConsumerServiceError
from confluent_kafka import Producer, Consumer
from dataclasses import dataclass
from typing import Callable, Type
import json
import logging


@dataclass
class KafkaService:
    """
    Service for interacting with Kafka.

    This class provides methods to produce and consume messages.

    Attributes:
        bootstrap_servers (str): The bootstrap servers for Kafka.
        group_id (str): The group ID for Kafka.
    """

    bootstrap_servers: str
    group_id: str

    def produce_message(self, topic_name: str, dto_class: Type) -> None:
        """
        Produce a message to a Kafka topic.

        This method creates a producer, produces a message to the specified
        topic, and flushes the producer.

        Args:
            topic_name (str): The name of the topic.
            dto_class (Type): The class of the DTO to produce.
        """
        producer = Producer({"bootstrap.servers": self.bootstrap_servers})
        producer.produce(topic_name, json.dumps(dto_class.to_dict()).encode("utf-8"))
        producer.flush()

    def consume_messages(
        self, topic_name: str, handler: Callable[[Type], None], dto_class: Type
    ) -> None:
        """
        Consume messages from a Kafka topic.

        This method creates a consumer, subscribes to the specified topic
        and consumes messages from it.
        If a message is successfully consumed, it is passed to the handler.
        If an error occurs while consuming a message, it is logged and the
        consumer continues to the next message.

        Args:
            topic_name (str): The name of the topic.
            handler (Callable[[Type], None]): The handler for the messages.
            dto_class (Type): The class of the DTO to consume.
        """
        consumer = Consumer(
            {
                "bootstrap.servers": self.bootstrap_servers,
                "group.id": self.group_id,
                "auto.offset.reset": "earliest",
            }
        )
        consumer.subscribe([topic_name])

        logging.info(f"Consuming messages from topic: {topic_name}")

        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                logging.info(f"Consumer error: {msg.error()}")
                continue

            try:
                data = json.loads(msg.value().decode("utf-8"))

                try:
                    handler(dto_class.from_json(data))
                    logging.info("Successfully handled")
                except ConsumerServiceError as e:
                    logging.error(f"Error occured: {e}")
                    continue

            except json.JSONDecodeError as e:
                logging.error(f"Error decoding message: {e}")
                continue

        consumer.close()
