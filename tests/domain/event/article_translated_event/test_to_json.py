from articles.domain.event import ArticleTranslatedEvent
from datetime import datetime


def test_article_translated_event_to_json() -> None:
    translated_event_data = {
        'article_id': 1,
        'content_path': 'content',
        'language_id': 1,
        'date': datetime.now()
    }
    translated_event = ArticleTranslatedEvent(**translated_event_data)
    result = translated_event.to_json()
    assert translated_event_data == result
