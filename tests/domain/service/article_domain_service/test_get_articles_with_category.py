from articles.domain.service import ArticleService
from articles.domain.errors import CategoryNotFoundError
from tests.factory import ArticleEntityFactory, CategoryEntityFactory
import pytest


class TestGetArticlesWithCategory:

    def test_when_no_articles(self, article_domain_service: ArticleService) -> None:
        category = CategoryEntityFactory()
        result = article_domain_service.get_articles_with_category(category.id)
        assert not result

    def test_when_no_category(self, article_domain_service: ArticleService) -> None:
        with pytest.raises(CategoryNotFoundError) as e:
            article_domain_service.get_articles_with_category(999)
        assert CategoryNotFoundError().message == str(e.value)

    def test_when_articles(
        self,
        article_domain_service: ArticleService,
    ) -> None:
        category = CategoryEntityFactory()
        ArticleEntityFactory.create_batch(5, category=category)

        result = article_domain_service.get_articles_with_category(category.id)

        assert all(["path_content" == r.content for r in result])
