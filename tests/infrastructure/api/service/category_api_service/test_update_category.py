from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.api.dto import CategoryDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestUpdateCategory:

    def test_when_domain_error(
            self,
            category_api_service: CategoryApiService
    ) -> None:
        mock_dto = MagicMock()

        with patch.object(
            category_api_service.category_service,
            'update_category',
        ) as mock_update_category:
            mock_update_category.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                category_api_service.update_category(mock_dto)

        assert DomainError().message == str(e.value)

    def test_when_updated(
            self,
            category_api_service: CategoryApiService
    ) -> None:
        mock_dto = MagicMock()

        with patch.object(
            category_api_service.category_service,
            'update_category',
        ) as mock_update_category:
            mock_update_category.return_value = MagicMock()
            result = category_api_service.update_category(mock_dto)

        mock_update_category.assert_called_once_with(
            mock_dto.to_domain()
        )
        assert isinstance(result, CategoryDTO)
