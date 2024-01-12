from articles.infrastructure.db.entity import TagEntity
from flask.testing import Client
from sqlalchemy.orm import Session


def test_tag_list_resource_get(client: Client, db_session: Session) -> None:
    tags_dto = [TagEntity(name=''), TagEntity(name='')]
    db_session.bulk_save_objects(tags_dto)
    db_session.commit()
    response = client.get('articles/tags')
    assert 200 == response.status_code
    assert len(tags_dto) == len(response.json)
