from articles.infrastructure.persistance.repository import CategoryRepository
from tests.factory import CategoryEntityFactory


def test_find_by_name(category_repository: CategoryRepository) -> None:
    category = CategoryEntityFactory()
    result = category_repository.find_by_name(category.name)
    assert category == result
