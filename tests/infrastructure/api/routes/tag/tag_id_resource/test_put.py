from articles.infrastructure.db.entity import TagEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestIdResourcePut:
    resource_path = '/articles/tags'

    def test_when_not_found(self, client: Client) -> None:
        tag_dto = {
            'name': 'updated_name',
            'description': 'dummy'
        }
        response = client.put(f'{self.resource_path}/1111', json=tag_dto)
        assert 400 == response.status_code
        assert b'Tag does not exist' in response.data

    def test_when_updated(self, client: Client, db_session: Session) -> None:
        db_session.add(TagEntity(id=1, name='name'))
        db_session.commit()
        tag_dto = {
            'name': 'updated_name',
            'description': 'dummy'
        }
        response = client.put(f'{self.resource_path}/1', json=tag_dto)
        assert 200 == response.status_code
        assert tag_dto['name'] == response.json['name']
