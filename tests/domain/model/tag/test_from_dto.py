from articles.domain.model import Tag


def test_from_dto() -> None:
    tag_dto = {
        'id': 1,
        'name': 'name',
    }
    result = Tag.from_dto(tag_dto)
    assert tag_dto['id'] == result.id_
    assert tag_dto['name'] == result.name
