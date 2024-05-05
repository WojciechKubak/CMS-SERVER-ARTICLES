from articles.infrastructure.db.entity import LanguageEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestIdResourceDelete:
    resource_path = '/articles/languages'

    def test_when_not_found(self, client: Client) -> None:
        response = client.delete(f'{self.resource_path}/1111')
        assert 400 == response.status_code
        assert b'Language does not exist' in response.data

    def test_when_deleted(self, client: Client, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='code'))
        db_session.commit()
        response = client.delete(f"{self.resource_path}/1")
        assert 200 == response.status_code
        assert b'Deleted language with id' in response.data
