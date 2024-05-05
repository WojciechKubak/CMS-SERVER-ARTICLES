from articles.infrastructure.db.entity import TranslationEntity, ArticleEntity, LanguageEntity
from articles.infrastructure.db.repository import TranslationRepository
from sqlalchemy.orm import Session


def test_find_by_article_and_language(db_session: Session, translation_repository: TranslationRepository) -> None:
    article_entity = ArticleEntity(id=1, title='title')
    language_entity = LanguageEntity(id=1, name='Language', code='LANG')
    translation_entity = TranslationEntity(
        id=1,
        content_path='content',
        language_id=language_entity.id,
        is_ready=True,
        article_id=article_entity.id
    )
    db_session.bulk_save_objects([article_entity, language_entity, translation_entity])
    db_session.commit()

    result = translation_repository.find_by_article_and_language(article_entity.id, language_entity.id)
    assert translation_entity.id == result.id
