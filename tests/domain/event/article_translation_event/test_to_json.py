from articles.domain.event import ArticleTranslationEvent
from datetime import datetime


def test_article_translation_event_to_json() -> None:
    translation_event_data = {
        'article_id': 1,
        'content_path': 'content',
        'language_id': 1,
        'date': datetime.now()
    }
    translation_event = ArticleTranslationEvent(**translation_event_data)
    result = translation_event.to_json()
    assert translation_event_data == result
