from articles.domain.model import Category, Article, Tag, Translation, Language
from articles.domain.event import ArticleTranslationEvent
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


class TranslationDbOutputPort(ABC):

    @abstractmethod
    def save_translation(self, translation: Translation) -> Translation:
        pass

    @abstractmethod
    def update_translation(self, translation: Translation) -> Translation:
        pass

    @abstractmethod
    def get_translation_by_id(self, id_: int) -> Translation | None:
        pass

    @abstractmethod
    def get_translation_by_article_and_language(self, article_id: int, language_id: int) -> Translation | None:
        pass


class LanguageDbOutputPort(ABC):

    @abstractmethod
    def save_language(self, language: Language) -> Language:
        pass

    @abstractmethod
    def get_language_by_id(self, id_: int) -> Language | None:
        pass

    @abstractmethod
    def get_language_by_name(self, name: str) -> Language | None:
        pass

    @abstractmethod
    def update_language(self, language: Language) -> Language:
        pass

    @abstractmethod
    def delete_language(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_all_languages(self) -> list[Language]:
        pass


class FileStorageOutputAdapter(ABC):

    @abstractmethod
    def upload_content(self, content: str) -> str:
        pass

    @abstractmethod
    def read_content(self, content_path: str) -> str:
        pass

    @abstractmethod
    def update_content(self, content_path: str, new_content: str) -> None:
        pass

    @abstractmethod
    def delete_content(self, content_path: str) -> None:
        pass


class ArticleEventPublisher(ABC):

    @abstractmethod
    def publish_article_translation_request(self, article_translation_event: ArticleTranslationEvent) -> None:
        pass
