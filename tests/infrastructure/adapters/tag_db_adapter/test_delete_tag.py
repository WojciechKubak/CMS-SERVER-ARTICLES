from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.db.entity import TagEntity
from sqlalchemy.orm import Session


def test_delete_tag(db_session: Session, tag_db_adapter: TagDbAdapter) -> None:
    db_session.add(TagEntity(id=1, name='name'))
    db_session.commit()
    tag_db_adapter.delete_tag(1)
    assert not db_session.query(TagEntity).filter_by(id=1).first()
