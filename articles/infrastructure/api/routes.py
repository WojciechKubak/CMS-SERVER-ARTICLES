from articles.infrastructure.api.configuration import (
    category_service,
    article_service,
    tag_service,
    language_service,
    translation_service
)
from articles.infrastructure.api.dto import (
    LanguageCreateDTO,
    LanguageUpdateDTO,
    CategoryCreateDTO,
    CategoryUpdateDTO,
    ArticleCreateDTO,
    ArticleUpdateDTO,
    TagCreateDTO,
    TagUpdateDTO,
)
from articles.infrastructure.api.errors import ApplicationError
from flask_restful import Resource, reqparse
from flask import Response, make_response


class CategoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str)

    def post(self) -> Response:
        try:
            data = CategoryResource.parser.parse_args()
            dto = CategoryCreateDTO.from_dict(data)
            category = category_service.create_category(dto)
            return make_response(category.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class CategoryIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        try:
            category = category_service.get_category_by_id(id_)
            return make_response(category.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def put(self, id_: int) -> Response:
        try:
            data = CategoryResource.parser.parse_args() | {'id': id_}
            dto = CategoryUpdateDTO.from_dict(data)
            category = category_service.update_category(dto)
            return make_response(category.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def delete(self, id_: int) -> Response:
        try:
            category_id = category_service.delete_category(id_)
            return make_response({'id': category_id}, 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class CategoryListResource(Resource):

    def get(self) -> Response:
        categories = category_service.get_all_categories()
        return make_response(
            [category.to_dict() for category in categories],
            200
        )


class ArticleResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str, nullable=False)
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('tags_id', type=int, action='append', nullable=False)

    def post(self) -> Response:
        try:
            data = ArticleResource.parser.parse_args()
            dto = ArticleCreateDTO.from_dict(data)
            article = article_service.create_article(dto)
            return make_response(article.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class ArticleIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str, nullable=False)
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('tags_id', type=int, action='append', nullable=True)

    def get(self, id_: int) -> Response:
        try:
            article = article_service.get_article_by_id(id_)
            return make_response(article.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def put(self, id_: int) -> Response:
        try:
            data = ArticleResource.parser.parse_args() | {'id': id_}
            dto = ArticleUpdateDTO.from_dict(data)
            article = article_service.update_article(dto)
            return make_response(article.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def delete(self, id_: int) -> Response:
        try:
            article_id = article_service.delete_article(id_)
            return make_response({'id': article_id}, 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class ArticlesWithCategoryResource(Resource):

    def get(self, category_id: str) -> Response:
        try:
            articles = article_service.get_articles_with_category(category_id)
            return make_response(
                [article.to_dict() for article in articles],
                200
            )
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class ArticleListResource(Resource):

    def get(self) -> Response:
        articles = article_service.get_all_articles()
        return make_response([article.to_dict() for article in articles], 200)


class TranslationIdResource(Resource):

    def get(self, id_: int) -> Response:
        try:
            translation = translation_service.get_translation_by_id(id_)
            return make_response(translation.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class ArticleTranslationResource(Resource):

    def post(self, article_id: int, language_id: int) -> Response:
        try:
            translation = translation_service.request_translation(
                article_id, language_id)
            return make_response(translation.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class TagIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        try:
            tag = tag_service.get_tag_by_id(id_)
            return make_response(tag.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def put(self, id_: int) -> Response:
        try:
            data = TagIdResource.parser.parse_args() | {'id': id_}
            dto = TagUpdateDTO.from_dict(data)
            tag = tag_service.update_tag(dto)
            return make_response(tag.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def delete(self, id_: int) -> Response:
        try:
            tag_id = tag_service.delete_tag(id_)
            return make_response({'id': tag_id}, 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class TagResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)

    def post(self) -> Response:
        try:
            data = TagResource.parser.parse_args()
            dto = TagCreateDTO.from_dict(data)
            tag = tag_service.create_tag(dto)
            return make_response(tag.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class TagListResource(Resource):

    def get(self) -> Response:
        tags = tag_service.get_all_tags()
        return make_response([tag.to_dict() for tag in tags], 200)


class LanguageIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('code', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        try:
            language = language_service.get_language_by_id(id_)
            return make_response(language.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def put(self, id_: int) -> Response:
        try:
            data = LanguageIdResource.parser.parse_args() | {'id': id_}
            dto = LanguageUpdateDTO.from_dict(data)
            language = language_service.update_language(dto)
            return make_response(language.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def delete(self, id_: int) -> Response:
        try:
            language_id = language_service.delete_language(id_)
            return make_response({'id': language_id}, 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class LanguageResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('code', type=str, nullable=False)

    def post(self) -> Response:
        try:
            data = LanguageResource.parser.parse_args()
            dto = LanguageCreateDTO.from_dict(data)
            language = language_service.create_language(dto)
            return make_response(language.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class LanguageListResource(Resource):

    def get(self) -> Response:
        languages = language_service.get_all_languages()
        return make_response(
            [language.to_dict() for language in languages],
            200
        )
