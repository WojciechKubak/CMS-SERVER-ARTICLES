from articles.domain.model import Category, Article, Tag, Translation, Language
from articles.domain.event import TranslationRequestEvent, LanguageEvent
from abc import ABC, abstractmethod


class CategoryDB(ABC):
    """
    Abstract base class for CategoryDB. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def save_category(self, category: Category) -> Category:
        """
        Abstract method to save a category.

        Args:
            category (Category): The category to be saved.

        Returns:
            Category: The saved category.
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
    def get_category_by_id(self, id_: int) -> Category | None:
        """
        Abstract method to get a category by id.

        Args:
            id_ (int): The id of the category to be fetched.

        Returns:
            Category | None: The fetched category if found, else None.
        """
        pass

    @abstractmethod
    def get_category_by_name(self, name: str) -> Category | None:
        """
        Abstract method to get a category by name.

        Args:
            name (str): The name of the category to be fetched.

        Returns:
            Category | None: The fetched category if found, else None.
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


class ArticleDB(ABC):
    """
    Abstract base class for ArticleDB. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def save_article(self, article: Article) -> Article:
        """
        Abstract method to save an article.

        Args:
            article (Article): The article to be saved.

        Returns:
            Article: The saved article.
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
    def get_article_by_id(self, id_: int) -> Article | None:
        """
        Abstract method to get an article by id.

        Args:
            id_ (int): The id of the article to be fetched.

        Returns:
            Article | None: The fetched article if found, else None.
        """
        pass

    @abstractmethod
    def get_article_by_title(self, title: str) -> Article | None:
        """
        Abstract method to get an article by title.

        Args:
            title (str): The title of the article to be fetched.

        Returns:
            Article | None: The fetched article if found, else None.
        """
        pass

    @abstractmethod
    def get_articles_with_category(self, category_id: int) -> list[Article]:
        """
        Abstract method to get articles with a specific category.

        Args:
            category_id (int): The id of the category to filter articles by.

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


class TagDB(ABC):
    """
    Abstract base class for TagDB. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def save_tag(self, tag: Tag) -> Tag:
        """
        Abstract method to save a tag.

        Args:
            tag (Tag): The tag to be saved.

        Returns:
            Tag: The saved tag.
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
    def get_tag_by_id(self, id_: int) -> Tag | None:
        """
        Abstract method to get a tag by id.

        Args:
            id_ (int): The id of the tag to be fetched.

        Returns:
            Tag | None: The fetched tag if found, else None.
        """
        pass

    @abstractmethod
    def get_tag_by_name(self, name: str) -> Tag | None:
        """
        Abstract method to get a tag by name.

        Args:
            name (str): The name of the tag to be fetched.

        Returns:
            Tag | None: The fetched tag if found, else None.
        """
        pass

    @abstractmethod
    def get_tags_by_id(self, ids: list[int]) -> list[Tag]:
        """
        Abstract method to get tags by their ids.

        Args:
            ids (list[int]): The ids of the tags to be fetched.

        Returns:
            list[Tag]: A list of fetched tags.
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


class TranslationDB(ABC):
    """
    Abstract base class for TranslationDB. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def save_translation(self, translation: Translation) -> Translation:
        """
        Abstract method to save a translation.

        Args:
            translation (Translation): The translation to be saved.

        Returns:
            Translation: The saved translation.
        """
        pass

    @abstractmethod
    def update_translation(self, translation: Translation) -> Translation:
        """
        Abstract method to update a translation.

        Args:
            translation (Translation): The translation to be updated.

        Returns:
            Translation: The updated translation.
        """
        pass

    @abstractmethod
    def get_translation_by_id(self, id_: int) -> Translation | None:
        """
        Abstract method to get a translation by id.

        Args:
            id_ (int): The id of the translation to be fetched.

        Returns:
            Translation | None: The fetched translation if found, else None.
        """
        pass

    @abstractmethod
    def get_translation_by_article_and_language(
        self,
        article_id: int,
        language_id: int
    ) -> Translation | None:
        """
        Abstract method to get a translation by article id and language id.

        Args:
            article_id (int): The id of the article of the
            translation to be fetched.
            language_id (int): The id of the language of the
            translation to be fetched.

        Returns:
            Translation | None: The fetched translation if found, else None.
        """
        pass


class LanguageDB(ABC):
    """
    Abstract base class for LanguageDB. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def save_language(self, language: Language) -> Language:
        """
        Abstract method to save a language.

        Args:
            language (Language): The language to be saved.

        Returns:
            Language: The saved language.
        """
        pass

    @abstractmethod
    def get_language_by_id(self, id_: int) -> Language | None:
        """
        Abstract method to get a language by id.

        Args:
            id_ (int): The id of the language to be fetched.

        Returns:
            Language | None: The fetched language if found, else None.
        """
        pass

    @abstractmethod
    def get_language_by_name(self, name: str) -> Language | None:
        """
        Abstract method to get a language by name.

        Args:
            name (str): The name of the language to be fetched.

        Returns:
            Language | None: The fetched language if found, else None.
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
    def get_all_languages(self) -> list[Language]:
        """
        Abstract method to get all languages.

        Returns:
            list[Language]: A list of all languages.
        """
        pass


class FileStorage(ABC):
    """
    Abstract base class for FileStorage. This class outlines the methods that
    any class inheriting from it should implement.
    """

    @abstractmethod
    def upload_content(self, content: str) -> str:
        """
        Abstract method to upload content.

        Args:
            content (str): The content to be uploaded.

        Returns:
            str: The path where the content was uploaded.
        """
        pass

    @abstractmethod
    def read_content(self, path: str) -> str:
        """
        Abstract method to read content from a path.

        Args:
            path (str): The path from where to read the content.

        Returns:
            str: The content read from the path.
        """
        pass

    @abstractmethod
    def update_content(self, path: str, new_content: str) -> None:
        """
        Abstract method to update content at a path.

        Args:
            path (str): The path where the content is to be updated.
            new_content (str): The new content to be uploaded.

        Returns:
            None
        """
        pass

    @abstractmethod
    def delete_content(self, path: str) -> None:
        """
        Abstract method to delete content at a path.

        Args:
            path (str): The path where the content is to be deleted.

        Returns:
            None
        """
        pass


class ArticleEventPublisher(ABC):
    """
    Abstract base class for ArticleEventPublisher. This class outlines the
    methods that any class inheriting from it should implement.
    """

    @abstractmethod
    def publish_event(self, event: TranslationRequestEvent) -> None:
        """
        Abstract method to publish a TranslationRequestEvent.

        Args:
            event (TranslationRequestEvent): The event to be published.

        Returns:
            None
        """
        pass


class LanguageEventPublisher(ABC):
    """
    Abstract base class for LanguageEventPublisher. This class outlines the
    methods that any class inheriting from it should implement.
    """

    @abstractmethod
    def publish_event(self, event: LanguageEvent) -> None:
        """
        Abstract method to publish a LanguageEvent.

        Args:
            event (LanguageEvent): The event to be published.

        Returns:
            None
        """
        pass
