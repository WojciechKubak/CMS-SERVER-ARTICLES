from articles.domain.event import TranslationRequestEvent
from tests.factory import ArticleFactory, LanguageFactory


def test_from_domain() -> None:
    article = ArticleFactory()
    language = LanguageFactory()

    result = TranslationRequestEvent.create(article, language)

    assert article.id_ == result.article_id
    assert article.title == result.title
    assert article.content == result.content_path
    assert language.id_ == result.language_id
