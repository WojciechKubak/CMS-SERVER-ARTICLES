from articles.application.ports.input import (
    ArticleAPI,
    CategoryAPI,
    TagAPI,
    LanguageAPI,
    TranslationAPI,
    TranslationRequestUseCase,
)
from articles.infrastructure.api.errors import ApplicationError
from articles.infrastructure.api.dto import (
    LanguageDTO,
    LanguageCreateDTO,
    LanguageUpdateDTO,
    CategoryDTO,
    CategoryCreateDTO,
    CategoryUpdateDTO,
    ArticleDTO,
    ArticleListDTO,
    ArticleCreateDTO,
    ArticleUpdateDTO,
    TagDTO,
    TagCreateDTO,
    TagUpdateDTO,
    TranslationDTO,
)
from articles.domain.errors import DomainError
from dataclasses import dataclass
from typing import Union


@dataclass
class CategoryApiService:
    """
    API service for Category operations.

    Attributes:
        category_service (CategoryAPI): The category service instance.
    """

    category_service: CategoryAPI

    def create_category(self, category_create_dto: CategoryCreateDTO) -> CategoryDTO:
        """
        Create a new category.

        Args:
            category_create_dto (CategoryCreateDTO): The category creation
            data.

        Returns:
            CategoryDTO: The created category.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.category_service.create_category(
                category_create_dto.to_domain()
            )
            return CategoryDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def update_category(self, category_update_dto: CategoryUpdateDTO) -> CategoryDTO:
        """
        Update an existing category.

        Args:
            category_update_dto (CategoryUpdateDTO): The category update data.

        Returns:
            CategoryDTO: The updated category.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.category_service.update_category(
                category_update_dto.to_domain()
            )
            return CategoryDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def delete_category(self, id_: int) -> int:
        """
        Delete a category by its ID.

        Args:
            id_ (int): The ID of the category.

        Returns:
            int: The ID of the deleted category.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            return self.category_service.delete_category(id_)
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_category_by_id(self, id_: int) -> CategoryDTO:
        """
        Get a category by its ID.

        Args:
            id_ (int): The ID of the category.

        Returns:
            CategoryDTO: The requested category.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.category_service.get_category_by_id(id_)
            return CategoryDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_all_categories(self) -> list[CategoryDTO]:
        """
        Get all categories.

        Returns:
            list[CategoryDTO]: The list of all categories.
        """
        categories = self.category_service.get_all_categories()
        return [CategoryDTO.from_domain(category) for category in categories]


