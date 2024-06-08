from articles.application.ports.input import (
    CategoryAPI,
    ArticleAPI,
    TagAPI,
    TranslationAPI,
    LanguageAPI,
    TranslationRequestUseCase,
    TranslationConsumer,
)
from articles.application.ports.output import (
    CategoryDB,
    ArticleDB,
    TagDB,
    TranslationDB,
    LanguageDB,
    FileStorage,
    ArticleEventPublisher,
    LanguageEventPublisher,
)
from articles.domain.event import (
    TranslationRequestEvent,
    ArticleTranslatedEvent,
    LanguageEvent,
    LanguageEventType,
)
from articles.domain.errors import (
    CategoryNameExistsError,
    ArticleTitleExistsError,
    CategoryNotFoundError,
    TagNotFoundError,
    ArticleNotFoundError,
    TagNameExistsError,
    TranslationNotFoundError,
    LanguageNotFoundError,
    LanguageNameExistsError,
    TranslationExistsError,
    TranslationPublishedError,
)
from articles.domain.model import Category, Article, Tag, Translation, Language
from dataclasses import dataclass


@dataclass
class CategoryService(CategoryAPI):
    """
    Service class for Category operations.

    Attributes:
        category_db (CategoryDB): The database interface for Category
        operations.
    """

    category_db: CategoryDB

    def create_category(self, category: Category) -> Category:
        """
        Method to create a new category.

        Args:
            category (Category): The category to be created.

        Returns:
            Category: The created category.

        Raises:
            CategoryNameExistsError: If a category with the same name already
            exists.
        """
        if self.category_db.get_category_by_name(category.name):
            raise CategoryNameExistsError()

        added_category = self.category_db.save_category(category)

        return added_category

    def update_category(self, category: Category) -> Category:
        """
        Method to update an existing category.

        Args:
            category (Category): The category to be updated.

        Returns:
            Category: The updated category.

        Raises:
            CategoryNotFoundError: If the category to be updated does
            not exist.
            CategoryNameExistsError: If a category with the same name
            already exists.
        """
        if not self.category_db.get_category_by_id(category.id_):
            raise CategoryNotFoundError()
        result = self.category_db.get_category_by_name(category.name)
        if result and result.id_ != category.id_:
            raise CategoryNameExistsError()

        updated_category = self.category_db.update_category(category)

        return updated_category

    def delete_category(self, id_: int) -> int:
        """
        Method to delete a category.

        Args:
            id_ (int): The ID of the category to be deleted.

        Returns:
            int: The ID of the deleted category.

        Raises:
            CategoryNotFoundError: If the category to be deleted does not
            exist.
        """
        if not self.category_db.get_category_by_id(id_):
            raise CategoryNotFoundError()
        self.category_db.delete_category(id_)
        return id_

    def get_category_by_id(self, id_: int) -> Category:
        """
        Method to get a category by its ID.

        Args:
            id_ (int): The ID of the category.

        Returns:
            Category: The category with the given ID.

        Raises:
            CategoryNotFoundError: If no category with the given ID exists.
        """
        result = self.category_db.get_category_by_id(id_)
        if not result:
            raise CategoryNotFoundError()
        return result

    def get_all_categories(self) -> list[Category]:
        """
        Method to get all categories.

        Returns:
            list[Category]: A list of all categories.
        """
        return self.category_db.get_all_categories()


