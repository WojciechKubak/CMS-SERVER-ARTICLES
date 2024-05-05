from unittest.mock import MagicMock, patch
from articles.infrastructure.broker.manager import ConfluentKafkaManager
import pytest


@pytest.mark.skip
@patch('articles.infrastructure.broker.manager.Consumer')
@patch('articles.infrastructure.broker.manager.TranslatedArticleDTO')
def test_consume_messages(mock_dto: MagicMock, mock_consumer: MagicMock) -> None:
    kafka_manager = ConfluentKafkaManager(bootstrap_servers='localhost:9092', group_id='test_group')
    topic_name = 'test_topic'
    handler = MagicMock()

    mock_consumer_instance = MagicMock()
    mock_consumer.return_value = mock_consumer_instance

    mock_msg = MagicMock()
    mock_msg.value.return_value = '{"key": "value"}'.encode('utf-8')
    mock_consumer_instance.poll.return_value = mock_msg

    kafka_manager.consume_messages(topic_name, handler)

    mock_consumer.assert_called_once_with({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'test_group',
        'auto.offset.reset': 'earliest'
    })
    mock_consumer_instance.subscribe.assert_called_once_with([topic_name])
    handler.assert_called_once_with(mock_dto.from_dto.return_value)
