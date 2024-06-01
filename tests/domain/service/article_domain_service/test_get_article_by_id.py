from articles.domain.service import ArticleService
from articles.domain.errors import ArticleNotFoundError
from articles.infrastructure.persistance.entity import ArticleEntity
from tests.factory import ArticleEntityFactory
import pytest


class TestGetArticleById:

    def test_when_not_found(
            self,
            article_domain_service: ArticleService
    ) -> None:
        with pytest.raises(ArticleNotFoundError) as e:
            article_domain_service.get_article_by_id(999)
        assert ArticleNotFoundError().message == str(e.value)

    def test_when_found(self, article_domain_service: ArticleService) -> None:
        article = ArticleEntityFactory()
        result = article_domain_service.get_article_by_id(article.id)
        assert ArticleEntity.query.filter_by(id=result.id_).first()
        assert 'path_content' == result.content
