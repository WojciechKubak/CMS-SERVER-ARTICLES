from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from articles.infrastructure.persistance.entity import LanguageEntity
from tests.factory import LanguageEntityFactory, LanguageFactory


def test_update_language(language_db_adapter: LanguageDbAdapter) -> None:
    language_dao = LanguageEntityFactory()
    new_name = f"new_{language_dao.name}"
    language = LanguageFactory(name=new_name)

    result = language_db_adapter.update_language(language)

    assert LanguageEntity.query.filter_by(id=result.id_).first().name == new_name
