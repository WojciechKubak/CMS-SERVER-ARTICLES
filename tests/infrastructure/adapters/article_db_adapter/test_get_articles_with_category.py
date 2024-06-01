from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from tests.factory import ArticleEntityFactory, CategoryEntityFactory


def test_get_articles_with_category(
        article_db_adapter: ArticleDbAdapter
) -> None:
    category = CategoryEntityFactory()
    articles = ArticleEntityFactory.create_batch(5, category=category)
    result = article_db_adapter.get_articles_with_category(category.id)
    assert len(articles) == len(result)
