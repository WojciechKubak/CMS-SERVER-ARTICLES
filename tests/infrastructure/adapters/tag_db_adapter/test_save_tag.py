from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.db.entity import TagEntity
from articles.domain.model import Tag
from sqlalchemy.orm import Session


def test_save_tag(tag_db_adapter: TagDbAdapter, db_session: Session) -> None:
    tag = Tag(id_=1, name='name')
    result = tag_db_adapter.save_tag(tag)
    assert tag == result
    assert db_session.query(TagEntity).filter_by(id=1).first()
