from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.persistance.entity import LanguageEntity
from tests.factory import LanguageFactory


def test_save_language(language_db_adapter: LanguageDbAdapter) -> None:
    language = LanguageFactory()
    result = language_db_adapter.save_language(language)
    assert LanguageEntity.query.filter_by(id=result.id_).first()
