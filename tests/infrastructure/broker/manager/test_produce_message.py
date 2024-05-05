from unittest.mock import MagicMock, patch
from articles.infrastructure.broker.manager import ConfluentKafkaManager


@patch('articles.infrastructure.broker.manager.Producer')
def test_produce_message(mock_producer) -> None:
    kafka_manager = ConfluentKafkaManager(bootstrap_servers='localhost:9092', group_id='test_group')
    topic_name = 'test_topic'
    message = {'key': 'value'}

    mock_producer_instance = MagicMock()
    mock_producer.return_value = mock_producer_instance

    kafka_manager.produce_message(topic_name, message)

    mock_producer.assert_called_once_with({'bootstrap.servers': 'localhost:9092'})
    mock_producer_instance.produce.assert_called_once_with(topic_name, '{"key": "value"}'.encode('utf-8'))
    mock_producer_instance.flush.assert_called_once()
