from articles.infrastructure.persistance.entity import (
    ArticleEntity,
    CategoryEntity,
    TagEntity,
    LanguageEntity,
    TranslationEntity
)
from articles.infrastructure.persistance.configuration import sa
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any


@dataclass
class CrudRepository[T](ABC):

    @abstractmethod
    def add_or_update(self, entity: T) -> None:
        pass

    @abstractmethod
    def find_by_id(self, entity_id: int) -> T | None:
        pass

    @abstractmethod
    def find_all(self) -> list[T]:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> None:
        pass


@dataclass
class CrudRepositoryORM[T: sa.Model](CrudRepository[T]):
    db: SQLAlchemy

    def __post_init__(self):
        self.sa = self.db
        self.entity = self.__class__.__orig_bases__[0].__args__[0]

    def add_or_update(self, item: Any) -> Any:
        return self.sa.session.merge(item)

    def delete(self, id_: int) -> None:
        item = self.sa.session.query(self.entity).filter_by(id=id_).first()
        self.sa.session.delete(item)

    def find_by_id(self, id_: int) -> Any | None:
        return self.sa.session.query(self.entity).filter_by(id=id_).first()

    def find_all(self) -> list[Any]:
        return self.sa.session.query(self.entity).all()


@dataclass
class ArticleRepository(CrudRepositoryORM[ArticleEntity]):

    def find_by_title(self, title: str) -> ArticleEntity | None:
        return self.sa.session.query(self.entity) \
            .filter_by(title=title).first()

    def find_by_category_id(self, category_id: int) -> list[ArticleEntity]:
        return self.sa.session.query(self.entity).filter_by(
            category_id=category_id).all()


@dataclass
class CategoryRepository(CrudRepositoryORM[CategoryEntity]):

    def find_by_name(self, name: str) -> CategoryEntity | None:
        return self.sa.session.query(self.entity).filter_by(name=name).first()


@dataclass
class TagRepository(CrudRepositoryORM[TagEntity]):

    def find_by_name(self, name: str) -> CategoryEntity | None:
        return self.sa.session.query(self.entity).filter_by(name=name).first()

    def find_many_by_id(self, tags_id: list[int]) -> list[TagEntity]:
        return self.sa.session.query(self.entity).filter(
            self.entity.id.in_(tags_id)).all()


@dataclass
class TranslationRepository(CrudRepositoryORM[TranslationEntity]):

    def find_by_article_and_language(
        self,
        article_id: int,
        language_id: int
    ) -> TranslationEntity | None:
        return self.sa.session.query(self.entity).filter(
            self.entity.article_id == article_id,
            self.entity.language_id == language_id
        ).first()


@dataclass
class LanguageRepository(CrudRepositoryORM[LanguageEntity]):

    def find_by_name(self, name: str) -> LanguageEntity | None:
        return self.sa.session.query(self.entity).filter_by(name=name).first()


article_repository = ArticleRepository(sa)
category_repository = CategoryRepository(sa)
tag_repository = TagRepository(sa)
language_repository = LanguageRepository(sa)
translation_repository = TranslationRepository(sa)
