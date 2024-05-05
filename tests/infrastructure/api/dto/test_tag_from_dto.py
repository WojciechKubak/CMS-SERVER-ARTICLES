from articles.infrastructure.api.dto import TagDTO


def test_from_dto() -> None:
    tag_dto = {
        'id_': 1,
        'name': 'name',
    }
    result = TagDTO.from_dto(tag_dto)
    assert tag_dto['id_'] == result.id_
    assert tag_dto['name'] == result.name
