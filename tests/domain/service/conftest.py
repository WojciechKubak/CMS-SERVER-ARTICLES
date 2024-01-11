from articles.infrastructure.adapters.adapters import ArticleDbAdapter, CategoryDbAdapter, TagDbAdapter
from articles.domain.service import ArticleDomainService, CategoryDomainService, TagDomainService
import pytest


@pytest.fixture(scope='function')
def tag_domain_service(tag_db_adapter: TagDbAdapter) -> TagDomainService:
    return TagDomainService(tag_db_adapter)


@pytest.fixture(scope='session')
def category_domain_service(category_db_adapter: CategoryDbAdapter) -> CategoryDomainService:
    return CategoryDomainService(category_db_adapter)


@pytest.fixture(scope='session')
def article_domain_service(
        article_db_adapter: ArticleDbAdapter,
        category_db_adapter: CategoryDbAdapter,
        tag_db_adapter: CategoryDbAdapter
) -> ArticleDomainService:
    return ArticleDomainService(article_db_adapter, category_db_adapter, tag_db_adapter)
