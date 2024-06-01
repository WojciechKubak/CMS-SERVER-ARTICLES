from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.persistance.entity import ArticleEntity
from tests.factory import ArticleEntityFactory


def test_delete_article(article_db_adapter: ArticleDbAdapter) -> None:
    article = ArticleEntityFactory()
    article_db_adapter.delete_article(article.id)
    assert not ArticleEntity.query.filter_by(id=article.id).first()
