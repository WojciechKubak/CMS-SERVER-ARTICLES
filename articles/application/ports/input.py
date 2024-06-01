from articles.domain.model import Category, Article, Tag, Translation, Language
from articles.domain.event import ArticleTranslatedEvent
from abc import ABC, abstractmethod


class CategoryAPI(ABC):
    """
    Abstract base class for CategoryAPI. This class outlines
    the methods that any class inheriting from it should implement.
    """

    @abstractmethod
    def create_category(self, category: Category) -> Category:
        """
        Abstract method to create a category.

        Args:
            category (Category): The category to be created.

        Returns:
            Category: The created category.
        """
        pass

    @abstractmethod
    def update_category(self, category: Category) -> Category:
        """
        Abstract method to update a category.

        Args:
            category (Category): The category to be updated.

        Returns:
            Category: The updated category.
        """
        pass

    @abstractmethod
    def delete_category(self, id_: int) -> int:
        """
        Abstract method to delete a category.

        Args:
            id_ (int): The id of the category to be deleted.

        Returns:
            int: The id of the deleted category.
        """
        pass

    @abstractmethod
    def get_category_by_id(self, id_: int) -> Category:
        """
        Abstract method to get a category by id.

        Args:
            id_ (int): The id of the category to be fetched.

        Returns:
            Category: The fetched category.
        """
        pass

    @abstractmethod
    def get_all_categories(self) -> list[Category]:
        """
        Abstract method to get all categories.

        Returns:
            list[Category]: A list of all categories.
        """
        pass


class ArticleAPI(ABC):
    """
    Abstract base class for ArticleAPI. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def create_article(self, article: Article) -> Article:
        """
        Abstract method to create an article.

        Args:
            article (Article): The article to be created.

        Returns:
            Article: The created article.
        """
        pass

    @abstractmethod
    def update_article(self, article: Article) -> Article:
        """
        Abstract method to update an article.

        Args:
            article (Article): The article to be updated.

        Returns:
            Article: The updated article.
        """
        pass

    @abstractmethod
    def delete_article(self, id_: int) -> int:
        """
        Abstract method to delete an article.

        Args:
            id_ (int): The id of the article to be deleted.

        Returns:
            int: The id of the deleted article.
        """
        pass

    @abstractmethod
    def get_article_by_id(self, id_: int) -> Article:
        """
        Abstract method to get an article by id.

        Args:
            id_ (int): The id of the article to be fetched.

        Returns:
            Article: The fetched article.
        """
        pass

    @abstractmethod
    def get_articles_with_category(self, category_id: int) -> list[Article]:
        """
        Abstract method to get articles with a specific category.

        Args:
            category_id (int): The id of the category.

        Returns:
            list[Article]: A list of articles with the specified category.
        """
        pass

    @abstractmethod
    def get_all_articles(self) -> list[Article]:
        """
        Abstract method to get all articles.

        Returns:
            list[Article]: A list of all articles.
        """
        pass


class TagAPI(ABC):
    """
    Abstract base class for TagAPI. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def create_tag(self, tag: Tag) -> Tag:
        """
        Abstract method to create a tag.

        Args:
            tag (Tag): The tag to be created.

        Returns:
            Tag: The created tag.
        """
        pass

    @abstractmethod
    def update_tag(self, tag: Tag) -> Tag:
        """
        Abstract method to update a tag.

        Args:
            tag (Tag): The tag to be updated.

        Returns:
            Tag: The updated tag.
        """
        pass

    @abstractmethod
    def delete_tag(self, id_: int) -> int:
        """
        Abstract method to delete a tag.

        Args:
            id_ (int): The id of the tag to be deleted.

        Returns:
            int: The id of the deleted tag.
        """
        pass

    @abstractmethod
    def get_tag_by_id(self, id_: int) -> Tag:
        """
        Abstract method to get a tag by id.

        Args:
            id_ (int): The id of the tag to be fetched.

        Returns:
            Tag: The fetched tag.
        """
        pass

    @abstractmethod
    def get_all_tags(self) -> list[Tag]:
        """
        Abstract method to get all tags.

        Returns:
            list[Tag]: A list of all tags.
        """
        pass


class TranslationAPI(ABC):
    """
    Abstract base class for TranslationAPI. This class outlines the methods
    that any class inheriting from it should implement.
    """

    @abstractmethod
    def get_translation_by_id(self, id_: int) -> Translation:
        """
        Abstract method to get a translation by id.

        Args:
            id_ (int): The id of the translation to be fetched.

        Returns:
            Translation: The fetched translation.
        """
        pass


class LanguageAPI(ABC):
    """
    Abstract base class for LanguageAPI. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def create_language(self, language: Language) -> Language:
        """
        Abstract method to create a language.

        Args:
            language (Language): The language to be created.

        Returns:
            Language: The created language.
        """
        pass

    @abstractmethod
    def update_language(self, language: Language) -> Language:
        """
        Abstract method to update a language.

        Args:
            language (Language): The language to be updated.

        Returns:
            Language: The updated language.
        """
        pass

    @abstractmethod
    def delete_language(self, id_: int) -> int:
        """
        Abstract method to delete a language.

        Args:
            id_ (int): The id of the language to be deleted.

        Returns:
            int: The id of the deleted language.
        """
        pass

    @abstractmethod
    def get_language_by_id(self, id_: int) -> Language:
        """
        Abstract method to get a language by id.

        Args:
            id_ (int): The id of the language to be fetched.

        Returns:
            Language: The fetched language.
        """
        pass

    @abstractmethod
    def get_all_languages(self) -> list[Language]:
        """
        Abstract method to get all languages.

        Returns:
            list[Language]: A list of all languages.
        """
        pass


class TranslationRequestUseCase(ABC):
    """
    Abstract base class for TranslationRequestUseCase. This class outlines the
    methods that any class inheriting from it should implement.
    """

    @abstractmethod
    def request_translation(
        self,
        article_id: int,
        language_id: int
    ) -> Translation:
        """
        Abstract method to request a translation.

        Args:
            article_id (int): The id of the article to be translated.
            language_id (int): The id of the language to translate to.

        Returns:
            Translation: The requested translation.
        """
        pass


class TranslationConsumer(ABC):
    """
    Abstract base class for TranslationConsumer. This class outlines the
    methods that any class inheriting from it should implement.
    """

    @abstractmethod
    def handle_translation_event(
        self,
        event: ArticleTranslatedEvent
    ) -> Translation:
        """
        Abstract method to handle a translation event.

        Args:
            event (ArticleTranslatedEvent): The translation event to handle.

        Returns:
            Translation: The handled translation.
        """
        pass
