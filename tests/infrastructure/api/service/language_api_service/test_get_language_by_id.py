from articles.infrastructure.api.service import LanguageApiService
from articles.infrastructure.api.dto import LanguageDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestGetLanguageById:

    def test_when_domain_error(
            self,
            language_api_service: LanguageApiService
    ) -> None:
        with patch.object(
            language_api_service.language_service,
            'get_language_by_id',
        ) as mock_get_language_by_id:
            mock_get_language_by_id.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                language_api_service.get_language_by_id(999)

        assert DomainError().message == str(e.value)

    def test_when_found(
            self,
            language_api_service: LanguageApiService
    ) -> None:
        language_id = 1

        with patch.object(
            language_api_service.language_service,
            'get_language_by_id',
        ) as mock_get_language_by_id:
            mock_get_language_by_id.return_value = MagicMock()
            result = language_api_service.get_language_by_id(language_id)

        mock_get_language_by_id.assert_called_once_with(language_id)
        assert isinstance(result, LanguageDTO)
