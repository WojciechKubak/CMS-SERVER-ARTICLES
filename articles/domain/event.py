from articles.domain.model import Article, Language
from dataclasses import dataclass
from datetime import datetime
from typing import Self
from enum import Enum


class LanguageEventType(Enum):
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'


@dataclass
class TranslationRequestEvent:
    article_id: int
    title: str
    content_path: str
    language_id: int
    date: datetime

    @classmethod
    def from_domain(cls, article: Article, language: Language) -> Self:
        return cls(
            article_id=article.id_,
            title=article.title,
            content_path=article.content,
            language_id=language.id_,
            date=datetime.now()
        )


@dataclass
class ArticleTranslatedEvent:
    article_id: int
    title: str
    content_path: str
    language_id: int
    author_id: int


@dataclass
class LanguageEvent:
    id_: int
    name: str
    code: str
    event_type: LanguageEventType

    @classmethod
    def from_domain(cls, language: Language, event_type: LanguageEventType) -> Self:
        return cls(
            id_=language.id_,
            name=language.name,
            code=language.code,
            event_type=event_type
        )
