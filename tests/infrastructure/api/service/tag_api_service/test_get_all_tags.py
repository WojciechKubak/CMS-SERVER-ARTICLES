from articles.infrastructure.api.service import TagApiService
from articles.infrastructure.api.dto import TagDTO
from unittest.mock import MagicMock, patch


def test_get_all_tags(tag_api_service: TagApiService) -> None:
    with patch.object(
        tag_api_service.tag_service,
        "get_all_tags",
    ) as mock_get_all_tags:
        mock_get_all_tags.return_value = [MagicMock()]
        result = tag_api_service.get_all_tags()

    mock_get_all_tags.assert_called_once()
    assert all(isinstance(tag, TagDTO) for tag in result)
