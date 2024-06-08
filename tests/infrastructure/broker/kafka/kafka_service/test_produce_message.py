from articles.infrastructure.broker.kafka import KafkaService
from unittest.mock import patch, MagicMock


@patch("articles.infrastructure.broker.kafka.Producer")
def test_produce_message(mock_producer_class, kafka_service: KafkaService) -> None:
    mock_producer_instance = mock_producer_class.return_value
    mock_dto_class = MagicMock()
    mock_dto_class.to_dict.return_value = {"key": "value"}

    kafka_service.produce_message("test_topic", mock_dto_class)

    mock_producer_instance.produce.assert_called_once_with(
        "test_topic", '{"key": "value"}'.encode("utf-8")
    )
    mock_producer_instance.flush.assert_called_once()
