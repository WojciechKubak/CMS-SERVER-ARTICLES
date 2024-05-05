from articles.infrastructure.api.service import (
    ArticleApiService, 
    CategoryApiService, 
    TagApiService,
    LanguageApiService,
    TranslationApiService
)
from articles import create_app
from articles.config import TestingConfig
from flask import Flask
from flask.testing import Client
from unittest.mock import patch
import pytest


@pytest.fixture(autouse=True, scope='session')
def mock_services(
    article_api_service: ArticleApiService, 
    category_api_service: CategoryApiService, 
    tag_api_service: TagApiService,
    language_api_service: LanguageApiService,
    translation_api_service: TranslationApiService
    ) -> None:
    with patch.multiple('articles.infrastructure.api.routes',
                        article_service=article_api_service,
                        category_service=category_api_service,
                        tag_service=tag_api_service,
                        language_service=language_api_service,
                        translation_service=translation_api_service
        ):
        yield


@pytest.fixture(scope='function')
def app() -> Flask:
    yield create_app(TestingConfig)


@pytest.fixture(scope='function')
def client(app: Flask) -> Client:
    with app.test_client() as client:
        yield client
