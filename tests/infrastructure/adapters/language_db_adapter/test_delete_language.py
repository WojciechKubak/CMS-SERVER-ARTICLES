from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.persistance.entity import LanguageEntity
from tests.factory import LanguageEntityFactory


def test_delete_language(language_db_adapter: LanguageDbAdapter) -> None:
    language = LanguageEntityFactory()
    language_db_adapter.delete_language(language.id)
    assert not LanguageEntity.query.filter_by(id=language.id).first()
