from articles.domain.model import Category


def test_from_dto() -> None:
    category_dto = {
        'id': 1,
        'name': 'name',
        'description': 'dummy'
    }
    result = Category.from_dto(category_dto)
    assert category_dto['id'] == result.id_
    assert category_dto['name'] == result.name
    assert category_dto['description'] == result.description
