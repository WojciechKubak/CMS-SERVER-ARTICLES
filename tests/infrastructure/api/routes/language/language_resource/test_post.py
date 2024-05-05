from articles.infrastructure.db.entity import LanguageEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestCreateLanguage:
    resource_path = '/articles/languages'

    def test_when_name_exists(self, client: Client, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='code'))
        db_session.commit()
        response = client.post(self.resource_path, json={'name': 'name', 'code': 'code'})
        assert 400 == response.status_code
        assert b'Language name already exists' in response.data

    def test_when_created(self, client: Client, db_session: Session) -> None:
        response = client.post(self.resource_path, json={'name': 'name', 'code': 'code'})
        assert 201 == response.status_code
        assert db_session.query(LanguageEntity).filter_by(id=response.json['id']).first()
