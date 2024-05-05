from articles.domain.service import LanguageDomainService
from articles.infrastructure.db.entity import LanguageEntity
from articles.domain.model import Language
from sqlalchemy.orm import Session
import pytest


class TestUpdateLanguage:

    def test_when_not_found(self, language_domain_service: LanguageDomainService) -> None:
        language = Language(id_=1, name='name', code='CODE')
        with pytest.raises(ValueError) as err:
            language_domain_service.update_language(language)
            assert 'Language does not exist' == str(err.value)

    def test_when_name_exists(self, language_domain_service: LanguageDomainService, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
        db_session.commit()
        language = Language(id_=2, name='name', code='CODE')
        with pytest.raises(ValueError) as err:
            language_domain_service.update_language(language)
            assert 'Language name already exists' == str(err.value)

    def test_when_updated(self, language_domain_service: LanguageDomainService, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
        db_session.commit()
        language = Language(id_=1, name='updated_name', code='NEW')
        result = language_domain_service.update_language(language)
        assert 'NEW' == db_session.query(LanguageEntity).filter_by(id=result.id_).first().code
