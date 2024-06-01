from articles.config import Config
from articles.infrastructure.broker.setup import setup_start_pooling
from articles.infrastructure.api.setup import setup_routing
from articles.infrastructure.persistance.configuration import sa
from flask import Flask, Response, make_response
from flask_restful import Api
from flask_executor import Executor
from flask_migrate import Migrate


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    executor = Executor(app)
    setup_start_pooling(app, executor)

    sa.init_app(app)
    _ = Migrate(app, sa)

    api = Api(app, prefix='/articles')
    setup_routing(api)

    with app.app_context():

        @app.route('/health')
        def health() -> Response:
            return make_response({'message': 'OK'}, 200)

        return app
