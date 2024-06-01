from articles.infrastructure.persistance.entity import ArticleEntity
from articles.domain.service import ArticleService
from articles.domain.errors import ArticleNotFoundError
from tests.factory import ArticleEntityFactory
from unittest.mock import patch
import pytest


class TestDeleteArticle:

    def test_when_not_found(
            self,
            article_domain_service: ArticleService
    ) -> None:
        with pytest.raises(ArticleNotFoundError) as e:
            article_domain_service.delete_article(999)
        assert ArticleNotFoundError().message == str(e.value)

    def test_when_deleted(
            self,
            article_domain_service: ArticleService
    ) -> None:
        article = ArticleEntityFactory()

        with patch.object(
            article_domain_service.file_storage,
            'delete_content'
        ) as mock_delete_content:
            id_ = article_domain_service.delete_article(article.id)

        mock_delete_content.assert_called_once()
        assert not ArticleEntity.query.filter_by(id=id_).first()
