from articles.infrastructure.api.service import TagApiService
from articles.infrastructure.db.entity import TagEntity
from sqlalchemy.orm import Session


def test_get_all_tags(tag_api_service: TagApiService, db_session: Session) -> None:
    tags_dto = [TagEntity(name=''), TagEntity(name='')]
    db_session.bulk_save_objects(tags_dto)
    db_session.commit()
    result = tag_api_service.get_all_tags()
    assert len(tags_dto) == len(result)
