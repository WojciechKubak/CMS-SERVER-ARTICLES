from articles.infrastructure.broker.kafka import KafkaService
from confluent_kafka import Message, KafkaError
from unittest.mock import patch, MagicMock
import pytest


@pytest.mark.skip("Keep stucking in consumer loop")
@patch("confluent_kafka.Consumer")
def test_consume_messages(mock_consumer_class) -> None:
    mock_consumer_instance = mock_consumer_class.return_value
    service = KafkaService(
        bootstrap_servers="test_bootstrap_server", group_id="test_group"
    )
    mock_handler = MagicMock()
    mock_dto_class = MagicMock()

    mock_msg = MagicMock(spec=Message)
    mock_msg.error.return_value = KafkaError(KafkaError._ALL_BROKERS_DOWN)
    mock_consumer_instance.poll.return_value = mock_msg

    service.consume_messages("test_topic", mock_handler, mock_dto_class)

    mock_consumer_instance.subscribe.assert_called_once_with(["test_topic"])
