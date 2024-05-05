from articles.infrastructure.api.service import ArticleApiService
from articles.infrastructure.api.dto import ArticleDTO
from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity, TagEntity
from sqlalchemy.orm import Session
import pytest


class TestCreateArticle:

    def test_when_not_found(self, article_api_service: ArticleApiService) -> None:
        article_dto = ArticleDTO(
            id_=None,
            title='title',
            content='dummy',
            category_id=1,
            tags_id=[1, 2]
        )
        with pytest.raises(ValueError) as err:
            article_api_service.update_article(article_dto)
            assert 'Article does not exist' == str(err.value)

    def test_when_title_exists(self, article_api_service: ArticleApiService, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=2, title='title'))
        db_session.commit()
        article_dto = ArticleDTO(
            id_=None,
            title='title',
            content='dummy',
            category_id=1,
            tags_id=[1, 2]
        )
        with pytest.raises(ValueError) as err:
            article_api_service.update_article(article_dto)
            assert 'Article name already exists' == str(err.value)

    def test_when_no_category(self, article_api_service: ArticleApiService) -> None:
        article_dto = ArticleDTO(
            id_=None,
            title='title',
            content='dummy',
            category_id=1,
            tags_id=[1, 2]
        )
        with pytest.raises(ValueError) as err:
            article_api_service.update_article(article_dto)
            assert 'Category does not exist' == str(err.value)

    def test_when_no_tag(self, article_api_service: ArticleApiService, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1))
        article_dto = ArticleDTO(
            id_=None,
            title='title',
            content='dummy',
            category_id=1,
            tags_id=[1, 2]
        )
        with pytest.raises(ValueError) as err:
            article_api_service.update_article(article_dto)
            assert 'Tag does not exist' == str(err.value)

    def test_when_created(self, article_api_service: ArticleApiService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            ArticleEntity(id=1, title='title'),
            CategoryEntity(id=1, name=''),
            TagEntity(id=1, name=''),
            TagEntity(id=2, name='')
        ])
        db_session.commit()
        article_dto = ArticleDTO(
            id_=1,
            title='title',
            content='dummy',
            category_id=1,
            tags_id=[1, 2]
        )
        article_api_service.update_article(article_dto)
        assert db_session.query(ArticleEntity).filter_by(id=1).first()
