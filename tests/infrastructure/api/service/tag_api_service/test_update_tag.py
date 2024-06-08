from articles.infrastructure.api.service import TagApiService
from articles.infrastructure.api.dto import TagDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestUpdateTag:

    def test_when_domain_error(self, tag_api_service: TagApiService) -> None:
        with patch.object(
            tag_api_service.tag_service,
            "update_tag",
        ) as mock_update_tag:
            mock_update_tag.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                tag_api_service.update_tag(MagicMock())

        assert DomainError().message == str(e.value)

    def test_when_updated(self, tag_api_service: TagApiService) -> None:
        mock_dto = MagicMock()

        with patch.object(
            tag_api_service.tag_service,
            "update_tag",
        ) as mock_update_tag:
            mock_update_tag.return_value = MagicMock()
            result = tag_api_service.update_tag(mock_dto)

        mock_update_tag.assert_called_once_with(mock_dto.to_domain())
        assert isinstance(result, TagDTO)
