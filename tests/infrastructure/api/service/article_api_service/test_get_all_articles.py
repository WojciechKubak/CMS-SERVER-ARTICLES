from articles.infrastructure.api.service import ArticleApiService
from articles.infrastructure.api.dto import ArticleListDTO
from unittest.mock import MagicMock, patch


def test_get_all_articles(article_api_service: ArticleApiService) -> None:
    with patch.object(
        article_api_service.article_service,
        "get_all_articles",
    ) as mock_get_all_articles:
        mock_get_all_articles.return_value = [MagicMock(), MagicMock()]
        result = article_api_service.get_all_articles()

    mock_get_all_articles.assert_called_once()
    assert isinstance(result, list)
    assert isinstance(result[0], ArticleListDTO)
