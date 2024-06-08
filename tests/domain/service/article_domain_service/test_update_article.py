from articles.infrastructure.persistance.entity import ArticleEntity
from articles.domain.service import ArticleService
from articles.domain.errors import (
    ArticleNotFoundError,
    ArticleTitleExistsError,
    CategoryNotFoundError,
    TagNotFoundError,
)
from tests.factory import ArticleFactory, ArticleEntityFactory
from unittest.mock import patch
import pytest


class TestUpdateArticle:

    def test_when_not_found(self, article_domain_service: ArticleService) -> None:
        article = ArticleFactory()
        with pytest.raises(ArticleNotFoundError) as e:
            article_domain_service.update_article(article)
        assert ArticleNotFoundError().message == str(e.value)

    def test_when_title_exists(self, article_domain_service: ArticleService) -> None:
        dao_first, dao_second = ArticleEntityFactory(), ArticleEntityFactory()
        article = ArticleFactory(id_=dao_first.id, title=dao_second.title)

        with pytest.raises(ArticleTitleExistsError) as e:
            article_domain_service.update_article(article)

        assert ArticleTitleExistsError().message == str(e.value)

    def test_when_no_category(self, article_domain_service: ArticleService) -> None:
        article_dao = ArticleEntityFactory()
        article = ArticleFactory(
            id_=article_dao.id, category=article_dao.category_id + 1
        )

        with pytest.raises(CategoryNotFoundError) as e:
            article_domain_service.update_article(article)

        assert CategoryNotFoundError().message == str(e.value)

    def test_when_no_tag(self, article_domain_service: ArticleService) -> None:
        article_dao = ArticleEntityFactory()
        article = ArticleFactory(id_=article_dao.id, category=article_dao.category_id)

        with pytest.raises(TagNotFoundError) as e:
            article_domain_service.update_article(article)

        assert TagNotFoundError().message == str(e.value)

    def test_when_updated(self, article_domain_service: ArticleService) -> None:
        article_dao = ArticleEntityFactory()
        new_title = f"new_{article_dao.title}"
        article = ArticleFactory(
            id_=article_dao.id,
            title=new_title,
            category=article_dao.category_id,
            tags=[tag.id for tag in article_dao.tags],
        )

        with patch.object(
            article_domain_service.file_storage, "update_content"
        ) as mock_delete_content:
            result = article_domain_service.update_article(article)

        mock_delete_content.assert_called_once()
        assert ArticleEntity.query.filter_by(id=result.id_).first().title == new_title
