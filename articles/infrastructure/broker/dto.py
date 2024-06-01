from articles.domain.event import (
    ArticleTranslatedEvent,
    TranslationRequestEvent,
    LanguageEvent,
    LanguageEventType
)
from dataclasses import dataclass
from typing import Any, Self
from datetime import datetime


@dataclass
class TranslationRequestDTO:
    """
    Data Transfer Object for translation requests.

    This class provides methods to convert to a dictionary and to create
    an instance from a domain event.

    Attributes:
        article_id (int): The ID of the article.
        title (str): The title of the article.
        content_path (str): The path to the content of the article.
        language_id (int): The ID of the language.
        date (datetime): The date of the request.
    """

    article_id: int
    title: str
    content_path: str
    language_id: int
    date: datetime

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the DTO to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the DTO.
        """
        return {
            'id': self.article_id,
            'title': self.title,
            'content_path': self.content_path,
            'language_id': self.language_id,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S')
        }

    @classmethod
    def from_domain(cls, event: TranslationRequestEvent) -> Self:
        """
        Create a DTO from a domain event.

        Args:
            event (TranslationRequestEvent): The domain event.

        Returns:
            TranslationRequestDTO: The created DTO.
        """
        return cls(
            article_id=event.article_id,
            title=event.title,
            content_path=event.content_path,
            language_id=event.language_id,
            date=event.date
        )


@dataclass
class LanguageChangeEvent:
    """
    Data Transfer Object for language change events.

    This class provides methods to convert to a dictionary and to create an
    instance from a domain event.

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

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the DTO to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the DTO.
        """
        return {
            'id': self.id_,
            'name': self.name,
            'code': self.code,
            'event_type': self.event_type.value
        }

    @classmethod
    def from_domain(cls, event: LanguageEvent) -> Self:
        """
        Create a DTO from a domain event.

        Args:
            event (LanguageEvent): The domain event.

        Returns:
            LanguageChangeEvent: The created DTO.
        """
        return cls(
            id_=event.id_,
            name=event.name,
            code=event.code,
            event_type=event.event_type
        )


@dataclass
class TranslatedArticleDTO:
    """
    Data Transfer Object for translated articles.

    This class provides methods to convert to a domain event and to create an
    instance from a JSON object.

    Attributes:
        article_id (int): The ID of the article.
        title (str): The title of the article.
        content_path (str): The path to the content of the article.
        language_id (int): The ID of the language.
        author_id (str): The ID of the author.
    """

    article_id: int
    title: str
    content_path: str
    language_id: int
    author_id: str

    def to_domain(self) -> ArticleTranslatedEvent:
        """
        Convert the DTO to a domain event.

        Returns:
            ArticleTranslatedEvent: The domain event.
        """
        return ArticleTranslatedEvent(
            article_id=self.article_id,
            title=self.title,
            content_path=self.content_path,
            language_id=self.language_id,
            author_id=self.author_id
        )

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Self:
        """
        Create a DTO from a JSON object.

        Args:
            data (dict[str, Any]): The JSON object.

        Returns:
            TranslatedArticleDTO: The created DTO.
        """
        return cls(
            article_id=data['id'],
            title=data['title'],
            language_id=data['language_id'],
            content_path=data['content_path'],
            author_id=data['translator_id']
        )
