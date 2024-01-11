from articles.ports.input import CategoryApiInputPort, ArticleApiInputPort, TagApiInputPort
from articles.ports.output import CategoryDbOutputPort, ArticleDbOutputPort, TagDbOutputPort
from articles.domain.model import Category, Article, Tag
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

    def create_article(self, article: Article) -> Article:
        if self.article_db_adapter.get_article_by_title(article.title):
            raise ValueError('Article title already exists')
        if not (category := self.category_db_adapter.get_category_by_id(article.category.id_)):
            raise ValueError('Category does not exist')
        tags_id = [tag.id_ for tag in article.tags]
        if len(tags := self.tag_db_adapter.get_tags_by_id(tags_id)) != len(tags_id):
            raise ValueError('Tag does not exist')

        article_to_create = article.with_category_and_tags(category, tags)
        return self.article_db_adapter.save_article(article_to_create)

    def update_article(self, article: Article) -> Article:
        if not self.article_db_adapter.get_article_by_id(article.id_):
            raise ValueError('Article does not exist')
        result = self.article_db_adapter.get_article_by_title(article.title)
        if result and result.id_ != article.id_:
            raise ValueError('Article title already exists')
        if not (category := self.category_db_adapter.get_category_by_id(article.category.id_)):
            raise ValueError('Category does not exist')
        tags_id = [tag.id_ for tag in article.tags]
        if len(tags := self.tag_db_adapter.get_tags_by_id(tags_id)) != len(tags_id):
            raise ValueError('Tag does not exist')

        article_to_update = article.with_category_and_tags(category, tags)
        return self.article_db_adapter.update_article(article_to_update)

    def delete_article(self, id_: int) -> int:
        if not self.article_db_adapter.get_article_by_id(id_):
            raise ValueError('Article does not exist')
        self.article_db_adapter.delete_article(id_)
        return id_

    def get_article_by_id(self, id_: int) -> Article:
        if not (article := self.article_db_adapter.get_article_by_id(id_)):
            raise ValueError('Article does not exist')
        return article

    def get_articles_with_category(self, category_id: int) -> list[Article]:
        if not self.category_db_adapter.get_category_by_id(category_id):
            raise ValueError('Category does not exist')
        return self.article_db_adapter.get_articles_with_category(category_id)

    def get_all_articles(self) -> list[Article]:
        return self.article_db_adapter.get_all_articles()


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
