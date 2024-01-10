from articles.infrastructure.db.entity import ArticleEntity, CategoryEntity, TagEntity
from dataclasses import dataclass
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from sqlalchemy import Engine
from typing import Any, Callable
from functools import wraps


def transactional(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args: tuple[Any], **kwargs: dict[str, Any]):
        session = self.session_maker()
        try:
            result = method(self, session, *args, **kwargs)
            session.commit()
            return result
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    return wrapper


@dataclass
class CrudRepository:
    _engine: Engine
    _entity: Any

    def __post_init__(self) -> None:
        self.session_maker = scoped_session(sessionmaker(self._engine, expire_on_commit=False))

    @transactional
    def add(self, session: Session, item: Any) -> None:
        session.add(item)

    @transactional
    def update(self, session: Session, item: Any) -> None:
        session.merge(item)

    @transactional
    def delete(self, session: Session, id_: int) -> None:
        item = session.query(self._entity).filter_by(id=id_).first()
        session.delete(item)

    @transactional
    def find_by_id(self, session: Session, id_: int) -> Any | None:
        return session.query(self._entity).filter_by(id=id_).first()

    @transactional
    def find_all(self, session: Session) -> list[Any]:
        return session.query(self._entity).all()


@dataclass
class ArticleRepository(CrudRepository):
    _engine: Engine
    _entity: Any = ArticleEntity


@dataclass
class CategoryRepository(CrudRepository):
    _engine: Engine
    _entity: Any = CategoryEntity


@dataclass
class TagRepository(CrudRepository):
    _engine: Engine
    _entity: Any = TagEntity
