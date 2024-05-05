from articles.infrastructure.db.entity import TranslationEntity, LanguageEntity, ArticleEntity
from articles.domain.model import Language, Article


def test_to_domain() -> None:
    translation_entity = TranslationEntity(
        id=1,
        content_path='content',
        language=LanguageEntity(id=1, name='Language', code='LANG'),
        is_ready=True,
        article=ArticleEntity(id=1, title='title')
    )
    result = translation_entity.to_domain()

    assert translation_entity.id == result.id_
    assert isinstance(result.language, Language)
    assert isinstance(result.article, Article)
