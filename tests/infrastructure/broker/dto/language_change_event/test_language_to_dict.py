from articles.infrastructure.broker.dto import LanguageChangeEvent
from articles.domain.event import LanguageEventType


def test_to_dict() -> None:
    data = {
        'id_': 1,
        'name': 'name',
        'code': 'code',
        'event_type': LanguageEventType.CREATE,
    }
    dto = LanguageChangeEvent(**data)

    result = dto.to_dict()

    assert dto.id_ == result['id']
    assert dto.name == result['name']
    assert dto.code == result['code']
    assert dto.event_type.value == result['event_type']
