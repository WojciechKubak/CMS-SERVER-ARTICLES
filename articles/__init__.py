from articles.config import Config
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
from flask import Flask, Response, make_response
from flask_restful import Api


def create_app(config: Config) -> Flask:

    app = Flask(__name__)
    app.config.from_object(config)

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

    with app.app_context():

        @app.route('/health')
        def index() -> Response:
            return make_response({'message': 'Articles home page'}, 200)

        return app
