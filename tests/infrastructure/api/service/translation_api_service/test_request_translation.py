from articles.infrastructure.api.service import TranslationApiService
from articles.infrastructure.api.dto import TranslationDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestRequestTranslation:

    def test_when_domain_error(
            self,
            translation_api_service: TranslationApiService
    ) -> None:
        with patch.object(
            translation_api_service.translation_service,
            'request_translation',
        ) as mock_request_translation:
            mock_request_translation.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                translation_api_service.request_translation(
                    MagicMock(), MagicMock())

        assert DomainError().message == str(e.value)

    def test_when_requested(
            self,
            translation_api_service: TranslationApiService
    ) -> None:
        mock_article = MagicMock()
        mock_language = MagicMock()

        with patch.object(
            translation_api_service.translation_service,
            'request_translation',
        ) as mock_request_translation:
            mock_request_translation.return_value = MagicMock()
            result = translation_api_service.request_translation(
                mock_article, mock_language
            )

        mock_request_translation.assert_called_once_with(
            mock_article, mock_language
        )
        assert isinstance(result, TranslationDTO)
