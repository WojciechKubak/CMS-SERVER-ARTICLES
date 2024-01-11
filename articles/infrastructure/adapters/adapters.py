from articles.ports.output import CategoryDbOutputPort, ArticleDbOutputPort, TagDbOutputPort
from articles.infrastructure.db.repository import CategoryRepository, ArticleRepository, TagRepository
from articles.infrastructure.db.entity import CategoryEntity, ArticleEntity, TagEntity
from articles.domain.model import Category, Article, Tag
from dataclasses import dataclass


@dataclass
class CategoryDbAdapter(CategoryDbOutputPort):
    category_repository: CategoryRepository

    def save_category(self, category: Category) -> Category:
        category_to_add = CategoryEntity.from_domain(category)
        self.category_repository.add(category_to_add)
        return category_to_add.to_domain()

    def update_category(self, category: Category) -> Category:
        category_to_update = CategoryEntity.from_domain(category)
        self.category_repository.update(category_to_update)
        return category_to_update.to_domain()

    def delete_category(self, id_: int) -> None:
        self.category_repository.delete(id_)

    def get_category_by_id(self, id_: int) -> Category | None:
        if category := self.category_repository.find_by_id(id_):
            return category.to_domain()
        return None

    def get_category_by_name(self, name: str) -> Category | None:
        if category := self.category_repository.find_by_name(name):
            return category.to_domain()
        return None

    def get_all_categories(self) -> list[Category]:
        return [category.to_domain() for category in self.category_repository.find_all()]


@dataclass
class ArticleDbAdapter(ArticleDbOutputPort):
    article_repository: ArticleRepository

    def save_article(self, article: Article) -> Article:
        article_to_add = ArticleEntity.from_domain(article)
        self.article_repository.add(article_to_add)
        return article_to_add.to_domain()

    def update_article(self, article: Article) -> Article:
        article_to_update = ArticleEntity.from_domain(article)
        self.article_repository.update(article_to_update)
        return article_to_update.to_domain()

    def delete_article(self, id_: int) -> None:
        self.article_repository.delete(id_)

    def get_article_by_id(self, id_: int) -> Article | None:
        if article := self.article_repository.find_by_id(id_):
            return article.to_domain()
        return None

    def get_article_by_title(self, title: str) -> Article | None:
        if article := self.article_repository.find_by_title(title):
            return article.to_domain()
        return None

    def get_articles_with_category(self, category_id: int) -> list[Article]:
        return [article.to_domain() for article in self.article_repository.find_by_category_id(category_id)]

    def get_all_articles(self) -> list[Article]:
        return [article.to_domain() for article in self.article_repository.find_all()]


@dataclass
class TagDbAdapter(TagDbOutputPort):
    tag_repository: TagRepository

    def save_tag(self, tag: Tag) -> Tag:
        tag_to_add = TagEntity.from_domain(tag)
        self.tag_repository.add(tag_to_add)
        return tag_to_add.to_domain()

    def update_tag(self, tag: Tag) -> Tag:
        tag_to_update = TagEntity.from_domain(tag)
        self.tag_repository.update(tag_to_update)
        return tag_to_update.to_domain()

    def delete_tag(self, id_: int) -> None:
        self.tag_repository.delete(id_)

    def get_tag_by_id(self, id_: int) -> Tag | None:
        if tag := self.tag_repository.find_by_id(id_):
            return tag.to_domain()
        return None

    def get_tag_by_name(self, name: str) -> Tag | None:
        if tag := self.tag_repository.find_by_name(name):
            return tag.to_domain()
        return None

    def get_tags_by_id(self, ids: list[int]) -> list[Tag]:
        return [tag.to_domain() for tag in self.tag_repository.find_many_by_id(ids)]

    def get_all_tags(self) -> list[Tag]:
        return [tag.to_domain() for tag in self.tag_repository.find_all()]
