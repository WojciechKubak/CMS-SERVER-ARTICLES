from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session


class TestGetCategoryById:

    def test_when_not_found(self, category_db_adapter: CategoryDbAdapter, db_session: Session) -> None:
        result = category_db_adapter.get_category_by_id(1111)
        assert not result
        assert not db_session.query(CategoryEntity).filter_by(id=1111).first()

    def test_when_found(self, category_db_adapter: CategoryDbAdapter, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name', description='dummy'))
        db_session.commit()
        result = category_db_adapter.get_category_by_id(1)
        assert 1 == result.id_
