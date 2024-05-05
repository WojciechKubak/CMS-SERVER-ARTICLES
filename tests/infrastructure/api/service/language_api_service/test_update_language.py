from articles.infrastructure.api.service import LanguageApiService
from articles.infrastructure.db.entity import LanguageEntity
from articles.infrastructure.api.dto import LanguageDTO
from sqlalchemy.orm import Session
import pytest


class TestUpdateLanguage:

    def test_when_not_found(self, language_api_service: LanguageApiService) -> None:
        language_dto = LanguageDTO(
            id_=1,
            name='name',
            code='CODE'
        )
        with pytest.raises(ValueError) as err:
            language_api_service.update_language(language_dto)
            assert 'Language does not exist' == str(err.value)

    def test_when_name_exists(self, language_api_service: LanguageApiService, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
        db_session.commit()
        language_dto = LanguageDTO(
            id_=2,
            name='name',
            code='CODE'
        )
        with pytest.raises(ValueError) as err:
            language_api_service.update_language(language_dto)
            assert 'Language name already exists' == str(err.value)

    def test_when_updated(self, language_api_service: LanguageApiService, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code=''))
        db_session.commit()
        language_dto = LanguageDTO(
            id_=1,
            name='name',
            code='CODE'
        )
        result = language_api_service.update_language(language_dto)
        assert language_dto.code == db_session.query(LanguageEntity).filter_by(id=result.id_).first().code
