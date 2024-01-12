from articles.infrastructure.api.service import ArticleApiService
from articles.infrastructure.db.entity import ArticleEntity
from sqlalchemy.orm import Session


def test_get_all_articles(article_api_service: ArticleApiService, db_session: Session) -> None:
    articles_dto = [ArticleEntity(title=''), ArticleEntity(title='')]
    db_session.bulk_save_objects(articles_dto)
    db_session.commit()
    result = article_api_service.get_all_articles()
    assert len(articles_dto) == len(result)
