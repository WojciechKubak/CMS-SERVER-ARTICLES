from articles.infrastructure.api.service import ArticleApiService, CategoryApiService, TagApiService
from articles.domain.service import ArticleDomainService, CategoryDomainService, TagDomainService
from articles.infrastructure.db.repository import ArticleRepository, CategoryRepository, TagRepository
from articles.infrastructure.adapters.adapters import ArticleDbAdapter, CategoryDbAdapter, TagDbAdapter
from articles.infrastructure.db.entity import Base
from articles.config import get_app_configuration, Config
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
import pytest
import os


@pytest.fixture(scope='session', autouse=True)
def with_test_app_config() -> None:
    os.environ['APP_CONFIGURATION'] = 'testing'
    yield


@pytest.fixture(scope='session')
def config_settings(with_test_app_config) -> type[Config]:
    return get_app_configuration()


@pytest.fixture(scope='session')
def database_uri(config_settings: type[Config]) -> str:
    return config_settings.DATABASE_URI


@pytest.fixture(scope='session')
def db_engine(database_uri: str) -> Engine:
    engine_ = create_engine(database_uri, echo=False)
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


@pytest.fixture(scope='session')
def article_db_adapter(article_repository: ArticleRepository) -> ArticleDbAdapter:
    return ArticleDbAdapter(article_repository)


@pytest.fixture(scope='session')
def category_db_adapter(category_repository: CategoryRepository) -> CategoryDbAdapter:
    return CategoryDbAdapter(category_repository)


@pytest.fixture(scope='session')
def tag_db_adapter(tag_repository: TagRepository) -> TagDbAdapter:
    return TagDbAdapter(tag_repository)


@pytest.fixture(scope='session')
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


@pytest.fixture(scope='session')
def article_api_service(article_domain_service: ArticleDomainService) -> ArticleApiService:
    return ArticleApiService(article_domain_service)


@pytest.fixture(scope='session')
def category_api_service(category_domain_service: CategoryDomainService) -> CategoryApiService:
    return CategoryApiService(category_domain_service)


@pytest.fixture(scope='session')
def tag_api_service(tag_domain_service: TagDomainService) -> TagApiService:
    return TagApiService(tag_domain_service)
