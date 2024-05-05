from articles.infrastructure.api.service import LanguageApiService
from articles.infrastructure.db.entity import LanguageEntity
from articles.infrastructure.api.dto import LanguageDTO
from sqlalchemy.orm import Session
import pytest


class TestCreateLanguage:

    def test_when_name_exists(self, language_api_service: LanguageApiService, db_session: Session) -> None:
        db_session.add(LanguageEntity(name='name', code='CODE'))
        db_session.commit()
        language_dto = LanguageDTO(
            id_=None,
            name='name',
            code='CODE'
        )
        with pytest.raises(ValueError) as err:
            language_api_service.create_language(language_dto)
            assert 'Language name already exists' == str(err.value)

    def test_when_created(self, language_api_service: LanguageApiService, db_session: Session) -> None:
        language_dto = LanguageDTO(
            id_=None,
            name='name',
            code='CODE'
        )
        result = language_api_service.create_language(language_dto)
        assert db_session.query(LanguageEntity).filter_by(id=result.id_).first()
