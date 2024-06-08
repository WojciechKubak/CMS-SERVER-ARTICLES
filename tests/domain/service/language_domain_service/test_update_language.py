from articles.domain.service import LanguageService
from articles.domain.errors import LanguageNameExistsError, LanguageNotFoundError
from articles.infrastructure.persistance.entity import LanguageEntity
from tests.factory import LanguageEntityFactory, LanguageFactory
from unittest.mock import patch
import pytest


class TestUpdateLanguage:

    def test_when_not_found(self, language_domain_service: LanguageService) -> None:
        language = LanguageFactory()
        with pytest.raises(LanguageNotFoundError) as e:
            language_domain_service.update_language(language)
        assert LanguageNotFoundError().message == str(e.value)

    def test_when_name_exists(self, language_domain_service: LanguageService) -> None:
        language_dto_first, language_dto_second = LanguageEntityFactory.create_batch(2)
        language = LanguageFactory(
            id_=language_dto_first.id, name=language_dto_second.name
        )

        with pytest.raises(LanguageNameExistsError) as e:
            language_domain_service.update_language(language)

        assert LanguageNameExistsError().message == str(e.value)

    def test_when_updated(self, language_domain_service: LanguageService) -> None:
        language_dto = LanguageEntityFactory()
        new_name = f"new_{language_dto.name}"
        language = LanguageFactory(id_=language_dto.id, name=new_name)

        with patch.object(
            language_domain_service.language_event_publisher, "publish_event"
        ) as publish:
            result = language_domain_service.update_language(language)

        publish.assert_called_once()
        assert LanguageEntity.query.filter_by(id=result.id_).first().name == new_name
