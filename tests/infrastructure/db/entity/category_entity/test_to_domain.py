from tests.factory import CategoryEntityFactory


def test_to_domain() -> None:
    category = CategoryEntityFactory()
    result = category.to_domain()
    assert category.id == result.id_
    assert category.name == result.name
    assert category.description == result.description
