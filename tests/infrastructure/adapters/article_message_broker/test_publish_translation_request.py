from articles.infrastructure.adapters.adapters import ArticleMessageBroker
from articles.domain.event import TranslationRequestEvent
from articles.infrastructure.broker.dto import TranslationRequestDTO
from datetime import datetime
from unittest.mock import Mock


def test_publish_translation_request() -> None:
    kafka_manager_mock = Mock()
    adapter = ArticleMessageBroker(
        kafka_manager=kafka_manager_mock,
        translation_requests_topic='requests_topic',
        translation_updates_topic='updates_topic'
    )
    event = TranslationRequestEvent(
        article_id=1, title='title', content_path='path', language_id=1, date=datetime.now()
    )
    adapter.publish_translation_request(event)

    kafka_manager_mock.produce_message.assert_called_once_with(
        'requests_topic', TranslationRequestDTO.from_domain(event))
