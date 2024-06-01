from articles.domain.model import Category, Tag, Article, Language, Translation
from dataclasses import dataclass
from typing import Any, Self
from abc import ABC


@dataclass
class CategoryBase(ABC):
    name: str
    description: str | None


@dataclass
class CategoryDTO(CategoryBase):
    id_: int

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
        }

    @classmethod
    def from_domain(cls, category: Category) -> None:
        return cls(
            id_=category.id_,
            name=category.name,
            description=category.description
        )


@dataclass
class CategoryCreateDTO(CategoryBase):
    pass

    def to_domain(self) -> Category:
        return Category(id_=None, **self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> None:
        return cls(
            name=data['name'],
            description=data.get('description', None)
        )


@dataclass
class CategoryUpdateDTO(CategoryBase):
    id_: int

    def to_domain(self) -> Category:
        return Category(**self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> None:
        return cls(
            id_=data['id'],
            name=data['name'],
            description=data.get('description', None)
        )


@dataclass
class TagBase(ABC):
    name: str


@dataclass
class TagDTO(TagBase):
    id_: int

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
        }

    @classmethod
    def from_domain(cls, tag: Tag) -> Tag:
        return cls(
            id_=tag.id_,
            name=tag.name
        )


@dataclass
class TagCreateDTO(TagBase):
    pass

    def to_domain(self) -> Tag:
        return Tag(id_=None, **self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            name=data['name']
        )


@dataclass
class TagUpdateDTO(TagBase):
    id_: int

    def to_domain(self) -> Tag:
        return Tag(**self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            id_=data['id'],
            name=data['name']
        )


@dataclass
class LanguageBase(ABC):
    name: str
    code: str


@dataclass
class LanguageDTO(LanguageBase):
    id_: int

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'name': self.name,
            'code': self.code
        }

    @classmethod
    def from_domain(cls, language: Language) -> Self:
        return cls(
            id_=language.id_,
            name=language.name,
            code=language.code
        )


@dataclass
class LanguageCreateDTO(LanguageBase):
    pass

    def to_domain(self) -> Language:
        return Language(id_=None, **self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            name=data['name'],
            code=data['code']
        )


@dataclass
class LanguageUpdateDTO(LanguageBase):
    id_: int

    def to_domain(self) -> Language:
        return Language(**self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            id_=data['id'],
            name=data['name'],
            code=data['code']
        )


@dataclass
class ArticleBase(ABC):
    title: str


@dataclass
class ArticleDTO(ArticleBase):
    id_: int
    content: str
    category: CategoryDTO
    tags: list[TagDTO]

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'content': self.content,
            'title': self.title,
            'category': self.category.to_dict(),
            'tags': [tag.to_dict() for tag in self.tags],
        }

    @classmethod
    def from_domain(cls, article: Article) -> Self:
        return cls(
            id_=article.id_,
            title=article.title,
            content=article.content,
            category=article.category,
            tags=article.tags
        )


@dataclass
class ArticleListDTO(ArticleBase):
    id_: int
    category: CategoryDTO
    tags: list[TagDTO]

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category.to_dict(),
            'tags': [tag.to_dict() for tag in self.tags],
        }

    @classmethod
    def from_domain(cls, article: Article) -> Self:
        return cls(
            id_=article.id_,
            title=article.title,
            category=article.category,
            tags=article.tags
        )


@dataclass
class ArticleCreateDTO(ArticleBase):
    content: str
    category_id: int
    tags_id: list[int]

    def to_domain(self) -> Article:
        return Article(
            id_=None,
            title=self.title,
            content=self.content,
            category=self.category_id,
            tags=list(set(self.tags_id))
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            title=data['title'],
            content=data['content'],
            category_id=data['category_id'],
            tags_id=data['tags_id']
        )


@dataclass
class ArticleUpdateDTO(ArticleBase):
    id_: int
    content: str
    category_id: int
    tags_id: list[int]

    def to_domain(self) -> Article:
        return Article(
            id_=self.id_,
            title=self.title,
            content=self.content,
            category=self.category_id,
            tags=list(set(self.tags_id))
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(
            id_=data['id'],
            title=data['title'],
            content=data['content'],
            category_id=data['category_id'],
            tags_id=data['tags_id']
        )


@dataclass
class TranslationDTO:
    id_: int
    language: LanguageDTO
    article: ArticleDTO
    title: str
    content: str

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id_,
            'language': self.language.to_dict(),
            'article': self.article.to_dict(),
            'title': self.title,
            'content': self.content
        }

    @classmethod
    def from_domain(cls, translation: Translation) -> Self:
        return cls(
            id_=translation.id_,
            language=translation.language,
            article=translation.article,
            title=translation.title,
            content=translation.content
        )
