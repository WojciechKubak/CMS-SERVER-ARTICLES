from articles.domain.service import TranslationDomainService
from articles.domain.event import ArticleTranslatedEvent
from articles.infrastructure.db.entity import (
    TranslationEntity, 
    LanguageEntity, 
    ArticleEntity,
    CategoryEntity
)
from sqlalchemy.orm import Session
from datetime import datetime
import pytest


class TestHandleTranslatedArticle:
    article_translated_event = ArticleTranslatedEvent(
        article_id=1, 
        language_id=1, 
        content_path='path', 
        date=datetime.now()
    )

    def test_when_no_article(self, translation_domain_service: TranslationDomainService) -> None:
        with pytest.raises(ValueError) as err:
            translation_domain_service.handle_translated_article(self.article_translated_event)
        assert 'Article does not exist' == str(err.value)

    def test_when_no_language(self, translation_domain_service: TranslationDomainService, db_session: Session) -> None:
        db_session.add(ArticleEntity(id=1, title='title'))
        db_session.commit()
        with pytest.raises(ValueError) as err:
            translation_domain_service.handle_translated_article(self.article_translated_event)
        assert 'Language does not exist' == str(err.value)

    def test_when_no_translation(self, translation_domain_service: TranslationDomainService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            ArticleEntity(id=1, title='title'),
            LanguageEntity(id=1, name='name', code='CODE')
        ])
        db_session.commit()
        with pytest.raises(ValueError) as err:
            translation_domain_service.handle_translated_article(self.article_translated_event)
        assert 'Translation does not exist' == str(err.value)

    def test_when_translation_published(self, translation_domain_service: TranslationDomainService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            ArticleEntity(id=1, title='title'),
            LanguageEntity(id=1, name='name', code='CODE'),
            TranslationEntity(id=1, language_id=1, article_id=1, is_ready=True)
        ])
        db_session.commit()
        with pytest.raises(ValueError) as err:
            translation_domain_service.handle_translated_article(self.article_translated_event)
        assert 'Translation already published' == str(err.value)

    def test_when_handled(self, translation_domain_service: TranslationDomainService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            CategoryEntity(id=1, name='name'),
            ArticleEntity(id=1, title='title', category_id=1),
            LanguageEntity(id=1, name='name', code='CODE'),
            TranslationEntity(id=1, language_id=1, article_id=1, is_ready=False)
        ])
        db_session.commit()
        result = translation_domain_service.handle_translated_article(self.article_translated_event)
        assert db_session.query(TranslationEntity).filter_by(id=result.id_).first().is_ready
        assert self.article_translated_event.content_path ==  \
            db_session.query(TranslationEntity).filter_by(id=result.id_).first().content_path