@dataclass
class ArticleService(ArticleAPI):
    """
    Service class for Article operations.

    Attributes:
        article_db (ArticleDB): The database interface for Article operations.
        category_db (CategoryDB): The database interface for Category
        operations.
        tag_db (TagDB): The database interface for Tag operations.
        file_storage (FileStorage): The storage interface for file operations.
    """

    article_db: ArticleDB
    category_db: CategoryDB
    tag_db: TagDB
    file_storage: FileStorage

    def create_article(self, article: Article) -> Article:
        """
        Create a new article.

        Args:
            article (Article): The article to be created.

        Returns:
            Article: The created article.

        Raises:
            ArticleTitleExistsError: If an article with the same title exists.
            CategoryNotFoundError: If the category does not exist.
            TagNotFoundError: If any of the tags do not exist.
        """
        if self.article_db.get_article_by_title(article.title):
            raise ArticleTitleExistsError()
        category = self.category_db.get_category_by_id(article.category)
        if not category:
            raise CategoryNotFoundError()
        tags = self.tag_db.get_tags_by_id(article.tags)
        if len(tags) != len(article.tags):
            raise TagNotFoundError()

        content_path = self.file_storage.upload_content(article.content)
        article_to_add = article.change_category_and_tags(
            category, tags
        ).change_content(content_path)
        added_article = self.article_db.save_article(article_to_add).change_content(
            article.content
        )

        return added_article

    def update_article(self, article: Article) -> Article:
        """
        Update an existing article.

        Args:
            article (Article): The article to be updated.

        Returns:
            Article: The updated article.

        Raises:
            ArticleNotFoundError: If the article does not exist.
            ArticleTitleExistsError: If an article with the same title exists.
            CategoryNotFoundError: If the category does not exist.
            TagNotFoundError: If any of the tags do not exist.
        """
        article_by_id = self.article_db.get_article_by_id(article.id_)
        if not article_by_id:
            raise ArticleNotFoundError()
        article_by_title = self.article_db.get_article_by_title(article.title)
        if article_by_title and article_by_title.id_ != article.id_:
            raise ArticleTitleExistsError()
        category_by_id = self.category_db.get_category_by_id(article.category)
        if not category_by_id:
            raise CategoryNotFoundError()
        tags_by_id = self.tag_db.get_tags_by_id(article.tags)
        if len(tags_by_id) != len(article.tags):
            raise TagNotFoundError()

        article_to_update = article.change_category_and_tags(category_by_id, tags_by_id)
        self.file_storage.update_content(article_by_id.content, article.content)
        updated_article = self.article_db.update_article(article_to_update)

        return updated_article

    def delete_article(self, id_: int) -> int:
        """
        Delete an article.

        Args:
            id_ (int): The ID of the article to be deleted.

        Returns:
            int: The ID of the deleted article.

        Raises:
            ArticleNotFoundError: If the article does not exist.
        """
        article_by_id = self.article_db.get_article_by_id(id_)
        if not article_by_id:
            raise ArticleNotFoundError()

        self.file_storage.delete_content(article_by_id.content)
        self.article_db.delete_article(id_)

        return id_

    def get_article_by_id(self, id_: int) -> Article:
        """
        Get an article by its ID.

        Args:
            id_ (int): The ID of the article.

        Returns:
            Article: The article with the given ID.

        Raises:
            ArticleNotFoundError: If the article does not exist.
        """
        if not (article := self.article_db.get_article_by_id(id_)):
            raise ArticleNotFoundError()
        content = self.file_storage.read_content(article.content)
        return article.change_content(content)

    def get_articles_with_category(self, category_id: int) -> list[Article]:
        """
        Get all articles with a specific category.

        Args:
            category_id (int): The ID of the category.

        Returns:
            list[Article]: A list of articles with the given category.

        Raises:
            CategoryNotFoundError: If the category does not exist.
        """
        if not self.category_db.get_category_by_id(category_id):
            raise CategoryNotFoundError()
        articles = self.article_db.get_articles_with_category(category_id)
        return [
            article.change_content(self.file_storage.read_content(article.content))
            for article in articles
        ]

    def get_all_articles(self) -> list[Article]:
        """
        Get all articles.

        Returns:
            list[Article]: A list of all articles.
        """
        return [
            article.change_content(self.file_storage.read_content(article.content))
            for article in self.article_db.get_all_articles()
        ]


