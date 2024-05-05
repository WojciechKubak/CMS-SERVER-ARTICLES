from articles.infrastructure.api.dto import LanguageDTO


def test_from_dto() -> None:
    language_dto = {
        'id_': 1,
        'name': 'language',
        'code': 'LN'
    }
    result = LanguageDTO.from_dto(language_dto)
    assert language_dto['id_'] == result.id_
    assert language_dto['name'] == result.name
    assert language_dto['code'] == result.code
