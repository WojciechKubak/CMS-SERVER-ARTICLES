from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from tests.factory import LanguageEntityFactory


class TestGetLanguageByName:

    def test_when_not_found(self, language_db_adapter: LanguageDbAdapter) -> None:
        result = language_db_adapter.get_language_by_name("name")
        assert not result

    def test_when_found(self, language_db_adapter: LanguageDbAdapter) -> None:
        language = LanguageEntityFactory()
        result = language_db_adapter.get_language_by_name(language.name)
        assert language.name == result.name
