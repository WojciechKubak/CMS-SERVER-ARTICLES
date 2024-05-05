from articles.infrastructure.db.entity import LanguageEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestIdResourcePut:
    resource_path = '/articles/languages'

    def test_when_not_found(self, client: Client) -> None:
        language_dto = {
            'name': 'updated_name',
            'code': 'new_code'
        }
        response = client.put(f'{self.resource_path}/1111', json=language_dto)
        assert 400 == response.status_code
        assert b'Language does not exist' in response.data

    def test_when_updated(self, client: Client, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='code'))
        db_session.commit()
        language_dto = {
            'name': 'updated_name',
            'code': 'new'
        }
        response = client.put(f'{self.resource_path}/1', json=language_dto)
        assert 200 == response.status_code
        assert language_dto['code'] == response.json['code']
