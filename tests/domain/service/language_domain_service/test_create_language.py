from articles.domain.service import LanguageService
from articles.domain.errors import LanguageNameExistsError
from articles.infrastructure.persistance.entity import LanguageEntity
from tests.factory import LanguageEntityFactory, LanguageFactory
from unittest.mock import patch
import pytest


class TestCreateLanguage:

    def test_when_name_exists(
            self,
            language_domain_service: LanguageService
    ) -> None:
        language_dto = LanguageEntityFactory()
        language = LanguageFactory(name=language_dto.name)

        with pytest.raises(LanguageNameExistsError) as e:
            language_domain_service.create_language(language)

        assert LanguageNameExistsError().message == str(e.value)

    def test_when_created(
            self,
            language_domain_service: LanguageService
    ) -> None:
        language = LanguageFactory()

        with patch.object(
            language_domain_service.language_event_publisher,
            'publish_event'
        ) as publish:
            result = language_domain_service.create_language(language)

        publish.assert_called_once()
        assert LanguageEntity.query.filter_by(id=result.id_).first()
