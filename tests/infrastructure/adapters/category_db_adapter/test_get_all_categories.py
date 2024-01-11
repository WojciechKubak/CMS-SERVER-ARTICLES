from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session


def test_get_all_categories(category_db_adapter: CategoryDbAdapter, db_session: Session) -> None:
    categories_dto = [CategoryEntity(name='name', description='dummy'), CategoryEntity(name='name', description='dummy')]
    db_session.bulk_save_objects(categories_dto)
    db_session.commit()
    result = category_db_adapter.get_all_categories()
    assert len(categories_dto) == len(result)
