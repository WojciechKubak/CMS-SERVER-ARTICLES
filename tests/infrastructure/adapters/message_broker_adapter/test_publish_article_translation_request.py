from articles.infrastructure.adapters.adapters import MessageBrokerAdapter
from articles.domain.event import ArticleTranslationEvent
from unittest.mock import Mock
from datetime import datetime


def test_publish_article_translation_request() -> None:
    kafka_manager_mock = Mock()
    adapter = MessageBrokerAdapter(
        kafka_manager=kafka_manager_mock,
        translation_requests_topic='requests_topic',
        translation_updates_topic='updates_topic'
    )
    event = ArticleTranslationEvent(
        article_id=1, content_path='path', language_id=1, date=datetime.now()
    )
    adapter.publish_article_translation_request(event)

    kafka_manager_mock.produce_message.assert_called_once_with(
        'requests_topic', event.to_json())
