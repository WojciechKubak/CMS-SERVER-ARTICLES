from articles.infrastructure.api.service import ArticleApiService
from articles.infrastructure.api.dto import ArticleDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestCreateArticle:

    def test_when_domain_error(
            self,
            article_api_service: ArticleApiService
    ) -> None:
        mock_dto = MagicMock()

        with patch.object(
            article_api_service.article_service,
            'create_article',
        ) as mock_create_article:
            mock_create_article.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                article_api_service.create_article(mock_dto)

        assert DomainError().message == str(e.value)

    def test_when_created(
            self,
            article_api_service: ArticleApiService
    ) -> None:
        mock_dto = MagicMock()

        with patch.object(
            article_api_service.article_service,
            'create_article',
        ) as mock_create_article:
            mock_create_article.return_value = MagicMock()
            result = article_api_service.create_article(mock_dto)

        mock_create_article.assert_called_once_with(
            mock_dto.to_domain()
        )
        assert isinstance(result, ArticleDTO)
