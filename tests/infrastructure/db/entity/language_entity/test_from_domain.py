from articles.infrastructure.persistance.entity import LanguageEntity
from tests.factory import LanguageFactory


def test_from_domain() -> None:
    language = LanguageFactory()
    result = LanguageEntity.from_domain(language)
    assert language.id_ == result.id
    assert language.name == result.name
    assert language.code == result.code
