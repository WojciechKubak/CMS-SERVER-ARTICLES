from articles.infrastructure.adapters.adapters import TranslationDbAdapter
from tests.factory import TranslationEntityFactory


class TestGetTranslationById:

    def test_when_not_found(self, translation_db_adapter: TranslationDbAdapter) -> None:
        result = translation_db_adapter.get_translation_by_id(999)
        assert not result

    def test_when_found(self, translation_db_adapter: TranslationDbAdapter) -> None:
        translation = TranslationEntityFactory()

        result = translation_db_adapter.get_translation_by_id(translation.id)

        assert translation.id == result.id_
