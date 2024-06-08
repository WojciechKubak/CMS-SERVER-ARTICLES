from articles.infrastructure.api.service import TranslationApiService
from articles.infrastructure.api.dto import TranslationDTO
from articles.infrastructure.api.errors import ApplicationError
from articles.domain.errors import DomainError
from unittest.mock import MagicMock, patch
import pytest


class TestGetTranslationById:

    def test_when_domain_error(
        self, translation_api_service: TranslationApiService
    ) -> None:
        with patch.object(
            translation_api_service.translation_service,
            "get_translation_by_id",
        ) as mock_get_translation_by_id:
            mock_get_translation_by_id.side_effect = DomainError()
            with pytest.raises(ApplicationError) as e:
                translation_api_service.get_translation_by_id(MagicMock())

        assert DomainError().message == str(e.value)

    def test_when_found(self, translation_api_service: TranslationApiService) -> None:
        translation_id = 1

        with patch.object(
            translation_api_service.translation_service,
            "get_translation_by_id",
        ) as mock_get_translation_by_id:
            mock_get_translation_by_id.return_value = MagicMock()
            result = translation_api_service.get_translation_by_id(translation_id)

        mock_get_translation_by_id.assert_called_once_with(translation_id)
        assert isinstance(result, TranslationDTO)
