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
    """
    Abstract base class for a CRUD repository.

    This class defines the interface for a CRUD repository. Subclasses
    should implement the abstract methods to provide the functionality for
    the specific type of repository.
    """

    @abstractmethod
    def add_or_update(self, entity: T) -> None:
        """
        Add a new entity or update an existing one.

        Args:
            entity (T): The entity to add or update.
        """
        pass

    @abstractmethod
    def find_by_id(self, entity_id: int) -> T | None:
        """
        Find an entity by its ID.

        Args:
            entity_id (int): The ID of the entity to find.

        Returns:
            T | None: The found entity or None if no entity was found.
        """
        pass

    @abstractmethod
    def find_all(self) -> list[T]:
        """
        Find all entities.

        Returns:
            list[T]: A list of all entities.
        """
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> None:
        """
        Delete an entity by its ID.

        Args:
            entity_id (int): The ID of the entity to delete.
        """
        pass


@dataclass
class CrudRepositoryORM[T: sa.Model](CrudRepository[T]):
    """
    Implementation of the CRUD repository for SQLAlchemy ORM.

    This class provides the functionality for a CRUD repository using
    SQLAlchemy ORM.

    Attributes:
        db (SQLAlchemy): The SQLAlchemy session.
    """

    db: SQLAlchemy

    def __post_init__(self):
        """
        Initialize the SQLAlchemy session and the entity type.
        """
        self.sa = self.db
        self.entity = self.__class__.__orig_bases__[0].__args__[0]

    def add_or_update(self, item: Any) -> Any:
        """
        Add a new item or update an existing one.

        Args:
            item (Any): The item to add or update.

        Returns:
            Any: The added or updated item.
        """
        return self.sa.session.merge(item)

    def delete(self, id_: int) -> None:
        """
        Delete an item by its ID.

        Args:
            id_ (int): The ID of the item to delete.
        """
        item = self.sa.session.query(self.entity).filter_by(id=id_).first()
        self.sa.session.delete(item)

    def find_by_id(self, id_: int) -> Any | None:
        """
        Find an item by its ID.

        Args:
            id_ (int): The ID of the item to find.

        Returns:
            Any | None: The found item or None if no item was found.
        """
        return self.sa.session.query(self.entity).filter_by(id=id_).first()

    def find_all(self) -> list[Any]:
        """
        Find all items.

        Returns:
            list[Any]: A list of all items.
        """
        return self.sa.session.query(self.entity).all()


@dataclass
class ArticleRepository(CrudRepositoryORM[ArticleEntity]):
    """
    Repository for ArticleEntity objects.

    This class provides additional methods to find ArticleEntity objects by
    title and category ID.
    """

    def find_by_title(self, title: str) -> ArticleEntity | None:
        """
        Find an ArticleEntity by its title.

        Args:
            title (str): The title of the ArticleEntity to find.

        Returns:
            ArticleEntity | None: The found ArticleEntity or None
            if no ArticleEntity was found.
        """
        return self.sa.session.query(self.entity) \
            .filter_by(title=title).first()

    def find_by_category_id(self, category_id: int) -> list[ArticleEntity]:
        """
        Find all ArticleEntity objects by category ID.

        Args:
            category_id (int): The category ID to find ArticleEntity
            objects by.

        Returns:
            list[ArticleEntity]: A list of found ArticleEntity objects.
        """
        return self.sa.session.query(self.entity).filter_by(
            category_id=category_id).all()


@dataclass
class CategoryRepository(CrudRepositoryORM[CategoryEntity]):
    """
    Repository for CategoryEntity objects.

    This class provides an additional method to find a CategoryEntity by name.
    """

    def find_by_name(self, name: str) -> CategoryEntity | None:
        """
        Find a CategoryEntity by its name.

        Args:
            name (str): The name of the CategoryEntity to find.

        Returns:
            CategoryEntity | None: The found CategoryEntity or None
            if no CategoryEntity was found.
        """
        return self.sa.session.query(self.entity).filter_by(name=name).first()


@dataclass
class TagRepository(CrudRepositoryORM[TagEntity]):
    """
    Repository for TagEntity objects.

    This class provides additional methods to find TagEntity objects by
    name and ID.
    """

    def find_by_name(self, name: str) -> CategoryEntity | None:
        """
        Find a TagEntity by its name.

        Args:
            name (str): The name of the TagEntity to find.

        Returns:
            TagEntity | None: The found TagEntity or None if no
            TagEntity was found.
        """
        return self.sa.session.query(self.entity).filter_by(name=name).first()

    def find_many_by_id(self, tags_id: list[int]) -> list[TagEntity]:
        """
        Find all TagEntity objects by their IDs.

        Args:
            tags_id (list[int]): The IDs to find TagEntity objects by.

        Returns:
            list[TagEntity]: A list of found TagEntity objects.
        """
        return self.sa.session.query(self.entity).filter(
            self.entity.id.in_(tags_id)).all()


@dataclass
class TranslationRepository(CrudRepositoryORM[TranslationEntity]):
    """
    Repository for TranslationEntity objects.

    This class provides an additional method to find a TranslationEntity by
    article ID and language ID.
    """

    def find_by_article_and_language(
        self,
        article_id: int,
        language_id: int
    ) -> TranslationEntity | None:
        """
        Find a TranslationEntity by its article ID and language ID.

        Args:
            article_id (int): The article ID of the TranslationEntity to find.
            language_id (int): The language ID of the TranslationEntity
            to find.

        Returns:
            TranslationEntity | None: The found TranslationEntity or None if
            no TranslationEntity was found.
        """
        return self.sa.session.query(self.entity).filter(
            self.entity.article_id == article_id,
            self.entity.language_id == language_id
        ).first()


@dataclass
class LanguageRepository(CrudRepositoryORM[LanguageEntity]):
    """
    Repository for LanguageEntity objects.

    This class provides an additional method to find a LanguageEntity by name.
    """

    def find_by_name(self, name: str) -> LanguageEntity | None:
        """
        Find a LanguageEntity by its name.

        Args:
            name (str): The name of the LanguageEntity to find.

        Returns:
            LanguageEntity | None: The found LanguageEntity or None if no
            LanguageEntity was found.
        """
        return self.sa.session.query(self.entity).filter_by(name=name).first()


article_repository = ArticleRepository(sa)
category_repository = CategoryRepository(sa)
tag_repository = TagRepository(sa)
language_repository = LanguageRepository(sa)
translation_repository = TranslationRepository(sa)
