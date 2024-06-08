from articles.domain.service import LanguageService
from articles.domain.errors import LanguageNotFoundError
from articles.infrastructure.persistance.entity import LanguageEntity
from tests.factory import LanguageEntityFactory
from unittest.mock import patch
import pytest


class TestDeleteLanguage:

    def test_when_not_found(self, language_domain_service: LanguageService) -> None:
        with pytest.raises(LanguageNotFoundError) as e:
            language_domain_service.delete_language(999)
        assert LanguageNotFoundError().message == str(e.value)

    def test_when_deleted(self, language_domain_service: LanguageService) -> None:
        language_dao = LanguageEntityFactory()

        with patch.object(
            language_domain_service.language_event_publisher, "publish_event"
        ) as publish:
            result = language_domain_service.delete_language(language_dao.id)

        publish.asser_called_once()
        assert not LanguageEntity.query.filter_by(id=result).first()
