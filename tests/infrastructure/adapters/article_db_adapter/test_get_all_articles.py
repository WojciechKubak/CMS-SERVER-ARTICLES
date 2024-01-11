from articles.infrastructure.adapters.adapters import ArticleDbAdapter
from articles.infrastructure.db.entity import ArticleEntity
from sqlalchemy.orm import Session


def test_get_all_articles(article_db_adapter: ArticleDbAdapter, db_session: Session) -> None:
    articles_dto = [ArticleEntity(title='title', content='dummy'), ArticleEntity(title='title', content='dummy')]
    db_session.bulk_save_objects(articles_dto)
    db_session.commit()
    result = article_db_adapter.get_all_articles()
    assert len(result)
