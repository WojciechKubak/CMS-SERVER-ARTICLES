from articles.infrastructure.persistance.entity import ArticleEntity
from articles.domain.service import ArticleService
from articles.domain.errors import (
    ArticleTitleExistsError,
    CategoryNotFoundError,
    TagNotFoundError
)
from tests.factory import (
    ArticleFactory,
    ArticleEntityFactory,
    CategoryEntityFactory,
    TagEntityFactory
)
import pytest


class TestCreateArticle:

    def test_when_title_exists(
            self,
            article_domain_service: ArticleService
    ) -> None:
        article_dao = ArticleEntityFactory()
        article = ArticleFactory(title=article_dao.title)

        with pytest.raises(ArticleTitleExistsError) as e:
            article_domain_service.create_article(article)

        assert ArticleTitleExistsError().message == str(e.value)

    def test_when_no_category(
            self,
            article_domain_service: ArticleService
    ) -> None:
        article = ArticleFactory()

        with pytest.raises(CategoryNotFoundError) as e:
            article_domain_service.create_article(article)

        assert CategoryNotFoundError().message == str(e.value)

    def test_when_no_tag(self, article_domain_service: ArticleService) -> None:
        category_dao = CategoryEntityFactory()
        article = ArticleFactory(category=category_dao.id)

        with pytest.raises(TagNotFoundError) as e:
            article_domain_service.create_article(article)

        assert TagNotFoundError().message == str(e.value)

    def test_when_created(
            self,
            article_domain_service: ArticleService
    ) -> None:
        category_dao = CategoryEntityFactory()
        tags_dao = TagEntityFactory.create_batch(3)
        article = ArticleFactory(
            category=category_dao.id,
            tags=[tag.id for tag in tags_dao]
        )

        result = article_domain_service.create_article(article)

        expected = ArticleEntity.query.filter_by(id=result.id_).first()
        assert expected.id == result.id_
        assert 'path' == expected.content_path
