from articles.infrastructure.broker.kafka import KafkaService
import pytest


@pytest.fixture(scope="session")
def kafka_service() -> KafkaService:
    return KafkaService(
        bootstrap_servers="test_bootstrap_server", group_id="test_group"
    )
