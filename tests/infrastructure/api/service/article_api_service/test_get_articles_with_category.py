from articles.infrastructure.api.service import ArticleApiService
from articles.infrastructure.api.dto import ArticleListDTO
from unittest.mock import MagicMock, patch


def test_get_articles_with_category(
        article_api_service: ArticleApiService
) -> None:
    category_id = 1

    with patch.object(
        article_api_service.article_service,
        'get_articles_with_category',
    ) as mock_get_articles_with_category:
        mock_get_articles_with_category.return_value = [
            MagicMock(), MagicMock()
        ]
        result = article_api_service.get_articles_with_category(category_id)

    mock_get_articles_with_category.assert_called_once_with(category_id)
    assert isinstance(result, list)
    assert isinstance(result[0], ArticleListDTO)
