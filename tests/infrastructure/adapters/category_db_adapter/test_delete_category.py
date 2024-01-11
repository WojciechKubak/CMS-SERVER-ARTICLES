from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session


def test_delete_category(category_db_adapter: CategoryDbAdapter, db_session: Session) -> None:
    db_session.add(CategoryEntity(id=1, name='name', description='dummy'))
    db_session.commit()
    category_db_adapter.delete_category(1)
    assert not db_session.query(CategoryEntity).filter_by(id=1).first()
