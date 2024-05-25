from articles.env_config import TRANSLATED_ARTICLES_TOPIC
from articles.infrastructure.broker.configuration import kafka_manager
from articles.infrastructure.broker.consumer import consumer_service
from articles.infrastructure.broker.dto import TranslatedArticleDTO
from flask import Flask, Response, make_response
from flask_executor import Executor


def setup_start_pooling(app: Flask, executor: Executor) -> None:

    @app.route('/start')
    def start_pooling() -> Response:
        executor.submit(
            kafka_manager.consume_messages,
            TRANSLATED_ARTICLES_TOPIC,
            consumer_service.handle_translated_article,
            TranslatedArticleDTO
        )
        return make_response({'message': 'Started'}, 200)
