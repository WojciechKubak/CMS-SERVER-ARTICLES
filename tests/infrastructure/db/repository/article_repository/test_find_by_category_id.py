from articles.infrastructure.persistance.repository import ArticleRepository
from tests.factory import ArticleEntityFactory, CategoryEntityFactory


def test_find_many_by_id(article_repository: ArticleRepository) -> None:
    category = CategoryEntityFactory()
    articles = ArticleEntityFactory.create_batch(
        5,
        category_id=category.id,
        category=category
    )

    result = article_repository.find_by_category_id(category.id)

    assert articles == result
