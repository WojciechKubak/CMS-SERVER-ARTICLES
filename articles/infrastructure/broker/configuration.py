from articles.infrastructure.broker.kafka import KafkaService
from articles.env_config import BROKER_URI, GROUP_ID


kafka_manager = KafkaService(BROKER_URI, GROUP_ID)
