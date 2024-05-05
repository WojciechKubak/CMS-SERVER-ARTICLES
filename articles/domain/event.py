from articles.domain.model import Article, Language
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Self


@dataclass
class ArticleTranslationEvent:
    article_id: int
    content_path: str
    language_id: int
    date: datetime

    def to_json(self) -> dict[str, Any]:
        return {
            'article_id': self.article_id,
            'content_path': self.content_path,
            'language_id': self.language_id,
            'date': self.date
        }

    @classmethod
    def from_domain(cls, article: Article, language: Language) -> Self:
        return cls(
            article_id=article.id_,
            content_path=article.content,
            language_id=language.id_,
            date=datetime.now()
        )


@dataclass
class ArticleTranslatedEvent:
    article_id: int
    language_id: int
    content_path: str
    date: datetime

    def to_json(self) -> dict[str, Any]:
        return {
            'article_id': self.article_id,
            'content_path': self.content_path,
            'language_id': self.language_id,
            'date': self.date
        }
