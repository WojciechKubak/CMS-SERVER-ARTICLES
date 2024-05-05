from articles.config import Config
from articles.env_config import TRANSLATED_ARTICLES_TOPIC
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
    TagListResource,
    ArticleTranslationResource,
    TranslationIdResource,
    LanguageIdResource,
    LanguageResource,
    LanguageListResource
)
from articles.infrastructure.broker.consumer import article_translation_consumer
from articles.infrastructure.broker.configuration import kafka_manager
from flask import Flask, Response, make_response
from flask_restful import Api
import threading
import logging

logging.basicConfig(level=logging.INFO)


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    consume_thread = threading.Thread(
        target=kafka_manager.consume_messages, 
        args=(TRANSLATED_ARTICLES_TOPIC, article_translation_consumer.handle_event,),
        daemon=True
    )
    consume_thread.start()

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

    api.add_resource(LanguageResource, '/languages')
    api.add_resource(LanguageIdResource, '/languages/<int:id_>')
    api.add_resource(LanguageListResource, '/languages')

    api.add_resource(ArticleTranslationResource, '/<int:article_id>/languages/<int:language_id>')
    api.add_resource(TranslationIdResource, '/translations/<int:id_>')

    with app.app_context():

        @app.route('/health')
        def index() -> Response:
            return make_response({'message': 'Articles home page'}, 200)

        return app
