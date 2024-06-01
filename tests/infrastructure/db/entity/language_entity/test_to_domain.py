from tests.factory import LanguageEntityFactory


def test_to_domain() -> None:
    language = LanguageEntityFactory()
    result = language.to_domain()
    assert language.id == result.id_
    assert language.name == result.name
    assert language.code == result.code
