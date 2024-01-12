from articles.infrastructure.api.service import ArticleApiService
from articles.infrastructure.db.entity import ArticleEntity
from sqlalchemy.orm import Session
import pytest


class TestGetArticleById:

    def test_when_not_found(self, article_api_service: ArticleApiService) -> None:
        with pytest.raises(ValueError) as err:
            article_api_service.get_article_by_id(9999)
        assert 'Article does not exist' == str(err.value)

    def test_when_found(self, article_api_service: ArticleApiService, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=1, title='title'))
        db_session.commit()
        result = article_api_service.get_article_by_id(1)
        assert db_session.query(ArticleEntity).filter_by(id=result.id_).first()
