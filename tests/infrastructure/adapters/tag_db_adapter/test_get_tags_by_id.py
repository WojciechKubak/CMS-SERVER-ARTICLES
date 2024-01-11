from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.db.entity import TagEntity
from sqlalchemy.orm import Session


def test_get_tags_by_id(tag_db_adapter: TagDbAdapter, db_session: Session) -> None:
    tags_dto = [TagEntity(id=1, name='name'), TagEntity(id=2, name='name')]
    db_session.bulk_save_objects(tags_dto)
    db_session.commit()
    result = tag_db_adapter.get_tags_by_id([1])
    assert 1 == len(result)
