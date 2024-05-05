from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.db.entity import LanguageEntity
from sqlalchemy.orm import Session


class TestGetLanguageById:

    def test_when_not_found(self, language_db_adapter: LanguageDbAdapter, db_session: Session) -> None:
        result = language_db_adapter.get_language_by_id(1111)
        assert not result
        assert not db_session.query(LanguageEntity).filter_by(id=1111).first()

    def test_when_found(self, language_db_adapter: LanguageDbAdapter, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
        db_session.commit()
        result = language_db_adapter.get_language_by_id(1)
        assert 1 == result.id_
