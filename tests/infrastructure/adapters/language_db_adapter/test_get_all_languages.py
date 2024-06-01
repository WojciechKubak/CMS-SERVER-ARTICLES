from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from tests.factory import LanguageEntityFactory


def test_get_all_languages(language_db_adapter: LanguageDbAdapter) -> None:
    languages = LanguageEntityFactory.create_batch(5)
    result = language_db_adapter.get_all_languages()
    assert len(languages) == len(result)
