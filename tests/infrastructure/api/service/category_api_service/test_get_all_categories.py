from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.api.dto import CategoryDTO
from unittest.mock import MagicMock, patch


def test_get_all_categories(category_api_service: CategoryApiService) -> None:
    with patch.object(
        category_api_service.category_service,
        "get_all_categories",
    ) as mock_get_all_categories:
        mock_get_all_categories.return_value = [MagicMock(), MagicMock()]
        result = category_api_service.get_all_categories()

    mock_get_all_categories.assert_called_once()
    assert isinstance(result, list)
    assert isinstance(result[0], CategoryDTO)
