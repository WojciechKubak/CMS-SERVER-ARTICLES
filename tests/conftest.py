from articles.infrastructure.db.repository import ArticleRepository, CategoryRepository, TagRepository
from articles.infrastructure.db.entity import Base
from articles.config import TestingConfig
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
import pytest


@pytest.fixture(scope='session', autouse=True)
def db_engine() -> Engine:
    engine_ = create_engine(TestingConfig.DATABASE_URI, echo=False)
    yield engine_
    engine_.dispose()


@pytest.fixture(scope='session')
def db_session_factory(db_engine: Engine) -> scoped_session:
    return scoped_session(sessionmaker(bind=db_engine, expire_on_commit=False))


@pytest.fixture(scope='function')
def db_session(db_session_factory: scoped_session) -> Session:
    session_ = db_session_factory()
    yield session_
    session_.rollback()
    session_.close()


@pytest.fixture(scope="function", autouse=True)
def tables(db_engine: Engine):
    Base.metadata.create_all(db_engine)
    yield
    Base.metadata.drop_all(db_engine)


@pytest.fixture(scope='session')
def article_repository(db_engine: Engine) -> ArticleRepository:
    return ArticleRepository(db_engine)


@pytest.fixture(scope='session')
def category_repository(db_engine: Engine) -> CategoryRepository:
    return CategoryRepository(db_engine)


@pytest.fixture(scope='session')
def tag_repository(db_engine: Engine) -> TagRepository:
    return TagRepository(db_engine)
