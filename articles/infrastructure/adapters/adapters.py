from articles.application.ports.output import (
    CategoryDB,
    ArticleDB,
    TagDB,
    LanguageDB,
    TranslationDB,
    FileStorage,
    ArticleEventPublisher,
    LanguageEventPublisher
)
from articles.infrastructure.persistance.repository import (
    CategoryRepository,
    ArticleRepository,
    TagRepository,
    TranslationRepository,
    LanguageRepository
)
from articles.infrastructure.persistance.entity import (
    CategoryEntity,
    ArticleEntity,
    TagEntity,
    TranslationEntity,
    LanguageEntity
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
    LanguageChangeEvent
)
from dataclasses import dataclass


@dataclass
class CategoryDbAdapter(CategoryDB):
    category_repository: CategoryRepository

    def save_category(self, category: Category) -> Category:
        category_to_add = CategoryEntity.from_domain(category)
        category_entity = self.category_repository.add_or_update(
            category_to_add)
        return category_entity.to_domain()

    def update_category(self, category: Category) -> Category:
        category_to_update = CategoryEntity.from_domain(category)
        category_entity = self.category_repository.add_or_update(
            category_to_update)
        return category_entity.to_domain()

    def delete_category(self, id_: int) -> None:
        self.category_repository.delete(id_)

    def get_category_by_id(self, id_: int) -> Category | None:
        result = self.category_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_category_by_name(self, name: str) -> Category | None:
        result = self.category_repository.find_by_name(name)
        return result.to_domain() if result else None

    def get_all_categories(self) -> list[Category]:
        return [
            category.to_domain()
            for category in self.category_repository.find_all()
        ]


@dataclass
class ArticleDbAdapter(ArticleDB):
    article_repository: ArticleRepository

    def save_article(self, article: Article) -> Article:
        article_to_add = ArticleEntity.from_domain(article)
        article_entity = self.article_repository.add_or_update(article_to_add)
        return article_entity.to_domain()

    def update_article(self, article: Article) -> Article:
        article_to_update = ArticleEntity.from_domain(article)
        article_entity = self.article_repository.add_or_update(
            article_to_update)
        return article_entity.to_domain()

    def delete_article(self, id_: int) -> None:
        self.article_repository.delete(id_)

    def get_article_by_id(self, id_: int) -> Article | None:
        result = self.article_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_article_by_title(self, title: str) -> Article | None:
        result = self.article_repository.find_by_title(title)
        return result.to_domain() if result else None

    def get_articles_with_category(self, category_id: int) -> list[Article]:
        return [
            article.to_domain()
            for article in self.article_repository.find_by_category_id(
                category_id)
        ]

    def get_all_articles(self) -> list[Article]:
        return [
            article.to_domain()
            for article in self.article_repository.find_all()
        ]


@dataclass
class TagDbAdapter(TagDB):
    tag_repository: TagRepository

    def save_tag(self, tag: Tag) -> Tag:
        tag_to_add = TagEntity.from_domain(tag)
        tag_entity = self.tag_repository.add_or_update(tag_to_add)
        return tag_entity.to_domain()

    def update_tag(self, tag: Tag) -> Tag:
        tag_to_update = TagEntity.from_domain(tag)
        tag_entity = self.tag_repository.add_or_update(tag_to_update)
        return tag_entity.to_domain()

    def delete_tag(self, id_: int) -> None:
        self.tag_repository.delete(id_)

    def get_tag_by_id(self, id_: int) -> Tag | None:
        result = self.tag_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_tag_by_name(self, name: str) -> Tag | None:
        result = self.tag_repository.find_by_name(name)
        return result.to_domain() if result else None

    def get_tags_by_id(self, ids: list[int]) -> list[Tag]:
        return [
            tag.to_domain()
            for tag in self.tag_repository.find_many_by_id(ids)
        ]

    def get_all_tags(self) -> list[Tag]:
        return [tag.to_domain() for tag in self.tag_repository.find_all()]


@dataclass
class TranslationDbAdapter(TranslationDB):
    translation_repository: TranslationRepository

    def save_translation(self, translation: Translation) -> Translation:
        translation_to_add = TranslationEntity.from_domain(translation)
        translation_entity = self.translation_repository.add_or_update(
            translation_to_add)
        return translation_entity.to_domain()

    def update_translation(self, translation: Translation) -> Translation:
        translation_to_update = TranslationEntity.from_domain(translation)
        translation_entity = self.translation_repository.add_or_update(
            translation_to_update)
        return translation_entity.to_domain()

    def get_translation_by_id(self, id_: int) -> Translation | None:
        result = self.translation_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_translation_by_article_and_language(
            self,
            article_id: int,
            language_id: int
    ) -> Translation | None:
        result = self.translation_repository.find_by_article_and_language(
            article_id, language_id)
        return result.to_domain() if result else None


@dataclass
class LanguageDbAdapter(LanguageDB):
    language_repository: LanguageRepository

    def save_language(self, language: Language) -> Language:
        language_to_add = LanguageEntity.from_domain(language)
        language_entity = self.language_repository.add_or_update(
            language_to_add)
        return language_entity.to_domain()

    def update_language(self, language: Language) -> Language:
        language_to_update = LanguageEntity.from_domain(language)
        language_entity = self.language_repository.add_or_update(
            language_to_update)
        return language_entity.to_domain()

    def get_language_by_name(self, name: str) -> Language | None:
        language = self.language_repository.find_by_name(name)
        return language.to_domain() if language else None

    def delete_language(self, id_: str) -> None:
        self.language_repository.delete(id_)

    def get_language_by_id(self, id_: str) -> Language | None:
        result = self.language_repository.find_by_id(id_)
        return result.to_domain() if result else None

    def get_all_languages(self) -> list[Language]:
        return [
            language.to_domain()
            for language in self.language_repository.find_all()
        ]


@dataclass
class FileStorageAdapter(FileStorage):
    storage_manager: Boto3Service

    def upload_content(self, content: str) -> str:
        return self.storage_manager.upload_to_file(content)

    def read_content(self, content_path: str) -> str:
        return self.storage_manager.read_file_content(content_path)

    def update_content(self, content_path: str, new_content: str) -> None:
        self.storage_manager.update_file_content(content_path, new_content)

    def delete_content(self, content_path) -> None:
        self.storage_manager.delete_file(content_path)


@dataclass
class ArticleMessageBroker(ArticleEventPublisher):
    kafka_manager: KafkaService
    translation_requests_topic: str

    def publish_event(self, event: TranslationRequestEvent) -> None:
        dto = TranslationRequestDTO.from_domain(event)
        self.kafka_manager.produce_message(
            self.translation_requests_topic, dto)


@dataclass
class LanguageMessageBroker(LanguageEventPublisher):
    kafka_manager: KafkaService
    language_changes_topic: str

    def publish_event(self, event: LanguageEvent) -> None:
        dto = LanguageChangeEvent.from_domain(event)
        self.kafka_manager.produce_message(self.language_changes_topic, dto)
