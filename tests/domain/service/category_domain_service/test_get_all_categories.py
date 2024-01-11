from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.db.entity import CategoryEntity
from sqlalchemy.orm import Session


def test_get_all_categories(category_db_adapter: CategoryDbAdapter, db_session: Session) -> None:
    categorys_dto = [CategoryEntity(name=''), CategoryEntity(name='')]
    db_session.bulk_save_objects(categorys_dto)
    db_session.commit()
    result = category_db_adapter.get_all_categories()
    assert len(categorys_dto) == len(result)
