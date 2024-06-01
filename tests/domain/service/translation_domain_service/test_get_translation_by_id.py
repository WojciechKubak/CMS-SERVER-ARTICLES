from articles.domain.service import TranslationService
from articles.infrastructure.persistance.entity import TranslationEntity
from articles.domain.errors import TranslationNotFoundError
from tests.factory import TranslationEntityFactory
import pytest


class TestGetTranslationById:

    def test_when_not_found(
            self,
            translation_domain_service: TranslationService
    ) -> None:
        with pytest.raises(TranslationNotFoundError) as e:
            translation_domain_service.get_translation_by_id(999)
        assert TranslationNotFoundError().message == str(e.value)

    def test_when_found(
            self,
            translation_domain_service: TranslationService
    ) -> None:
        translation = TranslationEntityFactory()
        result = translation_domain_service.get_translation_by_id(
            translation.id
        )
        assert TranslationEntity.query.filter_by(id=result.id_).first()
