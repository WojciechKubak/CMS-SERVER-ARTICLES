from articles.infrastructure.db.entity import TranslationEntity, ArticleEntity, LanguageEntity
from sqlalchemy.orm import Session
from flask.testing import Client


class TestIdResourceGet:
    resource_path = '/articles/translations'

    def test_when_not_found(self, client: Client) -> None:
        response = client.get(f'{self.resource_path}/1111')
        assert 400 == response.status_code
        assert b'Translation does not exist' in response.data

    def test_when_found(self, client: Client, db_session: Session) -> None:
        db_session.bulk_save_objects([
            LanguageEntity(id=1, name='name', code='CODE'),
            ArticleEntity(id=1, title='title'),
            TranslationEntity(id=1, language_id=1, article_id=1)
        ])
        db_session.commit()
        response = client.get(f'{self.resource_path}/1')
        assert 200 == response.status_code
        assert 1 == response.json['id']
