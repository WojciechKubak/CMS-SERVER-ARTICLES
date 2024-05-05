from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.db.entity import LanguageEntity
from sqlalchemy.orm import Session


def test_delete_language(db_session: Session, language_db_adapter: LanguageDbAdapter) -> None:
    db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
    db_session.commit()
    language_db_adapter.delete_language(1)
    assert not db_session.query(LanguageEntity).filter_by(id=1).first()
