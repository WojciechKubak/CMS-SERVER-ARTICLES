from articles.config import get_app_configuration
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
from flask import Flask
from flask.testing import Client
from flask_restful import Api
import pytest


@pytest.fixture(scope='function')
def app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_app_configuration())

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
