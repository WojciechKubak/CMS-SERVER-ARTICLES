from articles.infrastructure.db.entity import CategoryEntity
from flask.testing import Client
from sqlalchemy.orm import Session


def test_category_list_resource_get(client: Client, db_session: Session) -> None:
    categorys_dto = [CategoryEntity(name=''), CategoryEntity(name='')]
    db_session.bulk_save_objects(categorys_dto)
    db_session.commit()
    response = client.get('articles/categories')
    assert 200 == response.status_code
    assert len(categorys_dto) == len(response.json)
