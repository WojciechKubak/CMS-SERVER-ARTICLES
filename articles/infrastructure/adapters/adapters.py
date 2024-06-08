from articles.application.ports.output import (
    CategoryDB,
    ArticleDB,
    TagDB,
    LanguageDB,
    TranslationDB,
    FileStorage,
    ArticleEventPublisher,
    LanguageEventPublisher,
)
from articles.infrastructure.persistance.repository import (
    CategoryRepository,
    ArticleRepository,
    TagRepository,
    TranslationRepository,
    LanguageRepository,
)
from articles.infrastructure.persistance.entity import (
    CategoryEntity,
    ArticleEntity,
    TagEntity,
    TranslationEntity,
    LanguageEntity,
)
from articles.domain.model import (
    Category,
    Article,
    Tag,
    Translation,
    Language,
)
from articles.domain.event import TranslationRequestEvent, LanguageEvent
from articles.infrastructure.storage.boto3 import Boto3Service
from articles.infrastructure.broker.kafka import KafkaService
from articles.infrastructure.broker.dto import (
    TranslationRequestDTO,
    LanguageChangeEvent,
)
from dataclasses import dataclass


@dataclass
class CategoryDbAdapter(CategoryDB):
    """
    Adapter class for Category database operations.

    Attributes:
        category_repository (CategoryRepository): The repository for Category
        operations.
    """

    category_repository: CategoryRepository

    def save_category(self, category: Category) -> Category:
        """
        Save a new category.

        Args:
            category (Category): The category to be saved.

        Returns:
            Category: The saved category.
        """
        category_to_add = CategoryEntity.from_domain(category)
        category_entity = self.category_repository.add_or_update(category_to_add)
        return category_entity.to_domain()

    def update_category(self, category: Category) -> Category:
        """
        Update an existing category.

        Args:
            category (Category): The category to be updated.

        Returns:
            Category: The updated category.
        """
        category_to_update = CategoryEntity.from_domain(category)
        category_entity = self.category_repository.add_or_update(category_to_update)
        return category_entity.to_domain()

    def delete_category(self, id_: int) -> None:
        """
        Delete a category.

        Args:
            id_ (int): The ID of the category to be deleted.
        """
        self.category_repository.delete(id_)

    def get_category_by_id(self, id_: int) -> Category | None:
        """
        Get a category by its ID.

        Args:
            id_ (int): The ID of the category.

        Returns:
            Category | None: The category with the given ID, or None if
            no such category exists.
        """
        result = self.category_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_category_by_name(self, name: str) -> Category | None:
        """
        Get a category by its name.

        Args:
            name (str): The name of the category.

        Returns:
            Category | None: The category with the given name, or None if
            no such category exists.
        """
        result = self.category_repository.find_by_name(name)
        return result.to_domain() if result else None

    def get_all_categories(self) -> list[Category]:
        """
        Get all categories.

        Returns:
            list[Category]: A list of all categories.
        """
        return [
            category.to_domain() for category in self.category_repository.find_all()
        ]


@dataclass
class ArticleDbAdapter(ArticleDB):
    """
    Adapter class for Article database operations.

    Attributes:
        article_repository (ArticleRepository): The repository for Article
        operations.
    """

    article_repository: ArticleRepository

    def save_article(self, article: Article) -> Article:
        """
        Save a new article.

        Args:
            article (Article): The article to be saved.

        Returns:
            Article: The saved article.
        """
        article_to_add = ArticleEntity.from_domain(article)
        article_entity = self.article_repository.add_or_update(article_to_add)
        return article_entity.to_domain()

    def update_article(self, article: Article) -> Article:
        """
        Update an existing article.

        Args:
            article (Article): The article to be updated.

        Returns:
            Article: The updated article.
        """
        article_to_update = ArticleEntity.from_domain(article)
        article_entity = self.article_repository.add_or_update(article_to_update)
        return article_entity.to_domain()

    def delete_article(self, id_: int) -> None:
        """
        Delete an article.

        Args:
            id_ (int): The ID of the article to be deleted.
        """
        self.article_repository.delete(id_)

    def get_article_by_id(self, id_: int) -> Article | None:
        """
        Get an article by its ID.

        Args:
            id_ (int): The ID of the article.

        Returns:
            Article | None: The article with the given ID, or None if
            no such article exists.
        """
        result = self.article_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_article_by_title(self, title: str) -> Article | None:
        """
        Get an article by its title.

        Args:
            title (str): The title of the article.

        Returns:
            Article | None: The article with the given title, or None
            if no such article exists.
        """
        result = self.article_repository.find_by_title(title)
        return result.to_domain() if result else None

    def get_articles_with_category(self, category_id: int) -> list[Article]:
        """
        Get all articles with a specific category.

        Args:
            category_id (int): The ID of the category.

        Returns:
            list[Article]: A list of all articles with the given category.
        """
        return [
            article.to_domain()
            for article in self.article_repository.find_by_category_id(category_id)
        ]

    def get_all_articles(self) -> list[Article]:
        """
        Get all articles.

        Returns:
            list[Article]: A list of all articles.
        """
        return [article.to_domain() for article in self.article_repository.find_all()]


