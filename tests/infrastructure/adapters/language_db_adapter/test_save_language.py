from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.db.entity import LanguageEntity
from articles.domain.model import Language
from sqlalchemy.orm import Session


def test_save_language(language_db_adapter: LanguageDbAdapter, db_session: Session) -> None:
    language = Language(id_=1, name='name', code='CODE')
    result = language_db_adapter.save_language(language)
    assert language == result
    assert db_session.query(LanguageEntity).filter_by(id=1).first()
