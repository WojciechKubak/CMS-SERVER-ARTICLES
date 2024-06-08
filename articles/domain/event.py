from articles.domain.model import Article, Language
from dataclasses import dataclass
from datetime import datetime
from typing import Self
from enum import Enum


class LanguageEventType(Enum):
    """
    Enum representing the types of events that can occur for a Language.
    """

    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


@dataclass
class LanguageEvent:
    """
    Data class representing an event related to a Language.

    Attributes:
        id_ (int): The ID of the language.
        name (str): The name of the language.
        code (str): The code of the language.
        event_type (LanguageEventType): The type of the event.
    """

    id_: int
    name: str
    code: str
    event_type: LanguageEventType

    @classmethod
    def create(cls, language: Language, event_type: LanguageEventType) -> Self:
        """
        Class method to create a LanguageEvent from a Language instance and an
        event type.

        Args:
            language (Language): The language related to the event.
            event_type (LanguageEventType): The type of the event.

        Returns:
            LanguageEvent: The created LanguageEvent instance.
        """
        return cls(
            id_=language.id_,
            name=language.name,
            code=language.code,
            event_type=event_type,
        )


@dataclass
class TranslationRequestEvent:
    """
    Data class representing a request to translate an Article.

    Attributes:
        article_id (int): The ID of the article.
        title (str): The title of the article.
        content_path (str): The path to the content of the article.
        language_id (int): The ID of the language to translate
        the article into.
        date (datetime): The date of the translation request.
    """

    article_id: int
    title: str
    content_path: str
    language_id: int
    date: datetime

    @classmethod
    def create(cls, article: Article, language: Language) -> Self:
        """
        Class method to create a TranslationRequestEvent from an Article
        instance and a Language instance.

        Args:
            article (Article): The article to be translated.
            language (Language): The language to translate the article into.

        Returns:
            TranslationRequestEvent: The created TranslationRequestEvent
            instance.
        """
        return cls(
            article_id=article.id_,
            title=article.title,
            content_path=article.content,
            language_id=language.id_,
            date=datetime.now(),
        )


@dataclass
class ArticleTranslatedEvent:
    """
    Data class representing the event of an Article being translated.

    Attributes:
        article_id (int): The ID of the article.
        title (str): The title of the article.
        content_path (str): The path to the content of the article.
        language_id (int): The ID of the language the article
        was translated into.
        author_id (int): The ID of the author who translated the article.
    """

    article_id: int
    title: str
    content_path: str
    language_id: int
    author_id: int
