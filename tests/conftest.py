from articles.infrastructure.api.service import (
    ArticleApiService, 
    CategoryApiService, 
    TagApiService,
    LanguageApiService,
    TranslationApiService
)
from articles.domain.service import (
    ArticleDomainService, 
    CategoryDomainService, 
    TagDomainService,
    LanguageDomainService,
    TranslationDomainService
)
from articles.infrastructure.db.repository import (
    ArticleRepository, 
    CategoryRepository, 
    TagRepository,
    TranslationRepository,
    LanguageRepository
)
from articles.infrastructure.adapters.adapters import (
    ArticleDbAdapter, 
    CategoryDbAdapter, 
    TagDbAdapter, 
    TranslationDbAdapter,
    LanguageDbAdapter,
    FileStorageAdapter,
    ArticleMessageBroker,
    LanguageMessageBroker
)
from articles.infrastructure.broker.manager import ConfluentKafkaManager
from articles.infrastructure.db.entity import Base
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from unittest.mock import MagicMock
import pytest


@pytest.fixture(scope='session')
def database_uri() -> str:
    return 'mysql://user:user1234@localhost:3311/db_test'


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
def translation_repository(db_engine: Engine) -> TranslationRepository:
    return TranslationRepository(db_engine)


@pytest.fixture(scope='session')
def language_repository(db_engine: Engine) -> LanguageRepository:
    return LanguageRepository(db_engine)


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
def translation_db_adapter(translation_repository: TranslationRepository) -> TranslationDbAdapter:
    return TranslationDbAdapter(translation_repository)


@pytest.fixture(scope='session')
def language_db_adapter(language_repository: LanguageRepository) -> LanguageDbAdapter:
    return LanguageDbAdapter(language_repository)


@pytest.fixture(scope='session')
def tag_domain_service(tag_db_adapter: TagDbAdapter) -> TagDomainService:
    return TagDomainService(tag_db_adapter)


@pytest.fixture(scope='session')
def category_domain_service(category_db_adapter: CategoryDbAdapter) -> CategoryDomainService:
    return CategoryDomainService(category_db_adapter)


@pytest.fixture(scope='session')
def language_domain_service(
    language_db_adapter: LanguageDbAdapter,
    language_message_broker: LanguageMessageBroker
    ) -> LanguageDomainService:
    return LanguageDomainService(language_db_adapter, language_message_broker)


@pytest.fixture(scope='session')
def article_message_broker() -> ArticleMessageBroker:
    mock = MagicMock(spec=ArticleMessageBroker)
    mock.return_value = None
    return mock

@pytest.fixture(scope='session')
def language_message_broker() -> LanguageMessageBroker:
    mock = MagicMock(spec=LanguageMessageBroker)
    mock.return_value = None
    return mock


@pytest.fixture(scope='session')
def file_storage_adapter() -> FileStorageAdapter:
    mock = MagicMock(spec=FileStorageAdapter)
    mock.read_content.return_value = 'path'
    return mock


@pytest.fixture(scope='session')
def translation_domain_service(
    article_db_adapter: ArticleDbAdapter,
    language_db_adapter: LanguageDbAdapter,
    translation_db_adapter: TranslationDbAdapter,
    file_storage_adapter: FileStorageAdapter,
    article_message_broker: ArticleMessageBroker
) -> TranslationDomainService:
    return TranslationDomainService(
        article_db_adapter,
        language_db_adapter,
        translation_db_adapter,
        file_storage_adapter,
        article_message_broker
    )


@pytest.fixture(scope='session')
def article_domain_service(
        article_db_adapter: ArticleDbAdapter,
        category_db_adapter: CategoryDbAdapter,
        tag_db_adapter: CategoryDbAdapter,
        file_storage_adapter: FileStorageAdapter
) -> ArticleDomainService:
    return ArticleDomainService(
        article_db_adapter, 
        category_db_adapter, 
        tag_db_adapter, 
        file_storage_adapter
    )


@pytest.fixture(scope='session')
def article_api_service(article_domain_service: ArticleDomainService) -> ArticleApiService:
    return ArticleApiService(article_domain_service)


@pytest.fixture(scope='session')
def category_api_service(category_domain_service: CategoryDomainService) -> CategoryApiService:
    return CategoryApiService(category_domain_service)


@pytest.fixture(scope='session')
def tag_api_service(tag_domain_service: TagDomainService) -> TagApiService:
    return TagApiService(tag_domain_service)


@pytest.fixture(scope='session')
def language_api_service(language_domain_service: LanguageDomainService) -> LanguageApiService:
    return LanguageApiService(language_domain_service)


@pytest.fixture(scope='session')
def translation_api_service(translation_domain_service: TranslationDomainService) -> TranslationApiService:
    return TranslationApiService(translation_domain_service)
