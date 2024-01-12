from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity
from flask.testing import Client
from sqlalchemy.orm import Session


def test_get_articles_with_category(client: Client, db_session: Session) -> None:
    categories_dto = [
        CategoryEntity(id=1, name='name'),
        CategoryEntity(id=2, name='name')
    ]
    articles_dto = [
        ArticleEntity(title='tilte', category_id=1),
        ArticleEntity(title='tilte', category_id=1),
        ArticleEntity(title='tilte', category_id=2)
    ]
    db_session.bulk_save_objects([*categories_dto, *articles_dto])
    db_session.commit()
    response = client.get('articles/category/1')
    assert 200 == response.status_code
    assert 2 == len(response.json)
