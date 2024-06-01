from articles.infrastructure.adapters.adapters import ArticleMessageBroker
from articles.infrastructure.broker.dto import TranslationRequestDTO
from tests.factory import TranslationRequestEventFactory
from unittest.mock import Mock
import pytest


@pytest.fixture(scope='session')
def mock_kafka_manager() -> ArticleMessageBroker:
    kafka_manager_mock = Mock()
    return ArticleMessageBroker(
        kafka_manager=kafka_manager_mock,
        translation_requests_topic='requests_topic',
    )


def test_publish_translation_request(
        mock_kafka_manager: ArticleMessageBroker
) -> None:
    event = TranslationRequestEventFactory()

    mock_kafka_manager.publish_event(event)

    mock_kafka_manager.kafka_manager.produce_message.assert_called_once_with(
        'requests_topic',
        TranslationRequestDTO.from_domain(event)
    )
