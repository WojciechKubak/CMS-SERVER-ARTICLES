from articles.infrastructure.db.repository import ArticleRepository
from articles.infrastructure.db.entity import CategoryEntity, ArticleEntity
from sqlalchemy.orm import Session


def test_find_many_by_id(article_repository: ArticleRepository, db_session: Session) -> None:
    category = CategoryEntity(name='category')
    articles = [ArticleEntity(title='', category_id=1), ArticleEntity(title='', category_id=1)]
    db_session.bulk_save_objects([category, *articles])
    db_session.commit()

    result = article_repository.find_by_category_id(1)
    assert len(articles) == len(result)
