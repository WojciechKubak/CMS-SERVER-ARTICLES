from articles.infrastructure.api.configuration import category_service, article_service, tag_service
from flask_restful import Resource, reqparse
from flask import Response, make_response
from datetime import datetime


class CategoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str)

    def post(self) -> Response:
        try:
            category = category_service.create_category(CategoryResource.parser.parse_args())
            return make_response(category.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class CategoryIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        try:
            category = category_service.get_category_by_id(id_)
            return make_response(category.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def put(self, id_: int) -> Response:
        try:
            category = category_service.update_category(CategoryIdResource.parser.parse_args() | {'id': id_})
            return make_response(category.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def delete(self, id_: int) -> Response:
        try:
            category_id = category_service.delete_category(id_)
            return make_response({'message': f'Deleted category with id: {category_id}'}, 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class CategoryListResource(Resource):

    def get(self) -> Response:
        categories = category_service.get_all_categories()
        return make_response([category.to_json() for category in categories], 200)


class ArticleResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str, nullable=False)
    parser.add_argument('publication_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'))
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('tags_id', type=int, action='append', nullable=False)

    def post(self) -> Response:
        try:
            article = article_service.create_article(ArticleResource.parser.parse_args())
            return make_response(article.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class ArticleIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str, nullable=False)
    parser.add_argument('publication_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'))
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('tags_id', type=int, action='append', nullable=False)

    def get(self, id_: int) -> Response:
        try:
            article = article_service.get_article_by_id(id_)
            return make_response(article.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def put(self, id_: int) -> Response:
        try:
            article = article_service.update_article(ArticleIdResource.parser.parse_args() | {'id': id_})
            return make_response(article.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def delete(self, id_: int) -> Response:
        try:
            article_id = article_service.delete_article(id_)
            return make_response({'message': f'Deleted article with id: {article_id}'}, 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class ArticlesWithCategoryResource(Resource):

    def get(self, category_id: str) -> Response:
        try:
            articles = article_service.get_articles_with_category(category_id)
            return make_response([article.to_json() for article in articles], 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class ArticleListResource(Resource):

    def get(self) -> Response:
        articles = article_service.get_all_articles()
        return make_response([article.to_json() for article in articles], 200)


class TagIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        try:
            tag = tag_service.get_tag_by_id(id_)
            return make_response(tag.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def put(self, id_: int) -> Response:
        try:
            tag = tag_service.update_tag(TagIdResource.parser.parse_args() | {'id': id_})
            return make_response(tag.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def delete(self, id_: int) -> Response:
        try:
            tag_id = tag_service.delete_tag(id_)
            return make_response({'message': f'Deleted tag with id: {tag_id}'}, 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class TagResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)

    def post(self) -> Response:
        try:
            tag = tag_service.create_tag(TagResource.parser.parse_args())
            return make_response(tag.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class TagListResource(Resource):

    def get(self) -> Response:
        tags = tag_service.get_all_tags()
        return make_response([tag.to_json() for tag in tags], 200)
