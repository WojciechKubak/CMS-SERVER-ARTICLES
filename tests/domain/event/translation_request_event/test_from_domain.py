from articles.domain.model import Article, Language
from articles.domain.event import TranslationRequestEvent
from datetime import datetime


def test_article_translation_event_from_domain() -> None:
    article = Article(
        id_=1, 
        title='title',
        content='content',
        category=1,
        tags=[1, 2]
    )
    language = Language(id_=1, name='language', code='LN')
    result = TranslationRequestEvent.from_domain(article, language)
    assert article.id_ == result.article_id
    assert language.id_ == result.language_id
    assert article.content == result.content_path
    assert isinstance(result.date, datetime)