@dataclass
class TagService(TagAPI):
    """
    Service class for Tag operations.

    Attributes:
        tag_db (TagDB): The database interface for Tag operations.
    """

    tag_db: TagDB

    def create_tag(self, tag: Tag) -> Tag:
        """
        Create a new tag.

        Args:
            tag (Tag): The tag to be created.

        Returns:
            Tag: The created tag.

        Raises:
            TagNameExistsError: If a tag with the same name already exists.
        """
        if self.tag_db.get_tag_by_name(tag.name):
            raise TagNameExistsError()
        added_tag = self.tag_db.save_tag(tag)
        return added_tag

    def update_tag(self, tag: Tag) -> Tag:
        """
        Update an existing tag.

        Args:
            tag (Tag): The tag to be updated.

        Returns:
            Tag: The updated tag.

        Raises:
            TagNotFoundError: If the tag to be updated does not exist.
            TagNameExistsError: If a tag with the same name already exists.
        """
        if not self.tag_db.get_tag_by_id(tag.id_):
            raise TagNotFoundError()
        result = self.tag_db.get_tag_by_name(tag.name)
        if result and result.id_ != tag.id_:
            raise TagNameExistsError()

        updated_tag = self.tag_db.update_tag(tag)

        return updated_tag

    def delete_tag(self, id_: int) -> int:
        """
        Delete a tag.

        Args:
            id_ (int): The ID of the tag to be deleted.

        Returns:
            int: The ID of the deleted tag.

        Raises:
            TagNotFoundError: If the tag to be deleted does not exist.
        """
        if not self.tag_db.get_tag_by_id(id_):
            raise TagNotFoundError()
        self.tag_db.delete_tag(id_)
        return id_

    def get_tag_by_id(self, id_: int) -> Tag:
        """
        Get a tag by its ID.

        Args:
            id_ (int): The ID of the tag.

        Returns:
            Tag: The tag with the given ID.

        Raises:
            TagNotFoundError: If no tag with the given ID exists.
        """
        if not (tag := self.tag_db.get_tag_by_id(id_)):
            raise TagNotFoundError()
        return tag

    def get_all_tags(self) -> list[Tag]:
        """
        Get all tags.

        Returns:
            list[Tag]: A list of all tags.
        """
        return self.tag_db.get_all_tags()


@dataclass
class TranslationService(
    TranslationAPI, TranslationRequestUseCase, TranslationConsumer
):
    """
    Service class for Translation operations.

    Attributes:
        article_db (ArticleDB): The database interface for Article.
        language_db (LanguageDB): The database interface for Language.
        translation_db (TranslationDB): The database interface for Translation.
        file_storage (FileStorage): The storage interface for file operations.
        article_event_publisher (ArticleEventPublisher): The event publisher.
    """

    article_db: ArticleDB
    language_db: LanguageDB
    translation_db: TranslationDB
    file_storage: FileStorage
    article_event_publisher: ArticleEventPublisher

    def get_translation_by_id(self, id_: int) -> Translation:
        """
        Get a translation by its ID.

        Args:
            id_ (int): The ID of the translation.

        Returns:
            Translation: The translation with the given ID.

        Raises:
            TranslationNotFoundError: If the translation does not exist.
        """
        translation = self.translation_db.get_translation_by_id(id_)
        if not translation:
            raise TranslationNotFoundError()

        content = self.file_storage.read_content(translation.content)
        translation.content = content

        return translation

    def request_translation(self, article_id: int, language_id: str) -> Translation:
        """
        Request a translation for an article in a specific language.

        Args:
            article_id (int): The ID of the article.
            language_id (str): The ID of the language.

        Returns:
            Translation: The requested translation.

        Raises:
            LanguageNotFoundError: If the language does not exist.
            ArticleNotFoundError: If the article does not exist.
            TranslationExistsError: If a translation for the article in the
            specified language already exists.
        """
        language = self.language_db.get_language_by_id(language_id)
        if not language:
            raise LanguageNotFoundError()
        article = self.article_db.get_article_by_id(article_id)
        if not article:
            raise ArticleNotFoundError()
        if self.translation_db.get_translation_by_article_and_language(
            article_id, language_id
        ):
            raise TranslationExistsError()

        translation_to_add = Translation.create_request(language, article)
        added_translation = self.translation_db.save_translation(translation_to_add)
        event = TranslationRequestEvent.create(article, language)
        self.article_event_publisher.publish_event(event)

        return added_translation

    def handle_translation_event(self, event: ArticleTranslatedEvent) -> Translation:
        """
        Handle an event of an article being translated.

        Args:
            event (ArticleTranslatedEvent): The event of an article being
            translated.

        Returns:
            Translation: The updated translation.

        Raises:
            ArticleNotFoundError: If the article does not exist.
            LanguageNotFoundError: If the language does not exist.
            TranslationNotFoundError: If the translation does not exist.
            TranslationPublishedError: If the translation is already published.
        """
        if not self.article_db.get_article_by_id(event.article_id):
            raise ArticleNotFoundError()
        if not self.language_db.get_language_by_id(event.language_id):
            raise LanguageNotFoundError()
        translation = self.translation_db.get_translation_by_article_and_language(
            event.article_id, event.language_id
        )
        if not translation:
            raise TranslationNotFoundError()
        if translation.is_ready:
            raise TranslationPublishedError()

        translation = translation.publish(event.content_path)
        updated_translation = self.translation_db.update_translation(translation)

        return updated_translation


