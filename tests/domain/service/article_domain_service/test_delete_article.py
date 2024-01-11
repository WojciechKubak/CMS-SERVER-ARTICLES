from articles.domain.service import ArticleDomainService
from articles.infrastructure.db.entity import ArticleEntity
from sqlalchemy.orm import Session
import pytest


class TestDeleteArticle:

    def test_when_not_found(self, article_domain_service: ArticleDomainService) -> None:
        with pytest.raises(ValueError) as err:
            article_domain_service.delete_article(9999)
        assert 'Article does not exist' == str(err.value)

    def test_when_deleted(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=1, title='title'))
        db_session.commit()
        result = article_domain_service.delete_article(1)
        assert not db_session.query(ArticleEntity).filter_by(id=result).first()
