from articles.domain.service import ArticleDomainService
from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity
from articles.domain.model import Article, Category, Tag
from sqlalchemy.orm import Session
import pytest


class TestCreateArticle:

    def test_when_not_found(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        article = Article(
            id_=None,
            title='title',
            content='dummy',
            category=Category(id_=1, name='name', description='dummy'),
            tags=[]
        )
        with pytest.raises(ValueError) as err:
            article_domain_service.update_article(article)
            assert 'Article does not exist' == str(err.value)

    def test_when_title_exists(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=1, title='name'))
        db_session.commit()
        article = Article(
            id_=None,
            title='title',
            content='dummy',
            category=Category(id_=1, name='name', description='dummy'),
            tags=[]
        )
        with pytest.raises(ValueError) as err:
            article_domain_service.update_article(article)
            assert 'Article name already exists' == str(err.value)

    def test_when_no_category(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=1, title='name'))
        db_session.commit()
        article = Article(
            id_=None,
            title='title',
            content='dummy',
            category=Category(id_=1, name='name', description='dummy'),
            tags=[]
        )
        with pytest.raises(ValueError) as err:
            article_domain_service.update_article(article)
            assert 'Category does not exist' == str(err.value)

    def test_when_no_tag(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=1, title='name'))
        db_session.commit()
        article = Article(
            id_=None,
            title='title',
            content='dummy',
            category=Category(id_=1, name='name', description='dummy'),
            tags=[Tag(id_=1, name='name')]
        )
        with pytest.raises(ValueError) as err:
            article_domain_service.update_article(article)
            assert 'Tag does not exist' == str(err.value)

    def test_when_updated(self, article_domain_service: ArticleDomainService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            CategoryEntity(id=1, name='name'),
            ArticleEntity(id=1, title='title', content='dummy', category_id=1)
        ])
        db_session.commit()
        article = Article(
            id_=1,
            title='updated_title',
            content='dummy',
            category=Category(id_=1, name='name', description='dummy'),
            tags=[]
        )
        article_domain_service.update_article(article)
        assert 'updated_title' == db_session.query(ArticleEntity).filter_by(id=1).first().title
