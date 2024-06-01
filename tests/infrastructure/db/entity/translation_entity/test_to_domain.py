from articles.domain.model import Language, Article
from tests.factory import TranslationEntityFactory


def test_to_domain() -> None:
    translation = TranslationEntityFactory()
    result = translation.to_domain()
    assert translation.id == result.id_
    assert translation.content_path == result.content
    assert translation.is_ready == result.is_ready
    assert isinstance(result.language, Language)
    assert isinstance(result.article, Article)
