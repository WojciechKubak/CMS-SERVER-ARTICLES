from articles.infrastructure.db.entity import LanguageEntity
from articles.domain.model import Language


def test_from_domain() -> None:
    language_domain = Language(id_=1, name='Language', code='LANG')
    result = LanguageEntity.from_domain(language_domain)
    assert language_domain.id_ == result.id
    assert language_domain.name == result.name
    assert language_domain.code == result.code
