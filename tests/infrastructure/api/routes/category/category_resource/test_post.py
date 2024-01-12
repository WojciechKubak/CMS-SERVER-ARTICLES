from articles.infrastructure.db.entity import CategoryEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestCreateCategory:
    resource_path = '/articles/categories'

    def test_when_name_exists(self, client: Client, db_session: Session) -> None:
        db_session.add(CategoryEntity(name='name'))
        db_session.commit()
        response = client.post(self.resource_path, json={'name': 'name'})
        assert 400 == response.status_code
        assert b'Category name already exists' in response.data

    def test_when_created(self, client: Client, db_session: Session) -> None:
        response = client.post(self.resource_path, json={'name': 'name'})
        assert 201 == response.status_code
        assert db_session.query(CategoryEntity).filter_by(id=response.json['id']).first()
