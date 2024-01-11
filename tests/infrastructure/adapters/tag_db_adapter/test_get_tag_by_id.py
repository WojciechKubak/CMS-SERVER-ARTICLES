from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.db.entity import TagEntity
from sqlalchemy.orm import Session


class TestGetTagById:

    def test_when_not_found(self, tag_db_adapter: TagDbAdapter, db_session: Session) -> None:
        result = tag_db_adapter.get_tag_by_id(1111)
        assert not result
        assert not db_session.query(TagEntity).filter_by(id=1111).first()

    def test_when_found(self, tag_db_adapter: TagDbAdapter, db_session: Session) -> None:
        db_session.add(TagEntity(id=1, name='name'))
        db_session.commit()
        result = tag_db_adapter.get_tag_by_id(1)
        assert 1 == result.id_
