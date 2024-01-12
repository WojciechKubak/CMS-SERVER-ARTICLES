from articles.infrastructure.db.entity import CategoryEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestIdResourcePut:
    resource_path = '/articles/categories'

    def test_when_not_found(self, client: Client) -> None:
        category_dto = {
            'name': 'updated_name',
            'description': 'dummy'
        }
        response = client.put(f'{self.resource_path}/1111', json=category_dto)
        assert 400 == response.status_code
        assert b'Category does not exist' in response.data

    def test_when_updated(self, client: Client, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name'))
        db_session.commit()
        category_dto = {
            'name': 'updated_name',
            'description': 'dummy'
        }
        response = client.put(f'{self.resource_path}/1', json=category_dto)
        assert 200 == response.status_code
        assert category_dto['name'] == response.json['name']
