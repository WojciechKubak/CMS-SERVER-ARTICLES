from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity, TagEntity
from articles.infrastructure.db.entity import Base
from dataclasses import dataclass
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Engine
from typing import Any, Callable
from functools import wraps
from abc import ABC, abstractmethod


def transactional(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args: tuple[Any], **kwargs: dict[str, Any]):
        self.session = self.session_maker()
        try:
            result = method(self, *args, **kwargs)
            self.session.commit()
            return result
        except Exception:
            self.session.rollback()
            raise
        finally:
            self.session.close()
            self.session = None

    return wrapper

    
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
class CrudRepositoryORM[T: Base](CrudRepository[T]):
    engine: Engine

    def __post_init__(self):
        self.session_maker = scoped_session(
            sessionmaker(self.engine, expire_on_commit=False)
        )
        self.entity = self.__class__.__orig_bases__[0].__args__[0]

    @transactional
    def add_or_update(self, item: Any) -> Any:
        return self.session.merge(item)

    @transactional
    def delete(self, id_: int) -> None:
        item = self.session.query(self.entity).filter_by(id=id_).first()
        self.session.delete(item)

    @transactional
    def find_by_id(self, id_: int) -> Any | None:
        return self.session.query(self.entity).filter_by(id=id_).first()

    @transactional
    def find_all(self) -> list[Any]:
        return self.session.query(self.entity).all()


@dataclass
class ArticleRepository(CrudRepositoryORM[ArticleEntity]):

    @transactional
    def find_by_title(self, title: str) -> ArticleEntity | None:
        return self.session.query(self.entity).filter_by(title=title).first()

    @transactional
    def find_by_category_id(self, category_id: int) -> list[ArticleEntity]:
        return self.session.query(self.entity).filter_by(category_id=category_id).all()


@dataclass
class CategoryRepository(CrudRepositoryORM[CategoryEntity]):

    @transactional
    def find_by_name(self, name: str) -> CategoryEntity | None:
        return self.session.query(self.entity).filter_by(name=name).first()


@dataclass
class TagRepository(CrudRepositoryORM[TagEntity]):

    @transactional
    def find_by_name(self, name: str) -> CategoryEntity | None:
        return self.session.query(self.entity).filter_by(name=name).first()

    @transactional
    def find_many_by_id(self, ids: list[int]) -> list[TagEntity]:
        return self.session.query(self.entity).filter(self.entity.id.in_(ids)).all()
