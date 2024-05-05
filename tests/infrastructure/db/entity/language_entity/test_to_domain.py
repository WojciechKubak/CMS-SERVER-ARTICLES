from articles.infrastructure.db.entity import LanguageEntity


def test_to_domain() -> None:
    language_entity = LanguageEntity(id=1, name='Language', code='LANG')
    result = language_entity.to_domain()
    assert language_entity.id == result.id_
    assert language_entity.name == result.name
    assert language_entity.code == result.code
