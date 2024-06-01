from articles.infrastructure.api.service import LanguageApiService
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestDeleteLanguage:

    def test_when_domain_error(
            self,
            language_api_service: LanguageApiService
    ) -> None:
        with patch.object(
            language_api_service.language_service,
            'delete_language',
        ) as mock_delete_language:
            mock_delete_language.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                language_api_service.delete_language(999)

        assert DomainError().message == str(e.value)

    def test_when_deleted(
            self,
            language_api_service: LanguageApiService
    ) -> None:
        language_id = 1

        with patch.object(
            language_api_service.language_service,
            'delete_language',
        ) as mock_delete_language:
            mock_delete_language.return_value = MagicMock()
            language_api_service.delete_language(language_id)

        mock_delete_language.assert_called_once_with(language_id)
