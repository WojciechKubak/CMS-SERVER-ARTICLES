from articles.application.port.input import (
    CategoryApiInputPort, 
    ArticleApiInputPort, 
    TagApiInputPort,
    TranslationApiInputPort,
    LanguageApiInputPort,
    ArticleTranslationUseCase,
    ArticleTranslationEventConsumer
)
from articles.application.port.output import (
    CategoryDbOutputPort, 
    ArticleDbOutputPort, 
    TagDbOutputPort, 
    TranslationDbOutputPort,
    LanguageDbOutputPort,
    FileStorageOutputAdapter,
    ArticleEventPublisher,
    LanguageEventPublisher
)
from articles.domain.event import (
    TranslationRequestEvent, 
    ArticleTranslatedEvent,
    LanguageEvent,
    LanguageEventType
)
from articles.domain.model import Category, Article, Tag, Translation, Language
from dataclasses import dataclass


@dataclass
class CategoryDomainService(CategoryApiInputPort):
    category_db_adapter: CategoryDbOutputPort

    def create_category(self, category: Category) -> Category:
        if self.category_db_adapter.get_category_by_name(category.name):
            raise ValueError('Category name already exists')
        added_category = self.category_db_adapter.save_category(category)
        return added_category

    def update_category(self, category: Category) -> Category:
        if not self.category_db_adapter.get_category_by_id(category.id_):
            raise ValueError('Category does not exist')
        result = self.category_db_adapter.get_category_by_name(category.name)
        if result and result.id_ != category.id_:
            raise ValueError('Category name already exists')
        updated_category = self.category_db_adapter.update_category(category)
        return updated_category

    def delete_category(self, id_: int) -> int:
        if not self.category_db_adapter.get_category_by_id(id_):
            raise ValueError('Category does not exist')
        self.category_db_adapter.delete_category(id_)
        return id_

    def get_category_by_id(self, id_: int) -> Category:
        if not (category := self.category_db_adapter.get_category_by_id(id_)):
            raise ValueError('Category does not exist')
        return category

    def get_all_categories(self) -> list[Category]:
        return self.category_db_adapter.get_all_categories()


@dataclass
class ArticleDomainService(ArticleApiInputPort):
    article_db_adapter: ArticleDbOutputPort
    category_db_adapter: CategoryDbOutputPort
    tag_db_adapter: TagDbOutputPort
    storage_manager: FileStorageOutputAdapter

    def create_article(self, article: Article) -> Article:
        if self.article_db_adapter.get_article_by_title(article.title):
            raise ValueError('Article title already exists')
        if not (category := self.category_db_adapter.get_category_by_id(article.category)):
            raise ValueError('Category does not exist')
        if len(tags := self.tag_db_adapter.get_tags_by_id(article.tags)) != len(article.tags):
            raise ValueError('Tag does not exist')
        
        content_path = self.storage_manager.upload_content(article.content)  
        article_to_add = article\
            .change_category_and_tags(category, tags)\
            .change_content(content_path)

        added_article = self.article_db_adapter \
            .save_article(article_to_add) \
            .change_content(article.content)
        
        return added_article

    def update_article(self, article: Article) -> Article:
        article_by_id = self.article_db_adapter.get_article_by_id(article.id_)
        if not article_by_id:
            raise ValueError('Article does not exist')
        article_by_title = self.article_db_adapter.get_article_by_title(article.title)
        if article_by_title and article_by_title.id_ != article.id_:
            raise ValueError('Article title already exists')
        category_by_id = self.category_db_adapter.get_category_by_id(article.category)
        if not category_by_id:
            raise ValueError('Category does not exist')
        tags_by_id = self.tag_db_adapter.get_tags_by_id(article.tags)
        if len(tags_by_id) != len(article.tags):
            raise ValueError('Tag does not exist')
        
        article_to_update = article.change_category_and_tags(
            category_by_id, tags_by_id)
        self.storage_manager.update_content(article_by_id.content, article.content)

        updated_article = self.article_db_adapter.update_article(article_to_update)

        return updated_article

    def delete_article(self, id_: int) -> int:
        article_by_id = self.article_db_adapter.get_article_by_id(id_)
        if not article_by_id:
            raise ValueError('Article does not exist')
        self.storage_manager.delete_content(article_by_id.content)
        self.article_db_adapter.delete_article(id_)
        
        return id_

    def get_article_by_id(self, id_: int) -> Article:
        if not (article := self.article_db_adapter.get_article_by_id(id_)):
            raise ValueError('Article does not exist')
        content = self.storage_manager.read_content(article.content)
        return article.change_content(content)

    def get_articles_with_category(self, category_id: int) -> list[Article]:
        if not self.category_db_adapter.get_category_by_id(category_id):
            raise ValueError('Category does not exist')
        return self.article_db_adapter.get_articles_with_category(category_id)

    def get_all_articles(self) -> list[Article]:
        return [article.change_content(self.storage_manager.read_content(article.content)) 
                for article in self.article_db_adapter.get_all_articles()]


