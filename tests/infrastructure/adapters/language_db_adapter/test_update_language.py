from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.db.entity import LanguageEntity
from articles.domain.model import Language
from sqlalchemy.orm import Session


def test_update_language(language_db_adapter: LanguageDbAdapter, db_session: Session) -> None:
    db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
    db_session.commit()
    language = Language(id_=1, name='new_name', code='CODE')
    result = language_db_adapter.update_language(language)
    assert language == result
