from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.api.dto import CategoryDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestGetCategoryById:

    def test_when_domain_error(self, category_api_service: CategoryApiService) -> None:
        with patch.object(
            category_api_service.category_service,
            "get_category_by_id",
        ) as mock_get_category_by_id:
            mock_get_category_by_id.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                category_api_service.get_category_by_id(999)

        assert DomainError().message == str(e.value)

    def test_when_found(self, category_api_service: CategoryApiService) -> None:
        category_id = 1

        with patch.object(
            category_api_service.category_service,
            "get_category_by_id",
        ) as mock_get_category_by_id:
            mock_get_category_by_id.return_value = MagicMock()
            result = category_api_service.get_category_by_id(category_id)

        mock_get_category_by_id.assert_called_once_with(category_id)
        assert isinstance(result, CategoryDTO)
