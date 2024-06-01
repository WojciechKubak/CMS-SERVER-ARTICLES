from articles.infrastructure.adapters.adapters import TranslationDbAdapter
from tests.factory import TranslationEntityFactory


def test_get_translation_by_article_and_language_code(
        translation_db_adapter: TranslationDbAdapter,
) -> None:
    translation = TranslationEntityFactory()

    result = translation_db_adapter.get_translation_by_article_and_language(
        translation.article.id,
        translation.language.id,
    )

    assert translation.id == result.id_
