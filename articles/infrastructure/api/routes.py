from articles.infrastructure.api.configuration import (
    category_service, 
    article_service, 
    tag_service,
    language_service,
    translation_service
)
from articles.infrastructure.api.dto import CategoryDTO, TagDTO, ArticleDTO, LanguageDTO
from flask_restful import Resource, reqparse
from flask import Response, make_response


class CategoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str)

    def post(self) -> Response:
        try:
            dto = CategoryDTO.from_dto(CategoryResource.parser.parse_args())
            category = category_service.create_category(dto)
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
            dto = CategoryDTO.from_dto(CategoryResource.parser.parse_args() | {'id_': id_})
            category = category_service.update_category(dto)
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
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('tags_id', type=int, action='append', nullable=False)

    def post(self) -> Response:
        try:
            dto = ArticleDTO.from_dto(ArticleResource.parser.parse_args())
            article = article_service.create_article(dto)
            return make_response(article.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class ArticleIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str, nullable=False)
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
            data = ArticleDTO.from_dto(ArticleResource.parser.parse_args() | {'id_': id_})
            article = article_service.update_article(data)
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
    

class TranslationIdResource(Resource):

    def get(self, id_: int) -> Response:
        try:
            translation = translation_service.get_translation_by_id(id_)
            return make_response(translation.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)
    

class ArticleTranslationResource(Resource):

    def post(self, article_id: int, language_id: int) -> Response:
        try:
            translation = translation_service.request_translation(article_id, language_id)
            return make_response(translation.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


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
            dto = TagDTO.from_dto(TagIdResource.parser.parse_args() | {'id_': id_})
            tag = tag_service.update_tag(dto)
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
            dto = TagDTO.from_dto(TagIdResource.parser.parse_args())
            tag = tag_service.create_tag(dto)
            return make_response(tag.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class TagListResource(Resource):

    def get(self) -> Response:
        tags = tag_service.get_all_tags()
        return make_response([tag.to_json() for tag in tags], 200)


class LanguageIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('code', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        try:
            language = language_service.get_language_by_id(id_)
            return make_response(language.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def put(self, id_: int) -> Response:
        try:
            dto = LanguageDTO.from_dto(LanguageIdResource.parser.parse_args() | {'id_': id_})
            language = language_service.update_language(dto)
            return make_response(language.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def delete(self, id_: int) -> Response:
        try:
            language_id = language_service.delete_language(id_)
            return make_response({'message': f'Deleted language with id: {language_id}'}, 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class LanguageResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('code', type=str, nullable=False)

    def post(self) -> Response:
        try:
            dto = LanguageDTO.from_dto(LanguageResource.parser.parse_args())
            language = language_service.create_language(dto)
            return make_response(language.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class LanguageListResource(Resource):

    def get(self) -> Response:
        languages = language_service.get_all_languages()
        return make_response([language.to_json() for language in languages], 200)
