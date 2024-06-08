from articles.infrastructure.api.service import TagApiService
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestDeleteTag:

    def test_when_domain_error(self, tag_api_service: TagApiService) -> None:
        mock_dto = MagicMock()

        with patch.object(
            tag_api_service.tag_service,
            "delete_tag",
        ) as mock_delete_tag:
            mock_delete_tag.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                tag_api_service.delete_tag(mock_dto)
        assert DomainError().message == str(e.value)

    def test_when_deleted(self, tag_api_service: TagApiService) -> None:
        tag_id = 1

        with patch.object(
            tag_api_service.tag_service,
            "delete_tag",
        ) as mock_delete_tag:
            mock_delete_tag.return_value = MagicMock()
            tag_api_service.delete_tag(tag_id)

        mock_delete_tag.assert_called_once_with(tag_id)