@dataclass
class TagDbAdapter(TagDB):
    """
    Adapter class for Tag database operations.

    Attributes:
        tag_repository (TagRepository): The repository for Tag operations.
    """

    tag_repository: TagRepository

    def save_tag(self, tag: Tag) -> Tag:
        """
        Save a new tag.

        Args:
            tag (Tag): The tag to be saved.

        Returns:
            Tag: The saved tag.
        """
        tag_to_add = TagEntity.from_domain(tag)
        tag_entity = self.tag_repository.add_or_update(tag_to_add)
        return tag_entity.to_domain()

    def update_tag(self, tag: Tag) -> Tag:
        """
        Update an existing tag.

        Args:
            tag (Tag): The tag to be updated.

        Returns:
            Tag: The updated tag.
        """
        tag_to_update = TagEntity.from_domain(tag)
        tag_entity = self.tag_repository.add_or_update(tag_to_update)
        return tag_entity.to_domain()

    def delete_tag(self, id_: int) -> None:
        """
        Delete a tag.

        Args:
            id_ (int): The ID of the tag to be deleted.
        """
        self.tag_repository.delete(id_)

    def get_tag_by_id(self, id_: int) -> Tag | None:
        """
        Get a tag by its ID.

        Args:
            id_ (int): The ID of the tag.

        Returns:
            Tag | None: The tag with the given ID, or None if no such tag
            exists.
        """
        result = self.tag_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_tag_by_name(self, name: str) -> Tag | None:
        """
        Get a tag by its name.

        Args:
            name (str): The name of the tag.

        Returns:
            Tag | None: The tag with the given name, or None if no such tag
            exists.
        """
        result = self.tag_repository.find_by_name(name)
        return result.to_domain() if result else None

    def get_tags_by_id(self, ids: list[int]) -> list[Tag]:
        """
        Get multiple tags by their IDs.

        Args:
            ids (list[int]): The IDs of the tags.

        Returns:
            list[Tag]: A list of the tags with the given IDs.
        """
        return [tag.to_domain() for tag in self.tag_repository.find_many_by_id(ids)]

    def get_all_tags(self) -> list[Tag]:
        """
        Get all tags.

        Returns:
            list[Tag]: A list of all tags.
        """
        return [tag.to_domain() for tag in self.tag_repository.find_all()]


@dataclass
class TranslationDbAdapter(TranslationDB):
    """
    Adapter class for Translation database operations.

    Attributes:
        translation_repository (TranslationRepository): The repository for
        Translation operations.
    """

    translation_repository: TranslationRepository

    def save_translation(self, translation: Translation) -> Translation:
        """
        Save a new translation.

        Args:
            translation (Translation): The translation to be saved.

        Returns:
            Translation: The saved translation.
        """
        translation_to_add = TranslationEntity.from_domain(translation)
        translation_entity = self.translation_repository.add_or_update(
            translation_to_add
        )
        return translation_entity.to_domain()

    def update_translation(self, translation: Translation) -> Translation:
        """
        Update an existing translation.

        Args:
            translation (Translation): The translation to be updated.

        Returns:
            Translation: The updated translation.
        """
        translation_to_update = TranslationEntity.from_domain(translation)
        translation_entity = self.translation_repository.add_or_update(
            translation_to_update
        )
        return translation_entity.to_domain()

    def get_translation_by_id(self, id_: int) -> Translation | None:
        """
        Get a translation by its ID.

        Args:
            id_ (int): The ID of the translation.

        Returns:
            Translation | None: The translation with the given ID, or None if
            no such translation exists.
        """
        result = self.translation_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_translation_by_article_and_language(
        self, article_id: int, language_id: int
    ) -> Translation | None:
        """
        Get a translation by its associated article and language.

        Args:
            article_id (int): The ID of the article.
            language_id (int): The ID of the language.

        Returns:
            Translation | None: The translation for the given article and
            language, or None if no such translation exists.
        """
        result = self.translation_repository.find_by_article_and_language(
            article_id, language_id
        )
        return result.to_domain() if result else None


