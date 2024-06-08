from articles.infrastructure.broker.dto import LanguageChangeEvent
from articles.domain.event import LanguageEvent, LanguageEventType


def test_from_domain() -> None:
    data = {
        "id_": 1,
        "name": "name",
        "code": "code",
        "event_type": LanguageEventType.CREATE,
    }
    event = LanguageEvent(**data)

    result = LanguageChangeEvent.from_domain(event)

    assert event.id_ == result.id_
    assert event.name == result.name
    assert event.code == result.code
    assert event.event_type == result.event_type