@dataclass
class LanguageService(LanguageAPI):
    """
    Service class for Language operations.

    Attributes:
        language_db (LanguageDB): The database interface for Language.
        language_event_publisher (LanguageEventPublisher): The event publisher
        for Language events.
    """

    language_db: LanguageDB
    language_event_publisher: LanguageEventPublisher

    def create_language(self, language: Language) -> Language:
        """
        Create a new language.

        Args:
            language (Language): The language to be created.

        Returns:
            Language: The created language.

        Raises:
            LanguageNameExistsError: If a language with the same name already
            exists.
        """
        if self.language_db.get_language_by_name(language.name):
            raise LanguageNameExistsError()

        added_language = self.language_db.save_language(language)
        language_event = LanguageEvent.create(added_language, LanguageEventType.CREATE)
        self.language_event_publisher.publish_event(language_event)

        return added_language

    def update_language(self, language: Language) -> Language:
        """
        Update an existing language.

        Args:
            language (Language): The language to be updated.

        Returns:
            Language: The updated language.

        Raises:
            LanguageNotFoundError: If the language to be updated does
            not exist.
            LanguageNameExistsError: If a language with the same name
            already exists.
        """
        if not self.language_db.get_language_by_id(language.id_):
            raise LanguageNotFoundError()

        result = self.language_db.get_language_by_name(language.name)
        if result and result.id_ != language.id_:
            raise LanguageNameExistsError()

        updated_language = self.language_db.update_language(language)
        language_event = LanguageEvent.create(
            updated_language, LanguageEventType.UPDATE
        )
        self.language_event_publisher.publish_event(language_event)

        return updated_language

    def delete_language(self, id_: str) -> None:
        """
        Delete a language.

        Args:
            id_ (str): The ID of the language to be deleted.

        Raises:
            LanguageNotFoundError: If the language to be deleted does
            not exist.
        """
        if not self.language_db.get_language_by_id(id_):
            raise LanguageNotFoundError()

        language_to_delete = self.language_db.get_language_by_id(id_)
        language_event = LanguageEvent.create(
            language_to_delete, LanguageEventType.DELETE
        )
        self.language_event_publisher.publish_event(language_event)

        self.language_db.delete_language(id_)

    def get_language_by_id(self, id_: str) -> Language:
        """
        Get a language by its ID.

        Args:
            id_ (str): The ID of the language.

        Returns:
            Language: The language with the given ID.

        Raises:
            LanguageNotFoundError: If no language with the given ID exists.
        """
        if not (language := self.language_db.get_language_by_id(id_)):
            raise LanguageNotFoundError()
        return language

    def get_all_languages(self) -> list[Language]:
        """
        Get all languages.

        Returns:
            list[Language]: A list of all languages.
        """
        return self.language_db.get_all_languages()
