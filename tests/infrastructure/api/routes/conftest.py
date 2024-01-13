from articles.infrastructure.api.service import (
    ArticleApiService, 
    CategoryApiService, 
    TagApiService
)
from articles.infrastructure.api.routes import (
    CategoryResource,
    CategoryIdResource,
    CategoryListResource,
    ArticleResource,
    ArticleIdResource,
    ArticlesWithCategoryResource,
    ArticleListResource,
    TagResource,
    TagIdResource,
    TagListResource
)
from articles.config import Config
from flask import Flask
from flask.testing import Client
from flask_restful import Api
from unittest.mock import patch
import pytest


@pytest.fixture(autouse=True, scope='session')
def mock_services(
    article_api_service: ArticleApiService, 
    category_api_service: CategoryApiService, 
    tag_api_service: TagApiService
    ) -> None:
    with patch.multiple('articles.infrastructure.api.routes',
                        article_service=article_api_service,
                        category_service=category_api_service,
                        tag_service=tag_api_service):
        yield

@pytest.fixture(scope='function')
def app(config_settings: type[Config]) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_settings)

    api = Api(app, prefix='/articles')
    api.add_resource(CategoryResource, '/categories')
    api.add_resource(CategoryListResource, '/categories')
    api.add_resource(CategoryIdResource, '/categories/<int:id_>')

    api.add_resource(ArticleResource, '')
    api.add_resource(ArticleIdResource, '/<int:id_>')
    api.add_resource(ArticlesWithCategoryResource, '/category/<int:category_id>')
    api.add_resource(ArticleListResource, '')

    api.add_resource(TagResource, '/tags')
    api.add_resource(TagIdResource, '/tags/<int:id_>')
    api.add_resource(TagListResource, '/tags')
    
    yield app


@pytest.fixture(scope='function')
def client(app: Flask) -> Client:
    with app.test_client() as client:
        yield client
