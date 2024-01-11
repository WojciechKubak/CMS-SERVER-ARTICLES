from articles.infrastructure.adapters.adapters import TagDbAdapter
from articles.infrastructure.db.entity import TagEntity
from sqlalchemy.orm import Session


def test_get_all_tags(tag_db_adapter: TagDbAdapter, db_session: Session) -> None:
    tags_dto = [TagEntity(name='name'), TagEntity(name='name')]
    db_session.bulk_save_objects(tags_dto)
    db_session.commit()
    result = tag_db_adapter.get_all_tags()
    assert len(tags_dto) == len(result)
