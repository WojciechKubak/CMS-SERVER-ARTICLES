from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.persistance.entity import ArticleEntity
from tests.factory import ArticleFactory


def test_save_article(article_db_adapter: ArticleDbAdapter) -> None:
    article = ArticleFactory()
    result = article_db_adapter.save_article(article)
    assert ArticleEntity.query.filter_by(id=result.id_).first()
