from articles.infrastructure.broker.dto import TranslationRequestDTO
from articles.domain.event import TranslationRequestEvent
from datetime import datetime


def test_from_domain() -> None:
    data = {
        'article_id': 1,
        'title': 'title',
        'content_path': 'path',
        'language_id': 1,
        'date': datetime.now()
    }
    event = TranslationRequestEvent(**data)

    result = TranslationRequestDTO.from_domain(event)

    assert event.article_id == result.article_id
    assert event.title == result.title
    assert event.content_path == result.content_path
    assert event.language_id == result.language_id
    assert event.date == result.date
