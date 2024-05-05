from articles.infrastructure.api.dto import CategoryDTO


def test_from_dto() -> None:
    category_dto = {
        'id_': 1,
        'name': 'name',
        'description': 'dummy'
    }
    result = CategoryDTO.from_dto(category_dto)
    assert category_dto['id_'] == result.id_
    assert category_dto['name'] == result.name
    assert category_dto['description'] == result.description
