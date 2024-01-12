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
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, Response, make_response
from flask_restful import Api
from dotenv import load_dotenv
import logging

app = Flask(__name__)


def create_app() -> Flask:

    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=0
    )

    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    app.config.from_object(get_app_configuration())

    with app.app_context():

        @app.get('/')
        def index() -> Response:
            return make_response({'message': 'Articles home page'}, 200)

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

        return app
