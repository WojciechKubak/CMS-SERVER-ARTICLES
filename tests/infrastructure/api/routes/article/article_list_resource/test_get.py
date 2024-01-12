from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity
from flask.testing import Client
from sqlalchemy.orm import Session


def test_article_list_resource_get(client: Client, db_session: Session) -> None:
    articles_dto = [ArticleEntity(title='', category_id=1), ArticleEntity(title='', category_id=1)]
    db_session.bulk_save_objects([CategoryEntity(id=1, name=''), *articles_dto])
    db_session.commit()
    response = client.get('/articles')
    assert 200 == response.status_code
    assert len(articles_dto) == len(response.json)
