from articles.domain.model import Category, Article, Tag
from abc import ABC, abstractmethod


class CategoryDbOutputPort(ABC):

    @abstractmethod
    def save_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update_category(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete_category(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_category_by_id(self, id_: int) -> Category | None:
        pass

    @abstractmethod
    def get_category_by_name(self, name: str) -> Category | None:
        pass

    @abstractmethod
    def get_all_categories(self) -> list[Category]:
        pass


class ArticleDbOutputPort(ABC):

    @abstractmethod
    def save_article(self, article: Article) -> Article:
        pass

    @abstractmethod
    def update_article(self, article: Article) -> Article:
        pass

    @abstractmethod
    def delete_article(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_article_by_id(self, id_: int) -> Article | None:
        pass

    @abstractmethod
    def get_article_by_title(self, title: str) -> Article | None:
        pass

    @abstractmethod
    def get_articles_with_category(self, category_id: int) -> list[Article]:
        pass

    @abstractmethod
    def get_all_articles(self) -> list[Article]:
        pass


class TagDbOutputPort(ABC):

    @abstractmethod
    def save_tag(self, tag: Tag) -> Tag:
        pass

    @abstractmethod
    def update_tag(self, tag: Tag) -> Tag:
        pass

    @abstractmethod
    def delete_tag(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_tag_by_id(self, id_: int) -> Tag | None:
        pass

    @abstractmethod
    def get_tag_by_name(self, name: str) -> Tag | None:
        pass

    @abstractmethod
    def get_tags_by_id(self, ids: list[int]) -> list[Tag]:
        pass

    @abstractmethod
    def get_all_tags(self) -> list[Tag]:
        pass


class FileStorageOutputAdapter(ABC):

    @abstractmethod
    def upload_article_content(self, article: Article) -> str:
        pass

    @abstractmethod
    def read_article_content(self, article: Article) -> str:
        pass

    @abstractmethod
    def update_article_content(self, article: Article, new_content: str) -> None:
        pass

    @abstractmethod
    def delete_article_content(self, article: Article) -> None:
        pass
