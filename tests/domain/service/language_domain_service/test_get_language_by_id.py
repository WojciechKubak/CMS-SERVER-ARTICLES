from articles.domain.service import LanguageService
from articles.domain.errors import LanguageNotFoundError
from articles.infrastructure.persistance.entity import LanguageEntity
from tests.factory import LanguageEntityFactory
import pytest


class TestGetLanguageById:

    def test_when_not_found(
            self,
            language_domain_service: LanguageService
    ) -> None:
        with pytest.raises(LanguageNotFoundError) as e:
            language_domain_service.get_language_by_id(999)
        assert LanguageNotFoundError().message == str(e.value)

    def test_when_found(
            self,
            language_domain_service: LanguageService
    ) -> None:
        language_dao = LanguageEntityFactory()
        result = language_domain_service.get_language_by_id(language_dao.id)
        assert LanguageEntity.query.filter_by(id=result.id_).first()
