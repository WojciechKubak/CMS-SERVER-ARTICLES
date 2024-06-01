from articles.infrastructure.api.service import TagApiService
from articles.infrastructure.api.dto import TagDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestGetTagById:

    def test_when_domain_error(self, tag_api_service: TagApiService) -> None:
        with patch.object(
            tag_api_service.tag_service,
            'get_tag_by_id',
        ) as mock_get_tag_by_id:
            mock_get_tag_by_id.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                tag_api_service.get_tag_by_id(999)

        assert DomainError().message == str(e.value)

    def test_when_found(self, tag_api_service: TagApiService) -> None:
        tag_id = 1

        with patch.object(
            tag_api_service.tag_service,
            'get_tag_by_id',
        ) as mock_get_tag_by_id:
            mock_get_tag_by_id.return_value = MagicMock()
            result = tag_api_service.get_tag_by_id(tag_id)

        mock_get_tag_by_id.assert_called_once_with(tag_id)
        assert isinstance(result, TagDTO)
