from articles.domain.service import LanguageDomainService
from articles.infrastructure.db.entity import LanguageEntity
from sqlalchemy.orm import Session
import pytest


class TestDeleteLanguage:

    def test_when_not_found(self, language_domain_service: LanguageDomainService) -> None:
        with pytest.raises(ValueError) as err:
            language_domain_service.delete_language(9999)
        assert 'Language does not exist' == str(err.value)

    def test_when_deleted(self, language_domain_service: LanguageDomainService, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
        db_session.commit()
        result = language_domain_service.delete_language(1)
        assert not db_session.query(LanguageEntity).filter_by(id=result).first()
