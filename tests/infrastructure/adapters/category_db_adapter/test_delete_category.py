from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.persistance.entity import CategoryEntity
from tests.factory import CategoryEntityFactory


def test_delete_category(category_db_adapter: CategoryDbAdapter) -> None:
    category = CategoryEntityFactory()
    category_db_adapter.delete_category(category.id)
    assert not CategoryEntity.query.filter_by(id=category.id).first()
