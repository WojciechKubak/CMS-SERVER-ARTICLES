from articles.infrastructure.db.entity import TagEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestCreateTag:
    resource_path = '/articles/tags'

    def test_when_name_exists(self, client: Client, db_session: Session) -> None:
        db_session.add(TagEntity(name='name'))
        db_session.commit()
        response = client.post(self.resource_path, json={'name': 'name'})
        assert 400 == response.status_code
        assert b'Tag name already exists' in response.data

    def test_when_created(self, client: Client, db_session: Session) -> None:
        response = client.post(self.resource_path, json={'name': 'name'})
        assert 201 == response.status_code
        assert db_session.query(TagEntity).filter_by(id=response.json['id']).first()
