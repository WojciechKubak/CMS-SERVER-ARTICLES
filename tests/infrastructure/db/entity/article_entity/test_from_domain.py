from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity, TagEntity
from articles.domain.model import Article, Category, Tag


def test_from_domain() -> None:
    article = Article(
        id_=1,
        title='title',
        content='dummy',
        category=Category(id_=1, name='name', description='dummy'),
        tags=[Tag(id_=1, name=''), Tag(id_=12, name='')]
    )

    result = ArticleEntity.from_domain(article)

    assert article.id_ == result.id
    assert isinstance(result.category, CategoryEntity)
    assert all([isinstance(tag, TagEntity) for tag in result.tags])
