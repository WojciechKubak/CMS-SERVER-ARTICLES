from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.persistance.entity import ArticleEntity
from tests.factory import ArticleEntityFactory


class TestGetArticleById:

    def test_when_not_found(
            self,
            article_db_adapter: ArticleDbAdapter
    ) -> None:
        result = article_db_adapter.get_article_by_id(999)
        assert not result

    def test_when_found(self, article_db_adapter: ArticleDbAdapter) -> None:
        article = ArticleEntityFactory()
        result = article_db_adapter.get_article_by_id(article.id)
        assert ArticleEntity.query.filter_by(id=result.id_).first()
