from articles.infrastructure.broker.dto import TranslationRequestDTO
from datetime import datetime


def test_to_dict() -> None:
    data = {
        'article_id': 1,
        'title': 'title',
        'content_path': 'path',
        'language_id': 1,
        'date': datetime.now()
    }
    dto = TranslationRequestDTO(**data)

    result = dto.to_dict()

    assert dto.article_id == result['id']
    assert dto.title == result['title']
    assert dto.language_id == result['language_id']
    assert dto.date.strftime('%Y-%m-%d %H:%M:%S') == result['date']
