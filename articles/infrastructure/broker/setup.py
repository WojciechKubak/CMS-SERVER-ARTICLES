from articles.env_config import TRANSLATED_ARTICLES_TOPIC
from articles.infrastructure.broker.configuration import kafka_manager
from articles.infrastructure.broker.consumer import consumer_service
from articles.infrastructure.broker.dto import TranslatedArticleDTO
from flask import Flask, Response, make_response
from flask_executor import Executor


def setup_start_pooling(app: Flask, executor: Executor) -> None:
    """
    Setup the '/start' route to start consuming messages from Kafka.

    This function creates a route that, when accessed, starts a new task in
    the executor to consume messages from Kafka.
    The messages are consumed from the topic specified in the
    environment configuration and are handled by the consumer service.

    Args:
        app (Flask): The Flask application.
        executor (Executor): The executor to run tasks.
    """

    @app.route('/start')
    def start_pooling() -> Response:
        """
        Start consuming messages from Kafka.

        This function starts a new task in the executor to consume messages
        from Kafka.
        The messages are consumed from the topic specified in the environment
        configuration and are handled by the consumer service.

        Returns:
            Response: The HTTP response.
        """
        executor.submit(
            kafka_manager.consume_messages,
            TRANSLATED_ARTICLES_TOPIC,
            consumer_service.handle_translated_article,
            TranslatedArticleDTO
        )
        return make_response({'message': 'Started'}, 200)
