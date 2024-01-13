from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity, TagEntity
from articles.domain.model import Category, Tag


def test_to_domain() -> None:
    article_dao = ArticleEntity(
        id=1,
        title='title',
        content_path='dummy',
        category=CategoryEntity(id=1, name='name', description='dummy'),
        tags=[TagEntity(id=1, name='name'), TagEntity(id=2, name='name')]
    )
    result = article_dao.to_domain()

    assert article_dao.id == result.id_
    assert isinstance(result.category, Category)
    assert all(isinstance(tag, Tag) for tag in result.tags)
