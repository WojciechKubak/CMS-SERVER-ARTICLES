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
    """
    Resource for creating a new Category.

    Attributes:
        parser (RequestParser): Parser for the request data.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str)

    def post(self) -> Response:
        """
        Create a new Category.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            data = CategoryResource.parser.parse_args()
            dto = CategoryCreateDTO.from_dict(data)
            category = category_service.create_category(dto)
            return make_response(category.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class CategoryIdResource(Resource):
    """
    Resource for getting, updating, and deleting a Category by its ID.

    Attributes:
        parser (RequestParser): Parser for the request data.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        """
        Get a Category by its ID.

        Args:
            id_ (int): The ID of the Category.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            category = category_service.get_category_by_id(id_)
            return make_response(category.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def put(self, id_: int) -> Response:
        """
        Update a Category by its ID.

        Args:
            id_ (int): The ID of the Category.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            data = CategoryResource.parser.parse_args() | {'id': id_}
            dto = CategoryUpdateDTO.from_dict(data)
            category = category_service.update_category(dto)
            return make_response(category.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def delete(self, id_: int) -> Response:
        """
        Delete a Category by its ID.

        Args:
            id_ (int): The ID of the Category.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            category_id = category_service.delete_category(id_)
            return make_response({'id': category_id}, 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class CategoryListResource(Resource):
    """
    Resource for getting all Categories.
    """

    def get(self) -> Response:
        """
        Get all Categories.

        Returns:
            Response: Flask response object.
        """
        categories = category_service.get_all_categories()
        return make_response(
            [category.to_dict() for category in categories],
            200
        )


class ArticleResource(Resource):
    """
    Resource for creating a new Article.

    Attributes:
        parser (RequestParser): Parser for the request data.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str, nullable=False)
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('tags_id', type=int, action='append', nullable=False)

    def post(self) -> Response:
        """
        Create a new Article.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            data = ArticleResource.parser.parse_args()
            dto = ArticleCreateDTO.from_dict(data)
            article = article_service.create_article(dto)
            return make_response(article.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class ArticleIdResource(Resource):
    """
    Resource for getting, updating, and deleting an Article by its ID.

    Attributes:
        parser (RequestParser): Parser for the request data.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str, nullable=False)
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('tags_id', type=int, action='append', nullable=True)

    def get(self, id_: int) -> Response:
        """
        Get an Article by its ID.

        Args:
            id_ (int): The ID of the Article.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            article = article_service.get_article_by_id(id_)
            return make_response(article.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def put(self, id_: int) -> Response:
        """
        Update an Article by its ID.

        Args:
            id_ (int): The ID of the Article.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            data = ArticleResource.parser.parse_args() | {'id': id_}
            dto = ArticleUpdateDTO.from_dict(data)
            article = article_service.update_article(dto)
            return make_response(article.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def delete(self, id_: int) -> Response:
        """
        Delete an Article by its ID.

        Args:
            id_ (int): The ID of the Article.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            article_id = article_service.delete_article(id_)
            return make_response({'id': article_id}, 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class ArticlesWithCategoryResource(Resource):
    """
    Resource for getting all Articles with a specific Category.

    Attributes:
        parser (RequestParser): Parser for the request data.
    """

    def get(self, category_id: str) -> Response:
        """
        Get all Articles with a specific Category.

        Args:
            category_id (str): The ID of the Category.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            articles = article_service.get_articles_with_category(category_id)
            return make_response(
                [article.to_dict() for article in articles],
                200
            )
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class ArticleListResource(Resource):
    """
    Resource for getting all Articles.
    """

    def get(self) -> Response:
        """
        Get all Articles.

        Returns:
            Response: Flask response object.
        """
        articles = article_service.get_all_articles()
        return make_response([article.to_dict() for article in articles], 200)


class TranslationIdResource(Resource):
    """
    Resource for getting a Translation by its ID.
    """

    def get(self, id_: int) -> Response:
        """
        Get a Translation by its ID.

        Args:
            id_ (int): The ID of the Translation.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            translation = translation_service.get_translation_by_id(id_)
            return make_response(translation.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class ArticleTranslationResource(Resource):
    """
    Resource for requesting a Translation for an Article.

    Attributes:
        parser (RequestParser): Parser for the request data.
    """

    def post(self, article_id: int, language_id: int) -> Response:
        """
        Request a Translation for an Article.

        Args:
            article_id (int): The ID of the Article.
            language_id (int): The ID of the Language.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            translation = translation_service.request_translation(
                article_id, language_id)
            return make_response(translation.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class TagIdResource(Resource):
    """
    Resource for managing a Tag by its ID.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        """
        Get a Tag by its ID.

        Args:
            id_ (int): The ID of the Tag.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            tag = tag_service.get_tag_by_id(id_)
            return make_response(tag.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def put(self, id_: int) -> Response:
        """
        Update a Tag by its ID.

        Args:
            id_ (int): The ID of the Tag.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            data = TagIdResource.parser.parse_args() | {'id': id_}
            dto = TagUpdateDTO.from_dict(data)
            tag = tag_service.update_tag(dto)
            return make_response(tag.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def delete(self, id_: int) -> Response:
        """
        Delete a Tag by its ID.

        Args:
            id_ (int): The ID of the Tag.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            tag_id = tag_service.delete_tag(id_)
            return make_response({'id': tag_id}, 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class TagResource(Resource):
    """
    Resource for creating a Tag.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)

    def post(self) -> Response:
        """
        Create a Tag.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            data = TagResource.parser.parse_args()
            dto = TagCreateDTO.from_dict(data)
            tag = tag_service.create_tag(dto)
            return make_response(tag.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class TagListResource(Resource):
    """
    Resource for getting all Tags.
    """

    def get(self) -> Response:
        """
        Get all Tags.

        Returns:
            Response: Flask response object.
        """
        tags = tag_service.get_all_tags()
        return make_response([tag.to_dict() for tag in tags], 200)


class LanguageIdResource(Resource):
    """
    Resource for managing a Language by its ID.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('code', type=str, nullable=False)

    def get(self, id_: int) -> Response:
        """
        Get a Language by its ID.

        Args:
            id_ (int): The ID of the Language.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            language = language_service.get_language_by_id(id_)
            return make_response(language.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def put(self, id_: int) -> Response:
        """
        Update a Language by its ID.

        Args:
            id_ (int): The ID of the Language.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            data = LanguageIdResource.parser.parse_args() | {'id': id_}
            dto = LanguageUpdateDTO.from_dict(data)
            language = language_service.update_language(dto)
            return make_response(language.to_dict(), 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)

    def delete(self, id_: int) -> Response:
        """
        Delete a Language by its ID.

        Args:
            id_ (int): The ID of the Language.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            language_id = language_service.delete_language(id_)
            return make_response({'id': language_id}, 200)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class LanguageResource(Resource):
    """
    Resource for creating a Language.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('code', type=str, nullable=False)

    def post(self) -> Response:
        """
        Create a Language.

        Returns:
            Response: Flask response object.

        Raises:
            ApplicationError: If there is an application error.
        """
        try:
            data = LanguageResource.parser.parse_args()
            dto = LanguageCreateDTO.from_dict(data)
            language = language_service.create_language(dto)
            return make_response(language.to_dict(), 201)
        except ApplicationError as e:
            return make_response({'message': str(e)}, 400)


class LanguageListResource(Resource):
    """
    Resource for getting all Languages.
    """

    def get(self) -> Response:
        """
        Get all Languages.

        Returns:
            Response: Flask response object.
        """
        languages = language_service.get_all_languages()
        return make_response(
            [language.to_dict() for language in languages],
            200
        )
