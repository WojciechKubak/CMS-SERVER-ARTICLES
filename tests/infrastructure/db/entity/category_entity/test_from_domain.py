from articles.infrastructure.db.entity import CategoryEntity
from articles.domain.model import Category


def test_from_domain() -> None:
    category = Category(id_=1, name='name', description='dummy')
    result = CategoryEntity.from_domain(category)
    assert category.id_ == result.id
    assert category.name == result.name
