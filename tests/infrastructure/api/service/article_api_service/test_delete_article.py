from articles.infrastructure.api.service import ArticleApiService
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestDeleteArticle:

    def test_when_domain_error(
            self,
            article_api_service: ArticleApiService
    ) -> None:
        with patch.object(
            article_api_service.article_service,
            'delete_article',
        ) as mock_delete_article:
            mock_delete_article.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                article_api_service.delete_article(999)

        assert DomainError().message == str(e.value)

    def test_when_deleted(
            self,
            article_api_service: ArticleApiService
    ) -> None:
        id_to_delete = 1

        with patch.object(
            article_api_service.article_service,
            'delete_article',
        ) as mock_delete_article:
            mock_delete_article.return_value = MagicMock()
            article_api_service.delete_article(id_to_delete)

        mock_delete_article.assert_called_once_with(id_to_delete)
