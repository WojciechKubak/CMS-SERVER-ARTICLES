from articles.domain.model import Category, Tag
from tests.factory import ArticleEntityFactory


def test_to_domain() -> None:
    article = ArticleEntityFactory()
    result = article.to_domain()
    assert article.id == result.id_
    assert article.title == result.title
    assert article.content_path == result.content
    assert isinstance(result.category, Category)
    assert len(result.tags) == len(article.tags)
    assert all(isinstance(tag, Tag) for tag in result.tags)
