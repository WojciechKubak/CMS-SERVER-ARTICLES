from articles.infrastructure.api.service import ArticleApiService, CategoryApiService, TagApiService
from articles.domain.service import ArticleDomainService, CategoryDomainService, TagDomainService
import pytest


@pytest.fixture(scope='session')
def article_api_service(article_domain_service: ArticleDomainService) -> ArticleApiService:
    return ArticleApiService(article_domain_service)


@pytest.fixture(scope='session')
def category_api_service(category_domain_service: CategoryDomainService) -> CategoryApiService:
    return CategoryApiService(category_domain_service)


@pytest.fixture(scope='session')
def tag_api_service(tag_domain_service: TagDomainService) -> TagApiService:
    return TagApiService(tag_domain_service)
