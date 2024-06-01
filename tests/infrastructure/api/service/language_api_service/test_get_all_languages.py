from articles.infrastructure.api.service import LanguageApiService
from articles.infrastructure.api.dto import LanguageDTO
from unittest.mock import MagicMock, patch


def test_get_all_languages(
        language_api_service: LanguageApiService
) -> None:
    with patch.object(
        language_api_service.language_service,
        'get_all_languages',
    ) as mock_get_all_languages:
        mock_get_all_languages.return_value = [
            MagicMock(), MagicMock()
        ]
        result = language_api_service.get_all_languages()

    mock_get_all_languages.assert_called_once()
    assert isinstance(result, list)
    assert isinstance(result[0], LanguageDTO)
