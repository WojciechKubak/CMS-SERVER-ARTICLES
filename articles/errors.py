from articles.app import app
from flask import Response, make_response


@app.errorhandler(400)
def bad_request_error(error: int) -> Response:
    return make_response({'message': 'Bad Request'}), 400


@app.errorhandler(401)
def unauthorized_error(error: int) -> Response:
    return make_response({'message': 'Unauthorized'}), 401


@app.errorhandler(403)
def forbidden_error(error: int) -> Response:
    return make_response({'message': 'Forbidden'}), 403


@app.errorhandler(404)
def not_found_error(error: int) -> Response:
    return make_response({'message': 'Not Found'}), 404


@app.errorhandler(500)
def internal_error(error: int) -> Response:
    return make_response({'message': 'Internal Server Error'}), 500
