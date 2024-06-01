from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.persistance.entity import CategoryEntity
from tests.factory import CategoryFactory


def test_save_category(category_db_adapter: CategoryDbAdapter) -> None:
    category = CategoryFactory()
    result = category_db_adapter.save_category(category)
    assert CategoryEntity.query.filter_by(id=result.id_).first()
