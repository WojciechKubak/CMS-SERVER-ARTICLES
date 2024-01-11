from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity
from sqlalchemy.orm import Session


def test_get_all_articles(article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
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
    result = article_db_adapter.get_articles_with_category(1)
    assert len([article for article in articles_dto if article.category_id == 1]) == len(result)
