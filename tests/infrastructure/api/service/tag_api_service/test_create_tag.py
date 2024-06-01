from articles.infrastructure.api.service import TagApiService
from articles.infrastructure.api.dto import TagDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestCreateTag:

    def test_when_domain_error(self, tag_api_service: TagApiService) -> None:
        mock_dto = MagicMock()

        with patch.object(
            tag_api_service.tag_service,
            'create_tag',
        ) as mock_create_tag:
            mock_create_tag.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                tag_api_service.create_tag(mock_dto)

        assert DomainError().message == str(e.value)

    def test_when_created(self, tag_api_service: TagApiService) -> None:
        mock_dto = MagicMock()

        with patch.object(
            tag_api_service.tag_service,
            'create_tag',
        ) as mock_create_tag:
            mock_create_tag.return_value = MagicMock()
            result = tag_api_service.create_tag(mock_dto)

        mock_create_tag.assert_called_once_with(
            mock_dto.to_domain()
        )
        assert isinstance(result, TagDTO)
