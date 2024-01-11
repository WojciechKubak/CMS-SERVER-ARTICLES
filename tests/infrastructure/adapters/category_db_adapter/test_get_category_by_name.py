from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session


class TestGetCategoryByName:

    def test_when_not_found(self, category_db_adapter: CategoryDbAdapter, db_session: Session) -> None:
        result = category_db_adapter.get_category_by_name('abcdef')
        assert not result
        assert not db_session.query(CategoryEntity).filter_by(name='abcdef').first()

    def test_when_found(self, category_db_adapter: CategoryDbAdapter, db_session: Session) -> None:
        db_session.add(CategoryEntity(id=1, name='name', description='dummy'))
        db_session.commit()
        result = category_db_adapter.get_category_by_name('name')
        assert 'name' == result.name
