from dataclasses import dataclass
from typing import Any, Self


@dataclass
class Category:
    id_: int | None
    name: str
    description: str | None

    def to_json(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
            'description': self.description
        }


@dataclass
class Tag:
    id_: int | None
    name: str

    def to_json(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
        }


@dataclass
class Language:
    id_: int | None
    name: str
    code: str

    def to_json(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
            'code': self.code
        }


@dataclass
class Article:
    id_: int | None
    title: str
    content: str
    category: Category | int
    tags: list[Tag | int]

    def to_json(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'title': self.title,
            'content': self.content,
            'category': self.category.to_json(),
            'tags': [tag.to_json() for tag in self.tags],
        }

    def change_category_and_tags(self, category: Category, tags: list[Tag]) -> Self:
        return Article(
            id_=self.id_,
            title=self.title,
            content=self.content,
            category=category,
            tags=tags,
        )
    
    def change_content(self, content: str) -> Self:
        return Article(
            id_=self.id_,
            title=self.title,
            content=content,
            category=self.category,
            tags=self.tags,
        )


@dataclass
class Translation:
    id_: int | None
    language: Language
    content: str | None
    is_ready: bool
    article: Article

    def to_json(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'content': self.content,
            'language': self.language.to_json(),
            'is_ready': self.is_ready,
        }
    
    def publish(self, content_path: str) -> Self:
        return Translation(
            id_=self.id_,
            content=content_path,
            language=self.language,
            is_ready=True,
            article=self.article
        )

    @classmethod
    def create_request(cls, language: Language, article: Article) -> Self:
        return cls(
            id_=None,
            content=None,
            language=language,
            is_ready=False,
            article=article
        )
