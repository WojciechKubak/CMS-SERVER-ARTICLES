from articles.infrastructure.api.service import CategoryApiService
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestDeleteCategory:

    def test_when_domain_error(
            self,
            category_api_service: CategoryApiService
    ) -> None:
        with patch.object(
            category_api_service.category_service,
            'delete_category',
        ) as mock_delete_category:
            mock_delete_category.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                category_api_service.delete_category(999)

        assert DomainError().message == str(e.value)

    def test_when_deleted(
            self,
            category_api_service: CategoryApiService
    ) -> None:
        id_to_delete = 1

        with patch.object(
            category_api_service.category_service,
            'delete_category',
        ) as mock_delete_category:
            mock_delete_category.return_value = MagicMock()
            category_api_service.delete_category(id_to_delete)

        mock_delete_category.assert_called_once_with(id_to_delete)
