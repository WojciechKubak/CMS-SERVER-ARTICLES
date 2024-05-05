from articles.infrastructure.api.service import LanguageApiService
from articles.infrastructure.db.entity import LanguageEntity
from sqlalchemy.orm import Session


def test_get_all_languages(language_api_service: LanguageApiService, db_session: Session) -> None:
    languages_dto = [
        LanguageEntity(name='language1', code='CODE'), 
        LanguageEntity(name='language2', code='CODE')
    ]
    db_session.bulk_save_objects(languages_dto)
    db_session.commit()
    result = language_api_service.get_all_languages()
    assert len(languages_dto) == len(result)
