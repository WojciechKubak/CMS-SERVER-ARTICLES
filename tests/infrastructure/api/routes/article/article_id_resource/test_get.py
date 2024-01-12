from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestIdResourceGet:
    resource_path = '/articles'

    def test_when_not_found(self, client: Client) -> None:
        response = client.get(f'{self.resource_path}/1111')
        assert 400 == response.status_code
        assert b'Article does not exist' in response.data

    def test_when_found(self, client: Client, db_session: Session) -> None:
        db_session.bulk_save_objects([
            CategoryEntity(id=1, name='name'),
            ArticleEntity(id=1, title='title', category_id=1)
        ])
        db_session.commit()
        response = client.get(f'{self.resource_path}/1')
        assert 200 == response.status_code
        assert 1 == response.json['id']
