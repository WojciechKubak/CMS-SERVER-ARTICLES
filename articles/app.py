from articles.web.configuration import app
from flask import Flask, Response, make_response
from dotenv import load_dotenv
import logging


def create_app() -> Flask:

    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    with app.app_context():

        @app.get('/')
        def index() -> Response:
            return make_response({'message': 'Articles home page'}, 200)

        return app
