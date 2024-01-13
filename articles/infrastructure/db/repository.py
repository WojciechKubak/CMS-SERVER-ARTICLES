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

    @transactional
    def add(self, session: Session, item: ArticleEntity) -> ArticleEntity:
        return session.merge(item)

    @transactional
    def find_by_title(self, session: Session, title: str) -> ArticleEntity | None:
        return session.query(self._entity).filter_by(title=title).first()

    @transactional
    def find_by_category_id(self, session: Session, category_id: int) -> list[ArticleEntity]:
        return session.query(self._entity).filter_by(category_id=category_id).all()


@dataclass
class CategoryRepository(CrudRepository):
    _engine: Engine
    _entity: Any = CategoryEntity

    @transactional
    def find_by_name(self, session: Session, name: str) -> CategoryEntity | None:
        return session.query(self._entity).filter_by(name=name).first()


@dataclass
class TagRepository(CrudRepository):
    _engine: Engine
    _entity: Any = TagEntity

    @transactional
    def find_by_name(self, session: Session, name: str) -> CategoryEntity | None:
        return session.query(self._entity).filter_by(name=name).first()

    @transactional
    def find_many_by_id(self, session: Session, ids: list[int]) -> list[TagEntity]:
        return session.query(self._entity).filter(self._entity.id.in_(ids)).all()
