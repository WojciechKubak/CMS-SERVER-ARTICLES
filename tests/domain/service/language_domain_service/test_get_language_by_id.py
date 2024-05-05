from articles.domain.service import LanguageDomainService
from articles.infrastructure.db.entity import LanguageEntity
from sqlalchemy.orm import Session
import pytest


class TestGetLanguageById:

    def test_when_not_found(self, language_domain_service: LanguageDomainService) -> None:
        with pytest.raises(ValueError) as err:
            language_domain_service.get_language_by_id(9999)
        assert 'Language does not exist' == str(err.value)

    def test_when_found(self, language_domain_service: LanguageDomainService, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
        db_session.commit()
        result = language_domain_service.get_language_by_id(1)
        assert db_session.query(LanguageEntity).filter_by(id=result.id_).first()
