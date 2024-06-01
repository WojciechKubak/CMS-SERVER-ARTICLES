from articles.infrastructure.persistance.repository import \
    TranslationRepository
from tests.factory import TranslationEntityFactory


def test_find_by_article_and_language(
        translation_repository: TranslationRepository
) -> None:
    translation = TranslationEntityFactory()
    result = translation_repository.find_by_article_and_language(
        translation.article_id,
        translation.language_id
    )
    assert translation == result
