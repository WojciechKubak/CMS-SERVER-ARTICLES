from articles.infrastructure.db.entity import TagEntity
from articles.infrastructure.db.repository import TagRepository
from sqlalchemy.orm import Session


def test_find_by_name(db_session: Session, tag_repository: TagRepository) -> None:
    tag_name = 'name'
    tag = TagEntity(id=1, name=tag_name)
    db_session.add(tag)
    db_session.commit()

    result = tag_repository.find_by_name(tag_name)
    assert tag.name == result.name
