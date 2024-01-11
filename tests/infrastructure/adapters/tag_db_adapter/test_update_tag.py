from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.db.entity import TagEntity
from articles.domain.model import Tag
from sqlalchemy.orm import Session


def test_update_tag(tag_db_adapter: TagDbAdapter, db_session: Session) -> None:
    db_session.add(TagEntity(id=1, name=''))
    db_session.commit()

    tag = Tag(id_=1, name='name')
    result = tag_db_adapter.update_tag(tag)

    assert tag == result
    assert db_session.query(TagEntity).filter_by(id=1).first().name == 'name'
