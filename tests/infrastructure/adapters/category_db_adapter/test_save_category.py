from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.db.entity import CategoryEntity
from articles.domain.model import Category
from sqlalchemy.orm import Session


def test_save_category(category_db_adapter: CategoryDbAdapter, db_session: Session) -> None:
    category = Category(id_=1, name='name', description='dummy')
    result = category_db_adapter.save_category(category)
    assert category == result
    assert db_session.query(CategoryEntity).filter_by(id=1).first()
