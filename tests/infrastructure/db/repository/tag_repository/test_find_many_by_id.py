from articles.infrastructure.db.repository import TagRepository
from articles.infrastructure.db.entity import TagEntity
from sqlalchemy.orm import Session
from typing import Any


def test_find_many_by_id(tag_repository: TagRepository, db_session: Session) -> None:
    tags = [TagEntity(name=''), TagEntity(name='')]
    db_session.bulk_save_objects(tags)
    db_session.commit()

    result = tag_repository.find_many_by_id([1, 2])
    assert len(tags) == len(result)
