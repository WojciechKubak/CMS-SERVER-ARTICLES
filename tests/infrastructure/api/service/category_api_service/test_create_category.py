from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.api.dto import CategoryDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestCreateCategory:

    def test_when_domain_error(self, category_api_service: CategoryApiService) -> None:
        mock_dto = MagicMock()

        with patch.object(
            category_api_service.category_service,
            "create_category",
        ) as mock_create_category:
            mock_create_category.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                category_api_service.create_category(mock_dto)

        assert DomainError().message == str(e.value)

    def test_when_created(self, category_api_service: CategoryApiService) -> None:
        mock_dto = MagicMock()

        with patch.object(
            category_api_service.category_service,
            "create_category",
        ) as mock_create_category:
            mock_create_category.return_value = MagicMock()
            result = category_api_service.create_category(mock_dto)

        mock_create_category.assert_called_once_with(mock_dto.to_domain())
        assert isinstance(result, CategoryDTO)
