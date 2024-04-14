from articles.application.port.input import ArticleApiInputPort, CategoryApiInputPort, TagApiInputPort
from articles.domain.service import ArticleDomainService, CategoryDomainService, TagDomainService
from articles.domain.model import Category, Article, Tag
from dataclasses import dataclass
from typing import Any


@dataclass
class CategoryApiService(CategoryApiInputPort):
    category_service: CategoryDomainService

    def create_category(self, data: dict[str, Any]) -> Category:
        return self.category_service.create_category(Category.from_dto(data))

    def update_category(self, data: dict[str, Any]) -> Category:
        return self.category_service.update_category(Category.from_dto(data))

    def delete_category(self, id_: int) -> int:
        return self.category_service.delete_category(id_)

    def get_category_by_id(self, id_: int) -> Category:
        return self.category_service.get_category_by_id(id_)

    def get_all_categories(self) -> list[Category]:
        return self.category_service.get_all_categories()


@dataclass
class ArticleApiService(ArticleApiInputPort):
    article_service: ArticleDomainService

    def create_article(self, data: dict[str, Any]) -> Article:
        return self.article_service.create_article(Article.from_dto(data))

    def update_article(self, data: dict[str, Any]) -> Article:
        return self.article_service.update_article(Article.from_dto(data))

    def delete_article(self, id_: int) -> int:
        return self.article_service.delete_article(id_)

    def get_article_by_id(self, id_: int) -> Article:
        return self.article_service.get_article_by_id(id_)

    def get_articles_with_category(self, category_id: int) -> list[Article]:
        return self.article_service.get_articles_with_category(category_id)

    def get_all_articles(self) -> list[Article]:
        return self.article_service.get_all_articles()


@dataclass
class TagApiService(TagApiInputPort):
    tag_service: TagDomainService

    def create_tag(self, data: dict[str, Any]) -> Tag:
        return self.tag_service.create_tag(Tag.from_dto(data))

    def update_tag(self, data: dict[str, Any]) -> Tag:
        return self.tag_service.update_tag(Tag.from_dto(data))

    def delete_tag(self, id_: int) -> int:
        return self.tag_service.delete_tag(id_)

    def get_tag_by_id(self, id_: int) -> Tag:
        return self.tag_service.get_tag_by_id(id_)

    def get_all_tags(self) -> list[Tag]:
        return self.tag_service.get_all_tags()
