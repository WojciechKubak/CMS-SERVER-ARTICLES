from articles.infrastructure.persistance.entity import CategoryEntity
from tests.factory import CategoryFactory


def test_from_domain() -> None:
    category = CategoryFactory()
    result = CategoryEntity.from_domain(category)
    assert category.id_ == result.id
    assert category.name == result.name
    assert category.description == result.description
