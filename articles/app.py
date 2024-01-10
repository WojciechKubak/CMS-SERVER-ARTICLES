from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, Response, make_response
from dotenv import load_dotenv
import logging

app = Flask(__name__)


def create_app() -> Flask:
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=0
    )

    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    with app.app_context():

        @app.get('/')
        def index() -> Response:
            return make_response({'message': 'Articles home page'}, 200)

        return app
