from articles.infrastructure.api.service import ArticleApiService
from articles.infrastructure.api.dto import ArticleDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestGetArticleById:

    def test_when_domain_error(
            self,
            article_api_service: ArticleApiService
    ) -> None:
        with patch.object(
            article_api_service.article_service,
            'get_article_by_id',
        ) as mock_get_article_by_id:
            mock_get_article_by_id.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                article_api_service.get_article_by_id(999)

        assert DomainError().message == str(e.value)

    def test_when_found(
            self,
            article_api_service: ArticleApiService
    ) -> None:
        article_id = 1

        with patch.object(
            article_api_service.article_service,
            'get_article_by_id',
        ) as mock_get_article_by_id:
            mock_get_article_by_id.return_value = MagicMock()
            result = article_api_service.get_article_by_id(article_id)

        mock_get_article_by_id.assert_called_once_with(article_id)
        assert isinstance(result, ArticleDTO)
