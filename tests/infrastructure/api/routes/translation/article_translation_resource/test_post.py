from articles.infrastructure.db.entity import (
    TranslationEntity, 
    LanguageEntity, 
    ArticleEntity, 
    CategoryEntity
)
from flask.testing import Client
from sqlalchemy.orm import Session


class TestRequestTranslation:

    def test_when_no_language(self, client: Client) -> None:
        response = client.post('articles/1/languages/1')
        assert 400 == response.status_code
        assert b'Language does not exist' in response.data

    def test_when_no_article(self, client: Client, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
        db_session.commit()
        response = client.post('articles/1/languages/1')
        assert 400 == response.status_code
        assert b'Article does not exist' in response.data

    def test_when_translation_exists(self, client: Client, db_session: Session) -> None:
        db_session.bulk_save_objects([
            LanguageEntity(id=1, name='name', code='CODE'),
            ArticleEntity(id=1, title='title'),
            TranslationEntity(id=1, language_id=1, article_id=1)
        ])
        db_session.commit()
        response = client.post('articles/1/languages/1')
        assert 400 == response.status_code
        assert b'Translation already exists' in response.data

    def test_when_translation_requested(self, client: Client, db_session: Session) -> None:
        db_session.bulk_save_objects([
            LanguageEntity(id=1, name='name', code='CODE'),
            CategoryEntity(id=1, name='name'),
            ArticleEntity(id=1, title='title', category_id=1)
        ])
        db_session.commit()
        response = client.post('articles/1/languages/1')
        assert 200 == response.status_code
        assert db_session.query(TranslationEntity).filter_by(id=response.json['id']).first()
