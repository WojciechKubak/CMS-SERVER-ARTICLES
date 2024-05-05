from articles.infrastructure.adapters.adapters import TranslationDbAdapter
from articles.infrastructure.db.entity import (
    ArticleEntity, 
    LanguageEntity, 
    TranslationEntity,
    CategoryEntity,
    TagEntity
)
from articles.domain.model import Translation, Article, Language, Tag, Category
from sqlalchemy.orm import Session


def test_save_translation(translation_db_adapter: TranslationDbAdapter, db_session: Session) -> None:
    db_session.bulk_save_objects([
        CategoryEntity(id=1, name='name', description='dummy'),
        TagEntity(id=1, name='name'),
        ArticleEntity(id=1, title='title', category_id=1),
        LanguageEntity(id=1, name='lang', code='C'),
    ])
    db_session.commit()
    article = Article(
        id_=1,
        title='title',
        content='dummy',
        category=Category(id_=1, name='name', description='dummy'),
        tags=[Tag(id_=1, name='name')]
    )
    translation = Translation(
        id_=1, 
        content='content',
        is_ready=True,
        article=article,
        language=Language(id_=1, name='name', code='C')
    )
    result = translation_db_adapter.save_translation(translation)
    assert translation == result
    assert db_session.query(TranslationEntity).filter_by(id=1).first()
