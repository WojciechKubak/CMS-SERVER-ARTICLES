from articles.infrastructure.adapters.adapters import LanguageMessageBroker
from articles.infrastructure.broker.dto import LanguageChangeEvent
from unittest.mock import MagicMock
from tests.factory import LanguageEventFactory
import pytest


@pytest.fixture(scope="session")
def mock_message_broker() -> LanguageMessageBroker:
    kafka_manager_mock = MagicMock()
    return LanguageMessageBroker(
        kafka_manager=kafka_manager_mock, language_changes_topic="languages_topic"
    )


def test_publish_language_event(mock_message_broker: LanguageMessageBroker) -> None:
    event = LanguageEventFactory()
    mock_message_broker.publish_event(event)
    mock_message_broker.kafka_manager.produce_message.assert_called_once_with(
        "languages_topic", LanguageChangeEvent.from_domain(event)
    )