@dataclass
class TagDomainService(TagApiInputPort):
    tag_db_adapter: TagDbOutputPort

    def create_tag(self, tag: Tag) -> Tag:
        if self.tag_db_adapter.get_tag_by_name(tag.name):
            raise ValueError('Tag name already exists')
        added_tag = self.tag_db_adapter.save_tag(tag)
        return added_tag

    def update_tag(self, tag: Tag) -> Tag:
        if not self.tag_db_adapter.get_tag_by_id(tag.id_):
            raise ValueError('Tag does not exist')
        result = self.tag_db_adapter.get_tag_by_name(tag.name)
        if result and result.id_ != tag.id_:
            raise ValueError('Tag name already exists')
        updated_tag = self.tag_db_adapter.update_tag(tag)
        return updated_tag

    def delete_tag(self, id_: int) -> int:
        if not self.tag_db_adapter.get_tag_by_id(id_):
            raise ValueError('Tag does not exist')
        self.tag_db_adapter.delete_tag(id_)
        return id_

    def get_tag_by_id(self, id_: int) -> Tag:
        if not (tag := self.tag_db_adapter.get_tag_by_id(id_)):
            raise ValueError('Tag does not exist')
        return tag

    def get_all_tags(self) -> list[Tag]:
        return self.tag_db_adapter.get_all_tags()


@dataclass
class TranslationDomainService(
        TranslationApiInputPort,
        ArticleTranslationUseCase, 
        ArticleTranslationEventConsumer
    ):
    article_db_adapter: ArticleDbOutputPort
    language_db_adapter: LanguageDbOutputPort
    translation_db_adapter: TranslationDbOutputPort
    storage_manager: FileStorageOutputAdapter
    message_broker: ArticleEventPublisher

    def get_translation_by_id(self, id_: int) -> Translation:
        translation = self.translation_db_adapter.get_translation_by_id(id_)
        if not translation:
            raise ValueError('Translation does not exist')
        content = self.storage_manager.read_content(translation.content)
        translation.content = content
        return translation
    
    def request_article_translation(self, article_id: int, language_id: str) -> Translation:
        language = self.language_db_adapter.get_language_by_id(language_id)
        if not language:
            raise ValueError('Language does not exist')
        article = self.article_db_adapter.get_article_by_id(article_id)
        if not article:
            raise ValueError('Article does not exist')
        if self.translation_db_adapter.get_translation_by_article_and_language(
            article_id, language_id):
            raise ValueError('Translation already exists')
        
        translation_to_add = Translation.create_request(language, article)
        added_translation = self.translation_db_adapter.save_translation(translation_to_add)
        
        article_translation_event = TranslationRequestEvent.from_domain(article, language)
        self.message_broker.publish_translation_request(article_translation_event)

        return added_translation

    def handle_translated_article(self, article_translated_event: ArticleTranslatedEvent) -> Translation:
        if not self.article_db_adapter.get_article_by_id(article_translated_event.article_id):
            raise ValueError('Article does not exist') 
        if not self.language_db_adapter.get_language_by_id(article_translated_event.language_id):
            raise ValueError('Language does not exist')
        translation = self.translation_db_adapter.get_translation_by_article_and_language(
            article_translated_event.article_id, 
            article_translated_event.language_id
        )
        if not translation:
            raise ValueError('Translation does not exist')
        if translation.is_ready:
            raise ValueError('Translation already published')
        
        translation = translation.publish(article_translated_event.content_path)
        self.translation_db_adapter.update_translation(translation)

        return translation


@dataclass
class LanguageDomainService(LanguageApiInputPort):
    language_db_adapter: LanguageDbOutputPort
    language_event_publisher: LanguageEventPublisher

    def create_language(self, language: Language) -> Language:
        if self.language_db_adapter.get_language_by_name(language.name):
            raise ValueError('Language name already exists')
        added_language = self.language_db_adapter.save_language(language)

        language_event = LanguageEvent.from_domain(
            added_language, LanguageEventType.CREATE)
        self.language_event_publisher.publish_language_event(language_event)

        return added_language

    def update_language(self, language: Language) -> Language:
        if not self.language_db_adapter.get_language_by_id(language.id_):
            raise ValueError('Language does not exist')
        updated_language = self.language_db_adapter.update_language(language)

        language_event = LanguageEvent.from_domain(
            updated_language, LanguageEventType.UPDATE)
        self.language_event_publisher.publish_language_event(language_event)

        return updated_language

    def delete_language(self, id_: str) -> None:
        if not self.language_db_adapter.get_language_by_id(id_):
            raise ValueError('Language does not exist')
        
        language_to_delete = self.language_db_adapter.get_language_by_id(id_)
        language_event = LanguageEvent.from_domain(
            language_to_delete, LanguageEventType.DELETE)
        self.language_event_publisher.publish_language_event(language_event)

        self.language_db_adapter.delete_language(id_)

    def get_language_by_id(self, id_: str) -> Language:
        if not (language := self.language_db_adapter.get_language_by_id(id_)):
            raise ValueError('Language does not exist')
        return language

    def get_all_languages(self) -> list[Language]:
        return self.language_db_adapter.get_all_languages()
