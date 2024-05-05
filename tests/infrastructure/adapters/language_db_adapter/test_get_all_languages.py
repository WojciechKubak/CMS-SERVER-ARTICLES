from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.db.entity import LanguageEntity
from sqlalchemy.orm import Session


def test_get_all_languages(language_db_adapter: LanguageDbAdapter, db_session: Session) -> None:
    language_entities = [
        LanguageEntity(id=1, name='name', code='CODE'),
        LanguageEntity(id=2, name='name', code='CODE'),
    ]
    db_session.bulk_save_objects(language_entities)
    db_session.commit()
    result = language_db_adapter.get_all_languages()
    assert len(language_entities) == len(result)
