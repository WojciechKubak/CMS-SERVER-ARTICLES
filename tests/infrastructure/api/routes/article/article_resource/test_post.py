from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity, TagEntity
from flask.testing import Client
from sqlalchemy.orm import Session


class TestIdResourcePut:
    resource_path = '/articles'

    def test_when_title_exists(self, client: Client, db_session: Session) -> None:
        db_session.bulk_save_objects([
            ArticleEntity(id=1, title='title'),
            ArticleEntity(id=2, title='updated_title'),
        ])
        db_session.commit()
        article_dto = {
            'title': 'updated_title',
            'content': 'dummy',
            'category_id': 1,
            'tags_id': [1, 2]
        }
        response = client.post(self.resource_path, json=article_dto)
        assert 400 == response.status_code
        assert b'Article title already exists' in response.data

    def test_when_no_category(self, client: Client, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=1, title='title'))
        db_session.commit()
        article_dto = {
            'title': 'updated_title',
            'content': 'dummy',
            'category_id': 1,
            'tags_id': [1, 2]
        }
        response = client.post(self.resource_path, json=article_dto)
        assert 400 == response.status_code
        assert b'Category does not exist' in response.data

    def test_when_no_tag(self, client: Client, db_session: Session) -> None:
        db_session.bulk_save_objects([
            ArticleEntity(id=1, title='title'),
            CategoryEntity(id=1, name='name'),
        ])
        db_session.commit()
        article_dto = {
            'title': 'updated_title',
            'content': 'dummy',
            'category_id': 1,
            'tags_id': [1, 2]
        }
        response = client.post(self.resource_path, json=article_dto)
        assert 400 == response.status_code
        assert b'Tag does not exist' in response.data

    def test_when_created(self, client: Client, db_session: Session) -> None:
        db_session.bulk_save_objects([
            ArticleEntity(id=1, title='title'),
            CategoryEntity(id=1, name=''),
            TagEntity(id=1, name=''),
            TagEntity(id=2, name='')
        ])
        db_session.commit()
        article_dto = {
            'title': 'updated_title',
            'content': 'dummy',
            'category_id': 1,
            'tags_id': [1, 2]
        }
        response = client.post(self.resource_path, json=article_dto)
        assert 201 == response.status_code
        assert db_session.query(ArticleEntity).filter_by(id=response.json['id']).first()
