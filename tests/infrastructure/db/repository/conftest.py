from articles.infrastructure.db.repository import ArticleRepository, CategoryRepository, TagRepository
from sqlalchemy import Engine
import pytest


@pytest.fixture(scope='session')
def article_repository(db_engine: Engine) -> ArticleRepository:
    return ArticleRepository(db_engine)


@pytest.fixture(scope='session')
def category_repository(db_engine: Engine) -> CategoryRepository:
    return CategoryRepository(db_engine)


@pytest.fixture(scope='session')
def tag_repository(db_engine: Engine) -> TagRepository:
    return TagRepository(db_engine)
