from articles.infrastructure.db.entity import CategoryEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestIdResourceDelete:
    resource_path = '/articles/categories'

    def test_when_not_found(self, client: Client) -> None:
        response = client.delete(f'{self.resource_path}/1111')
        assert 400 == response.status_code
        assert b'Category does not exist' in response.data

    def test_when_deleted(self, client: Client, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name'))
        db_session.commit()
        response = client.delete(f"{self.resource_path}/1")
        assert 200 == response.status_code
        assert b'Deleted category with id' in response.data