@dataclass
class LanguageDbAdapter(LanguageDB):
    """
    Adapter class for Language database operations.

    Attributes:
        language_repository (LanguageRepository): The repository
        for Language operations.
    """

    language_repository: LanguageRepository

    def save_language(self, language: Language) -> Language:
        """
        Save a new language.

        Args:
            language (Language): The language to be saved.

        Returns:
            Language: The saved language.
        """
        language_to_add = LanguageEntity.from_domain(language)
        language_entity = self.language_repository.add_or_update(language_to_add)
        return language_entity.to_domain()

    def update_language(self, language: Language) -> Language:
        """
        Update an existing language.

        Args:
            language (Language): The language to be updated.

        Returns:
            Language: The updated language.
        """
        language_to_update = LanguageEntity.from_domain(language)
        language_entity = self.language_repository.add_or_update(language_to_update)
        return language_entity.to_domain()

    def get_language_by_name(self, name: str) -> Language | None:
        """
        Get a language by its name.

        Args:
            name (str): The name of the language.

        Returns:
            Language | None: The language with the given name, or None if no
            such language exists.
        """
        language = self.language_repository.find_by_name(name)
        return language.to_domain() if language else None

    def delete_language(self, id_: str) -> None:
        """
        Delete a language.

        Args:
            id_ (str): The ID of the language to be deleted.
        """
        self.language_repository.delete(id_)

    def get_language_by_id(self, id_: str) -> Language | None:
        """
        Get a language by its ID.

        Args:
            id_ (str): The ID of the language.

        Returns:
            Language | None: The language with the given ID, or None if
            no such language exists.
        """
        result = self.language_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_all_languages(self) -> list[Language]:
        """
        Get all languages.

        Returns:
            list[Language]: A list of all languages.
        """
        return [
            language.to_domain() for language in self.language_repository.find_all()
        ]


@dataclass
class FileStorageAdapter(FileStorage):
    """
    Adapter class for File Storage operations.

    Attributes:
        storage_manager (Boto3Service): The service for managing file
        storage operations.
    """

    storage_manager: Boto3Service

    def upload_content(self, content: str) -> str:
        """
        Upload content to file storage.

        Args:
            content (str): The content to be uploaded.

        Returns:
            str: The path of the uploaded content.
        """
        return self.storage_manager.upload_to_file(content)

    def read_content(self, content_path: str) -> str:
        """
        Read content from file storage.

        Args:
            content_path (str): The path of the content to be read.

        Returns:
            str: The content read from the file.
        """
        return self.storage_manager.read_file_content(content_path)

    def update_content(self, content_path: str, new_content: str) -> None:
        """
        Update content in file storage.

        Args:
            content_path (str): The path of the content to be updated.
            new_content (str): The new content to replace the existing content.
        """
        self.storage_manager.update_file_content(content_path, new_content)

    def delete_content(self, content_path) -> None:
        """
        Delete content from file storage.

        Args:
            content_path: The path of the content to be deleted.
        """
        self.storage_manager.delete_file(content_path)


@dataclass
class ArticleMessageBroker(ArticleEventPublisher):
    """
    Broker class for publishing Article events.

    Attributes:
        kafka_manager (KafkaService): The service for managing Kafka
        operations.
        translation_requests_topic (str): The topic for translation request
        events.
    """

    kafka_manager: KafkaService
    translation_requests_topic: str

    def publish_event(self, event: TranslationRequestEvent) -> None:
        """
        Publish a translation request event.

        Args:
            event (TranslationRequestEvent): The event to be published.
        """
        dto = TranslationRequestDTO.from_domain(event)
        self.kafka_manager.produce_message(self.translation_requests_topic, dto)


@dataclass
class LanguageMessageBroker(LanguageEventPublisher):
    """
    Broker class for publishing Language events.

    Attributes:
        kafka_manager (KafkaService): The service for managing Kafka
        operations.
        language_changes_topic (str): The topic for language change events.
    """

    kafka_manager: KafkaService
    language_changes_topic: str

    def publish_event(self, event: LanguageEvent) -> None:
        """
        Publish a language event.

        Args:
            event (LanguageEvent): The event to be published.
        """
        dto = LanguageChangeEvent.from_domain(event)
        self.kafka_manager.produce_message(self.language_changes_topic, dto)
