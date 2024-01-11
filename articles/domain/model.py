from dataclasses import dataclass
from typing import Any


@dataclass
class Category:
    id_: int
    name: str
    description: str

    @classmethod
    def from_dto(cls, data: dict[str, Any]) -> 'Category':
        return cls(
            id_=data.get('id'),
            name=data.get('name'),
            description=data.get('description')
        )


@dataclass
class Tag:
    id_: int
    name: str

    @classmethod
    def from_dto(cls, data: dict[str, Any]) -> 'Tag':
        return cls(
            id_=data.get('id'),
            name=data.get('name')
        )


@dataclass
class Article:
    id_: int
    title: str
    content: str
    category: Category
    tags: list[Tag]

    def with_category_and_tags(self, category: Category, tags: list[Tag]) -> 'Article':
        return Article(
            id_=self.id_,
            title=self.title,
            content=self.content,
            category=category,
            tags=tags
        )

    @classmethod
    def from_dto(cls, data: dict[str, Any]) -> 'Article':
        return cls(
            id_=data.get('id'),
            title=data.get('title'),
            content=data.get('content'),
            category=Category.from_dto({'id': data.get('category_id')}),
            tags=[Tag.from_dto({'id': id_}) for id_ in data.get('tags_id')]
        )
