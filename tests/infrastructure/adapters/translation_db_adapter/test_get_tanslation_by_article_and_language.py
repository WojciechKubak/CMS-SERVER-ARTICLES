from articles.infrastructure.adapters.adapters import TranslationDbAdapter
from articles.infrastructure.db.entity import (
    ArticleEntity, 
    LanguageEntity, 
    TranslationEntity,
    CategoryEntity,
    TagEntity
)
from sqlalchemy.orm import Session


def test_get_translation_by_article_and_language_code(
        translation_db_adapter: TranslationDbAdapter, 
        db_session: Session
    ) -> None:
    db_session.bulk_save_objects([
        CategoryEntity(id=1, name='name', description='dummy'),
        TagEntity(id=1, name='name'),
        ArticleEntity(id=1, title='title', category_id=1),
        LanguageEntity(id=1, name='lang', code='C'),
        TranslationEntity(id=1, article_id=1, language_id=1),
    ])
    db_session.commit()
    assert translation_db_adapter.get_translation_by_article_and_language(1, 1)
