from articles.domain.service import ArticleDomainService
from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity, TagEntity
from articles.domain.model import Article
from sqlalchemy.orm import Session
import pytest


class TestCreateArticle:

    def test_when_title_exists(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.add(ArticleEntity(title='name'))
        db_session.commit()
        article = Article(
            id_=None,
            title='title',
            content='dummy',
            category=1,
            tags=[1, 2]
        )
        with pytest.raises(ValueError) as err:
            article_domain_service.create_article(article)
            assert 'Article name already exists' == str(err.value)

    def test_when_no_category(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.add(ArticleEntity(title='name'))
        db_session.commit()
        article = Article(
            id_=None,
            title='title',
            content='dummy',
            category=1,
            tags=[1, 2]
        )
        with pytest.raises(ValueError) as err:
            article_domain_service.create_article(article)
            assert 'Category does not exist' == str(err.value)

    def test_when_no_tag(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.add(ArticleEntity(title='name'))
        db_session.commit()
        article = Article(
            id_=None,
            title='title',
            content='dummy',
            category=1,
            tags=[1, 2]
        )
        with pytest.raises(ValueError) as err:
            article_domain_service.create_article(article)
            assert 'Tag does not exist' == str(err.value)

    def test_when_created(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            CategoryEntity(id=1, name=''),
            TagEntity(id=1, name=''),
            TagEntity(id=2, name='')
        ])
        db_session.commit()
        article = Article(
            id_=None,
            title='title',
            content='dummy',
            category=1,
            tags=[]
        )
        article_domain_service.create_article(article)
        assert db_session.query(ArticleEntity).filter_by(title='title').first()
