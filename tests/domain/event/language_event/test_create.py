from articles.domain.event import LanguageEvent, LanguageEventType
from tests.factory import LanguageFactory


def test_from_domain() -> None:
    language = LanguageFactory()
    event_type = LanguageEventType.CREATE

    result = LanguageEvent.create(language, event_type)

    assert language.id_ == result.id_
    assert language.name == result.name
    assert language.code == result.code
    assert event_type == result.event_type
