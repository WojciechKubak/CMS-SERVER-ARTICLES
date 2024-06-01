from articles.infrastructure.api.service import LanguageApiService
from articles.infrastructure.api.dto import LanguageDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestCreateLanguage:

    def test_when_domain_error(
            self,
            language_api_service: LanguageApiService
    ) -> None:
        mock_dto = MagicMock()

        with patch.object(
            language_api_service.language_service,
            'create_language',
        ) as mock_create_language:
            mock_create_language.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                language_api_service.create_language(mock_dto)

        assert DomainError().message == str(e.value)

    def test_when_created(
            self,
            language_api_service: LanguageApiService
    ) -> None:
        mock_dto = MagicMock()

        with patch.object(
            language_api_service.language_service,
            'create_language',
        ) as mock_create_language:
            mock_create_language.return_value = MagicMock()
            result = language_api_service.create_language(mock_dto)

        mock_create_language.assert_called_once_with(
            mock_dto.to_domain()
        )
        assert isinstance(result, LanguageDTO)
