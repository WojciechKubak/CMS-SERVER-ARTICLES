from articles.domain.model import Category, Article, Tag, Translation, Language
from articles.domain.event import ArticleTranslatedEvent
from abc import ABC, abstractmethod


class CategoryAPI(ABC):

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


class ArticleAPI(ABC):

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


class TagAPI(ABC):

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


class TranslationAPI(ABC):

    @abstractmethod
    def get_translation_by_id(self, id_: int) -> Translation:
        pass


class LanguageAPI(ABC):

    @abstractmethod
    def create_language(self, language: Language) -> Language:
        pass

    @abstractmethod
    def update_language(self, language: Language) -> Language:
        pass

    @abstractmethod
    def delete_language(self, id_: int) -> int:
        pass

    @abstractmethod
    def get_language_by_id(self, id_: int) -> Language:
        pass

    @abstractmethod
    def get_all_languages(self) -> list[Language]:
        pass


class TranslationRequestUseCase(ABC):

    @abstractmethod
    def request_translation(
        self,
        article_id: int,
        language_id: int
    ) -> Translation:
        pass


class TranslationConsumer(ABC):

    @abstractmethod
    def handle_translation_event(
        self,
        event: ArticleTranslatedEvent
    ) -> Translation:
        pass
