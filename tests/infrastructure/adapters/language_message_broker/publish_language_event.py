from articles.infrastructure.adapters.adapters import LanguageMessageBroker
from articles.domain.event import LanguageEvent, LanguageEventType
from articles.infrastructure.broker.dto import LanguageChangeEvent
from unittest.mock import Mock


def test_publish_language_event() -> None:
    kafka_manager_mock = Mock()
    adapter = LanguageMessageBroker(
        kafka_manager=kafka_manager_mock,
        language_changes_topic='languages_topic'
    )
    event = LanguageEvent(
        id_=1, name='name', code='code', event_type=LanguageEventType.CREATE
    )
    adapter.publish_language_event(event)

    kafka_manager_mock.produce_message.assert_called_once_with(
        'languages_topic', LanguageChangeEvent.from_domain(event))
