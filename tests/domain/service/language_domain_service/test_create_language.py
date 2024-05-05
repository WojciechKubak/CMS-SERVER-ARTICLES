from articles.domain.service import LanguageDomainService
from articles.infrastructure.db.entity import LanguageEntity
from articles.domain.model import Language
from sqlalchemy.orm import Session
import pytest


class TestCreateLanguage:

    def test_when_name_exists(self, language_domain_service: LanguageDomainService, db_session: Session) -> None:
        db_session.add(LanguageEntity(name='name', code='CODE'))
        db_session.commit()
        language = Language(id_=None, name='name', code='CODE')
        with pytest.raises(ValueError) as err:
            language_domain_service.create_language(language)
            assert 'Language name already exists' == str(err.value)

    def test_when_created(self, language_domain_service: LanguageDomainService, db_session: Session) -> None:
        language = Language(id_=None, name='name', code='CODE')
        result = language_domain_service.create_language(language)
        assert db_session.query(LanguageEntity).filter_by(id=result.id_).first()
