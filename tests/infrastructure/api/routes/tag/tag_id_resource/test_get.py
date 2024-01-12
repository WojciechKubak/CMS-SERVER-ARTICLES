from articles.infrastructure.db.entity import TagEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestIdResourceGet:
    resource_path = '/articles/tags'

    def test_when_not_found(self, client: Client) -> None:
        response = client.get(f'{self.resource_path}/1111')
        assert 400 == response.status_code
        assert b'Tag does not exist' in response.data

    def test_when_found(self, client: Client, db_session: Session) -> None:
        db_session.add(TagEntity(id=1, name='name'))
        db_session.commit()
        response = client.get(f'{self.resource_path}/1')
        assert 200 == response.status_code
        assert 1 == response.json['id']
