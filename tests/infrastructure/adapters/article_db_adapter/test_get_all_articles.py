from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from tests.factory import ArticleEntityFactory


def test_get_all_articles(article_db_adapter: ArticleDbAdapter) -> None:
    articles = ArticleEntityFactory.create_batch(5)
    result = article_db_adapter.get_all_articles()
    assert len(articles) == len(result)
