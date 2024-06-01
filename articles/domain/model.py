from dataclasses import dataclass
from typing import Self


@dataclass
class Category:
    id_: int | None
    name: str
    description: str | None


@dataclass
class Tag:
    id_: int | None
    name: str


@dataclass
class Language:
    id_: int | None
    name: str
    code: str


@dataclass
class Article:
    id_: int | None
    title: str
    content: str
    category: Category | int
    tags: list[Tag] | list[int]

    def change_category_and_tags(
            self,
            category: Category,
            tags: list[Tag]
    ) -> Self:
        return self.__class__(
            id_=self.id_,
            title=self.title,
            content=self.content,
            category=category,
            tags=tags,
        )

    def change_content(self, content: str) -> Self:
        return self.__class__(
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
    content: str
    is_ready: bool
    article: Article

    def publish(self, content_path: str) -> Self:
        return self.__class__(
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
