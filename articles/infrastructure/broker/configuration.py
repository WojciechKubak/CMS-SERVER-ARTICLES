from articles.infrastructure.broker.manager import ConfluentKafkaManager
from articles.env_config import BROKER_URI, GROUP_ID


kafka_manager = ConfluentKafkaManager(BROKER_URI, GROUP_ID)
