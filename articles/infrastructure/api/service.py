from articles.application.port.input import (
    ArticleApiInputPort, 
    CategoryApiInputPort, 
    TagApiInputPort,
    LanguageApiInputPort,
    TranslationApiInputPort,
    ArticleTranslationUseCase,
)
from articles.infrastructure.api.dto import CategoryDTO, TagDTO, ArticleDTO, LanguageDTO
from articles.domain.model import Category, Article, Tag, Translation, Language
from dataclasses import dataclass
from typing import Union


@dataclass
class CategoryApiService:
    category_service: CategoryApiInputPort

    def create_category(self, category_dto: CategoryDTO) -> Category:
        return self.category_service.create_category(category_dto.to_domain())

    def update_category(self, category_dto: CategoryDTO) -> Category:
        return self.category_service.update_category(category_dto.to_domain())

    def delete_category(self, id_: int) -> int:
        return self.category_service.delete_category(id_)

    def get_category_by_id(self, id_: int) -> Category:
        return self.category_service.get_category_by_id(id_)

    def get_all_categories(self) -> list[Category]:
        return self.category_service.get_all_categories()


@dataclass
class ArticleApiService:
    article_service: ArticleApiInputPort

    def create_article(self, article_dto: ArticleDTO) -> Article:
        return self.article_service.create_article(article_dto.to_domain())

    def update_article(self, article_dto: ArticleDTO) -> Article:
        return self.article_service.update_article(article_dto.to_domain())

    def delete_article(self, id_: int) -> int:
        return self.article_service.delete_article(id_)

    def get_article_by_id(self, id_: int) -> Article:
        return self.article_service.get_article_by_id(id_)

    def get_articles_with_category(self, category_id: int) -> list[Article]:
        return self.article_service.get_articles_with_category(category_id)

    def get_all_articles(self) -> list[Article]:
        return self.article_service.get_all_articles()
    
    def request_article_translation(self, article_id: int, language_id: int) -> None:
        return self.article_service.request_article_translation(article_id, language_id)


@dataclass
class TagApiService:
    tag_service: TagApiInputPort

    def create_tag(self, tag_dto: TagDTO) -> Tag:
        return self.tag_service.create_tag(tag_dto.to_domain())

    def update_tag(self, tag_dto: TagDTO) -> Tag:
        return self.tag_service.update_tag(tag_dto.to_domain())

    def delete_tag(self, id_: int) -> int:
        return self.tag_service.delete_tag(id_)

    def get_tag_by_id(self, id_: int) -> Tag:
        return self.tag_service.get_tag_by_id(id_)

    def get_all_tags(self) -> list[Tag]:
        return self.tag_service.get_all_tags()


@dataclass
class LanguageApiService:
    language_service: LanguageApiInputPort

    def create_language(self, language_dto: LanguageDTO) -> Language:
        return self.language_service.create_language(language_dto.to_domain())

    def update_language(self, language_dto: LanguageDTO) -> Language:
        return self.language_service.update_language(language_dto.to_domain())
    
    def delete_language(self, id_: int) -> int:
        return self.language_service.delete_language(id_)
    
    def get_language_by_id(self, id_: int) -> Language:
        return self.language_service.get_language_by_id(id_)
    
    def get_all_languages(self) -> list[Language]:
        return self.language_service.get_all_languages()


@dataclass
class TranslationApiService:
    translation_service: Union[TranslationApiInputPort, ArticleTranslationUseCase]

    def get_translation_by_id(self, id_: int) -> Translation:
        return self.translation_service.get_translation_by_id(id_)
    
    def request_translation(self, article_id: int, language_id: int) -> Translation:
        return self.translation_service.request_article_translation(article_id, language_id)
