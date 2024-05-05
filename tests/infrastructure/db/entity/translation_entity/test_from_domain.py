from articles.infrastructure.db.entity import TranslationEntity, ArticleEntity, LanguageEntity
from articles.domain.model import Translation, Language, Article, Category


def test_from_domain() -> None:
    langauge = Language(id_=1, name='Language', code='LANG')
    article = Article(id_=1, title='title', content='dummy', category=Category(id_=1, name='', description=''), tags=[])
    translation_domain = Translation(
        id_=1, 
        language=langauge,
        content='content',
        is_ready=True,
        article=article,
    )
    result = TranslationEntity.from_domain(translation_domain)
    assert translation_domain.id_ == result.id
    assert isinstance(result.article, ArticleEntity)
    assert isinstance(result.language, LanguageEntity)
