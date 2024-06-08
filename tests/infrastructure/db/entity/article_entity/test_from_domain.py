from articles.infrastructure.persistance.entity import (
    ArticleEntity,
    CategoryEntity,
    TagEntity,
)
from tests.factory import ArticleFactory


def test_from_domain() -> None:
    article = ArticleFactory()
    result = ArticleEntity.from_domain(article)
    assert article.id_ == result.id
    assert article.title == result.title
    assert article.content == result.content_path
    assert isinstance(result.category, CategoryEntity)
    assert len(result.tags) == len(article.tags)
    assert all(isinstance(tag, TagEntity) for tag in result.tags)
