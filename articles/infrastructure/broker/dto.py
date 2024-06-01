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
    article_id: int
    title: str
    content_path: str
    language_id: int
    date: datetime

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.article_id,
            'title': self.title,
            'content_path': self.content_path,
            'language_id': self.language_id,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S')
        }

    @classmethod
    def from_domain(cls, event: TranslationRequestEvent) -> Self:
        return cls(
            article_id=event.article_id,
            title=event.title,
            content_path=event.content_path,
            language_id=event.language_id,
            date=event.date
        )


@dataclass
class LanguageChangeEvent:
    id_: int
    name: str
    code: str
    event_type: LanguageEventType

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
            'code': self.code,
            'event_type': self.event_type.value
        }

    @classmethod
    def from_domain(cls, event: LanguageEvent) -> Self:
        return cls(
            id_=event.id_,
            name=event.name,
            code=event.code,
            event_type=event.event_type
        )


@dataclass
class TranslatedArticleDTO:
    article_id: int
    title: str
    content_path: str
    language_id: int
    author_id: str

    def to_domain(self) -> ArticleTranslatedEvent:
        return ArticleTranslatedEvent(
            article_id=self.article_id,
            title=self.title,
            content_path=self.content_path,
            language_id=self.language_id,
            author_id=self.author_id
        )

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> Self:
        return cls(
            article_id=data['id'],
            title=data['title'],
            language_id=data['language_id'],
            content_path=data['content_path'],
            author_id=data['translator_id']
        )