@dataclass
class ArticleApiService:
    """
    API service for Article operations.

    Attributes:
        article_service (ArticleAPI): The article service instance.
    """

    article_service: ArticleAPI

    def create_article(self, article_create_dto: ArticleCreateDTO) -> ArticleDTO:
        """
        Create a new article.

        Args:
            article_create_dto (ArticleCreateDTO): The article creation data.

        Returns:
            ArticleDTO: The created article.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.article_service.create_article(article_create_dto.to_domain())
            return ArticleDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def update_article(self, article_update_dto: ArticleUpdateDTO) -> ArticleDTO:
        """
        Update an existing article.

        Args:
            article_update_dto (ArticleUpdateDTO): The article update data.

        Returns:
            ArticleDTO: The updated article.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.article_service.update_article(article_update_dto.to_domain())
            return ArticleDTO.from_dto(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def delete_article(self, id_: int) -> int:
        """
        Delete an article by its ID.

        Args:
            id_ (int): The ID of the article.

        Returns:
            int: The ID of the deleted article.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            return self.article_service.delete_article(id_)
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_article_by_id(self, id_: int) -> ArticleDTO:
        """
        Get an article by its ID.

        Args:
            id_ (int): The ID of the article.

        Returns:
            ArticleDTO: The requested article.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.article_service.get_article_by_id(id_)
            return ArticleDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_articles_with_category(self, category_id: int) -> list[ArticleListDTO]:
        """
        Get articles with a specific category.

        Args:
            category_id (int): The ID of the category.

        Returns:
            list[ArticleListDTO]: The list of articles with the specified
            category.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            articles = self.article_service.get_articles_with_category(category_id)
            return [ArticleListDTO.from_domain(article) for article in articles]
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_all_articles(self) -> list[ArticleListDTO]:
        """
        Get all articles.

        Returns:
            list[ArticleListDTO]: The list of all articles.
        """
        result = self.article_service.get_all_articles()
        return [ArticleListDTO.from_domain(article) for article in result]


@dataclass
class TagApiService:
    """
    API service for Tag operations.

    Attributes:
        tag_service (TagAPI): The tag service instance.
    """

    tag_service: TagAPI

    def create_tag(self, tag_create_dto: TagCreateDTO) -> TagDTO:
        """
        Create a new tag.

        Args:
            tag_create_dto (TagCreateDTO): The tag creation data.

        Returns:
            TagDTO: The created tag.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.tag_service.create_tag(tag_create_dto.to_domain())
            return TagDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def update_tag(self, tag_update_dto: TagUpdateDTO) -> TagDTO:
        """
        Update an existing tag.

        Args:
            tag_update_dto (TagUpdateDTO): The tag update data.

        Returns:
            TagDTO: The updated tag.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.tag_service.update_tag(tag_update_dto.to_domain())
            return TagDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def delete_tag(self, id_: int) -> int:
        """
        Delete a tag by its ID.

        Args:
            id_ (int): The ID of the tag.

        Returns:
            int: The ID of the deleted tag.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            self.tag_service.delete_tag(id_)
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_tag_by_id(self, id_: int) -> TagDTO:
        """
        Get a tag by its ID.

        Args:
            id_ (int): The ID of the tag.

        Returns:
            TagDTO: The requested tag.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.tag_service.get_tag_by_id(id_)
            return TagDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_all_tags(self) -> list[TagDTO]:
        """
        Get all tags.

        Returns:
            list[TagDTO]: The list of all tags.
        """
        tags = self.tag_service.get_all_tags()
        return [TagDTO.from_domain(tag) for tag in tags]


@dataclass
class LanguageApiService:
    """
    API service for Language operations.

    Attributes:
        language_service (LanguageAPI): The language service instance.
    """

    language_service: LanguageAPI

    def create_language(self, language_create_dto: LanguageCreateDTO) -> LanguageDTO:
        """
        Create a new language.

        Args:
            language_create_dto (LanguageCreateDTO): The language creation
            data.

        Returns:
            LanguageDTO: The created language.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.language_service.create_language(
                language_create_dto.to_domain()
            )
            return LanguageDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def update_language(self, language_update_dto: LanguageUpdateDTO) -> LanguageDTO:
        """
        Update an existing language.

        Args:
            language_update_dto (LanguageUpdateDTO): The language update data.

        Returns:
            LanguageDTO: The updated language.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.language_service.update_language(
                language_update_dto.to_domain()
            )
            return LanguageDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def delete_language(self, id_: int) -> int:
        """
        Delete a language by its ID.

        Args:
            id_ (int): The ID of the language.

        Returns:
            int: The ID of the deleted language.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            return self.language_service.delete_language(id_)
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_language_by_id(self, id_: int) -> LanguageDTO:
        """
        Get a language by its ID.

        Args:
            id_ (int): The ID of the language.

        Returns:
            LanguageDTO: The requested language.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.language_service.get_language_by_id(id_)
            return LanguageDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def get_all_languages(self) -> list[LanguageDTO]:
        """
        Get all languages.

        Returns:
            list[LanguageDTO]: The list of all languages.
        """
        languages = self.language_service.get_all_languages()
        return [LanguageDTO.from_domain(language) for language in languages]


@dataclass
class TranslationApiService:
    """
    API service for Translation operations.

    Attributes:
        translation_service (Union[TranslationAPI, TranslationRequestUseCase]):
        The translation service instance.
    """

    translation_service: Union[TranslationAPI, TranslationRequestUseCase]

    def get_translation_by_id(self, id_: int) -> TranslationDTO:
        """
        Get a translation by its ID.

        Args:
            id_ (int): The ID of the translation.

        Returns:
            TranslationDTO: The requested translation.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.translation_service.get_translation_by_id(id_)
            return TranslationDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))

    def request_translation(self, article_id: int, language_id: int) -> TranslationDTO:
        """
        Request a translation for an article in a specific language.

        Args:
            article_id (int): The ID of the article.
            language_id (int): The ID of the language.

        Returns:
            TranslationDTO: The requested translation.

        Raises:
            ApplicationError: If there is a domain error.
        """
        try:
            result = self.translation_service.request_translation(
                article_id, language_id
            )
            return TranslationDTO.from_domain(result)
        except DomainError as e:
            raise ApplicationError(str(e))
