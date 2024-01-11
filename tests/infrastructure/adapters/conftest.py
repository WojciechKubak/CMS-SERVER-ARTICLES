from articles.infrastructure.db.repository import ArticleRepository, CategoryRepository, TagRepository
from articles.infrastructure.adapters.adapters import ArticleDbAdapter, CategoryDbAdapter, TagDbAdapter
import pytest


@pytest.fixture(scope='session')
def article_db_adapter(article_repository: ArticleRepository) -> ArticleDbAdapter:
    return ArticleDbAdapter(article_repository)


@pytest.fixture(scope='session')
def category_db_adapter(category_repository: CategoryRepository) -> CategoryDbAdapter:
    return CategoryDbAdapter(category_repository)


@pytest.fixture(scope='session')
def tag_db_adapter(tag_repository: TagRepository) -> TagDbAdapter:
    return TagDbAdapter(tag_repository)
