from articles.infrastructure.persistance.entity import (
    TranslationEntity,
    LanguageEntity,
    ArticleEntity
)
from tests.factory import TranslationFactory


def test_from_domain() -> None:
    translation = TranslationFactory()
    result = TranslationEntity.from_domain(translation)
    assert translation.id_ == result.id
    assert translation.content == result.content_path
    assert translation.is_ready == result.is_ready
    assert isinstance(result.language, LanguageEntity)
    assert isinstance(result.article, ArticleEntity)
