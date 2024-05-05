from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.db.entity import LanguageEntity
from sqlalchemy.orm import Session


def test_get_all_categories(language_db_adapter: LanguageDbAdapter, db_session: Session) -> None:
    languages_dto = [
        LanguageEntity(name='name1', code='CODE1'), 
        LanguageEntity(name='name2', code='CODE2')
    ]
    db_session.bulk_save_objects(languages_dto)
    db_session.commit()
    result = language_db_adapter.get_all_languages()
    assert len(languages_dto) == len(result)
