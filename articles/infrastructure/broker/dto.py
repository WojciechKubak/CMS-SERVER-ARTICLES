from articles.domain.event import ArticleTranslatedEvent
from dataclasses import dataclass
from typing import Any, Self
from datetime import datetime


@dataclass
class TranslatedArticleDTO:
    article_id: int
    language_id: int
    translation_path: str
    translation_date: datetime
    author: str

    def to_domain(self) -> ArticleTranslatedEvent:
        return ArticleTranslatedEvent(
            article_id=self.article_id,
            language_id=self.language_id,
            content_path=self.translation_path,
            date=self.translation_date
        )
    
    @classmethod
    def from_dto(cls, data: dict[str, Any]) -> Self:
        return cls(
            article_id=data['article_id'],
            language_id=data['language_id'],
            translation_path=data['translation_path'],
            translation_date=data['translation_date'],
            author=data['author']
        )
