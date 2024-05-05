from articles.domain.model import Category, Tag, Article, Language
from dataclasses import dataclass
from typing import Any, Self


@dataclass
class CategoryDTO:
    id_: int | None
    name: str
    description: str | None

    def to_domain(self) -> Category:
        return Category(**self.__dict__)

    @classmethod
    def from_dto(cls, data: dict[str, Any]) -> Self:
        return cls(
            id_=data.get('id_', None),
            name=data['name'],
            description=data.get('description', None)
        )


@dataclass
class TagDTO:
    id_: int | None
    name: str

    def to_domain(self) -> Tag:
        return Tag(**self.__dict__)

    @classmethod
    def from_dto(cls, data: dict[str, Any]) -> Self:
        return cls(
            id_=data.get('id_', None),
            name=data['name'],
        )


@dataclass
class LanguageDTO:
    id_: int | None
    name: str
    code: str

    def to_domain(self) -> Language:
        return Language(**self.__dict__)

    @classmethod
    def from_dto(cls, data: dict[str, Any]) -> Self:
        return cls(
            id_=data.get('id_', None),
            name=data['name'],
            code=data['code']
        )


@dataclass
class ArticleDTO:
    id_: int | None
    title: str
    content: str
    category_id: int
    tags_id: list[int]

    def to_domain(self) -> Article:
        return Article(
            id_=self.id_,
            title=self.title,
            content=self.content,
            category=self.category_id,
            tags=self.tags_id,
        )

    @classmethod
    def from_dto(cls, data: dict[str, Any]) -> Article:
        return cls(
            id_=data.get('id_', None),
            title=data['title'],
            content=data['content'],
            category_id=data['category_id'],
            tags_id=list(set(data['tags_id']))
        )
