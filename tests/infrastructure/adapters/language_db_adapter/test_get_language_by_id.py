from articles.infrastructure.adapters.adapters import LanguageDbAdapter
from tests.factory import LanguageEntityFactory


class TestGetLanguageById:

    def test_when_not_found(
            self,
            language_db_adapter: LanguageDbAdapter
    ) -> None:
        result = language_db_adapter.get_language_by_id(999)
        assert not result

    def test_when_found(self, language_db_adapter: LanguageDbAdapter) -> None:
        language = LanguageEntityFactory()
        result = language_db_adapter.get_language_by_id(language.id)
        assert language.id == result.id_
