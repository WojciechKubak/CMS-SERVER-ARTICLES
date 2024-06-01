from articles.infrastructure.adapters.adapters import CategoryDbAdapter
from tests.factory import CategoryEntityFactory


def test_get_all_categories(category_db_adapter: CategoryDbAdapter) -> None:
    categories = CategoryEntityFactory.create_batch(5)
    result = category_db_adapter.get_all_categories()
    assert len(categories) == len(result)
