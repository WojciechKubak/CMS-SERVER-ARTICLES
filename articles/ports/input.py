from articles.domain.model import Category, Article, Tag
from abc import ABC, abstractmethod


class CategoryApiInputPort(ABC):

    @abstractmethod
    def create_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete_category(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_category_by_id(self, id_: int) -> Category:
        pass

    @abstractmethod
    def get_all_categories(self) -> list[Category]:
        pass


class ArticleApiInputPort(ABC):

    @abstractmethod
    def create_article(self, article: Article) -> Article:
        pass

    @abstractmethod
    def update_article(self, article: Article) -> Article:
        pass

    @abstractmethod
    def delete_article(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_article_by_id(self, id_: int) -> Article:
        pass

    @abstractmethod
    def get_articles_with_category(self, category_id: int) -> list[Article]:
        pass

    @abstractmethod
    def get_all_articles(self) -> list[Article]:
        pass


class TagApiInputPort(ABC):

    @abstractmethod
    def create_tag(self, tag: Tag) -> Tag:
        pass

    @abstractmethod
    def update_tag(self, tag: Tag) -> Tag:
        pass

    @abstractmethod
    def delete_tag(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_tag_by_id(self, id_: int) -> Tag:
        pass

    @abstractmethod
    def get_all_tags(self) -> list[Tag]:
        pass
