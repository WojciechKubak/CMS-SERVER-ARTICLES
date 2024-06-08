from articles.infrastructure.api.service import (
    ArticleApiService,
    CategoryApiService,
    TagApiService,
    LanguageApiService,
    TranslationApiService,
)
from articles.domain.service import (
    ArticleService,
    CategoryService,
    TagService,
    LanguageService,
    TranslationService,
)
from articles.infrastructure.persistance.repository import (
    ArticleRepository,
    CategoryRepository,
    TagRepository,
    TranslationRepository,
    LanguageRepository,
)
from articles.infrastructure.adapters.adapters import (
    ArticleDbAdapter,
    CategoryDbAdapter,
    TagDbAdapter,
    TranslationDbAdapter,
    LanguageDbAdapter,
    FileStorageAdapter,
    ArticleMessageBroker,
    LanguageMessageBroker,
)
from articles.infrastructure.persistance.configuration import sa
from articles.app import create_app
from articles.config import TestingConfig
from flask import Flask
from flask.testing import Client
from unittest.mock import MagicMock
import pytest


@pytest.fixture(scope="function")
def app() -> Flask:
    yield create_app(TestingConfig)


@pytest.fixture(scope="function")
def client(app: Flask) -> Client:
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def db_setup_and_teardown(app: Flask) -> Flask:
    with app.app_context():
        sa.create_all()

        yield app

    with app.app_context():
        sa.drop_all()


@pytest.fixture(scope="session")
def article_repository() -> ArticleRepository:
    return ArticleRepository(sa)


@pytest.fixture(scope="session")
def category_repository() -> CategoryRepository:
    return CategoryRepository(sa)


@pytest.fixture(scope="session")
def tag_repository() -> TagRepository:
    return TagRepository(sa)


@pytest.fixture(scope="session")
def translation_repository() -> TranslationRepository:
    return TranslationRepository(sa)


@pytest.fixture(scope="session")
def language_repository() -> LanguageRepository:
    return LanguageRepository(sa)


@pytest.fixture(scope="session")
def article_db_adapter(article_repository: ArticleRepository) -> ArticleDbAdapter:
    return ArticleDbAdapter(article_repository)


@pytest.fixture(scope="session")
def category_db_adapter(category_repository: CategoryRepository) -> CategoryDbAdapter:
    return CategoryDbAdapter(category_repository)


@pytest.fixture(scope="session")
def tag_db_adapter(tag_repository: TagRepository) -> TagDbAdapter:
    return TagDbAdapter(tag_repository)


@pytest.fixture(scope="session")
def translation_db_adapter(
    translation_repository: TranslationRepository,
) -> TranslationDbAdapter:
    return TranslationDbAdapter(translation_repository)


@pytest.fixture(scope="session")
def language_db_adapter(language_repository: LanguageRepository) -> LanguageDbAdapter:
    return LanguageDbAdapter(language_repository)


@pytest.fixture(scope="session")
def tag_domain_service(tag_db_adapter: TagDbAdapter) -> TagService:
    return TagService(tag_db_adapter)


@pytest.fixture(scope="session")
def category_domain_service(category_db_adapter: CategoryDbAdapter) -> CategoryService:
    return CategoryService(category_db_adapter)


@pytest.fixture(scope="session")
def language_domain_service(
    language_db_adapter: LanguageDbAdapter,
    language_message_broker: LanguageMessageBroker,
) -> LanguageService:
    return LanguageService(language_db_adapter, language_message_broker)


@pytest.fixture(scope="session")
def article_message_broker() -> ArticleMessageBroker:
    mock = MagicMock(spec=ArticleMessageBroker)
    mock.return_value = None
    return mock


@pytest.fixture(scope="session")
def language_message_broker() -> LanguageMessageBroker:
    mock = MagicMock(spec=LanguageMessageBroker)
    mock.return_value = None
    return mock


@pytest.fixture(scope="session")
def file_storage_adapter() -> FileStorageAdapter:
    mock = MagicMock(spec=FileStorageAdapter)
    mock.read_content.return_value = "path_content"
    mock.upload_content.return_value = "path"
    return mock


@pytest.fixture(scope="session")
def translation_domain_service(
    article_db_adapter: ArticleDbAdapter,
    language_db_adapter: LanguageDbAdapter,
    translation_db_adapter: TranslationDbAdapter,
    file_storage_adapter: FileStorageAdapter,
    article_message_broker: ArticleMessageBroker,
) -> TranslationService:
    return TranslationService(
        article_db_adapter,
        language_db_adapter,
        translation_db_adapter,
        file_storage_adapter,
        article_message_broker,
    )


@pytest.fixture(scope="session")
def article_domain_service(
    article_db_adapter: ArticleDbAdapter,
    category_db_adapter: CategoryDbAdapter,
    tag_db_adapter: CategoryDbAdapter,
    file_storage_adapter: FileStorageAdapter,
) -> ArticleService:
    return ArticleService(
        article_db_adapter, category_db_adapter, tag_db_adapter, file_storage_adapter
    )


@pytest.fixture(scope="session")
def article_api_service(article_domain_service: ArticleService) -> ArticleApiService:
    return ArticleApiService(article_domain_service)


@pytest.fixture(scope="session")
def category_api_service(
    category_domain_service: CategoryService,
) -> CategoryApiService:
    return CategoryApiService(category_domain_service)


@pytest.fixture(scope="session")
def tag_api_service(tag_domain_service: TagService) -> TagApiService:
    return TagApiService(tag_domain_service)


@pytest.fixture(scope="session")
def language_api_service(
    language_domain_service: LanguageService,
) -> LanguageApiService:
    return LanguageApiService(language_domain_service)


@pytest.fixture(scope="session")
def translation_api_service(
    translation_domain_service: TranslationService,
) -> TranslationApiService:
    return TranslationApiService(translation_domain_service)
