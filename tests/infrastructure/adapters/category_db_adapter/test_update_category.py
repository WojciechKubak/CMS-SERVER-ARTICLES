from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from articles.infrastructure.persistance.entity import CategoryEntity
from tests.factory import CategoryEntityFactory, CategoryFactory


def test_update_category(category_db_adapter: CategoryDbAdapter) -> None:
    category_dao = CategoryEntityFactory()
    new_name = f'new_{category_dao.name}'
    category = CategoryFactory(name=new_name)

    result = category_db_adapter.update_category(category)

    assert CategoryEntity.query.filter_by(id=result.id_).first().name \
        == new_name
