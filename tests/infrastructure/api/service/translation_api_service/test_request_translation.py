from articles.infrastructure.api.service import TranslationApiService
from articles.infrastructure.db.entity import (
    TranslationEntity, 
    LanguageEntity, 
    ArticleEntity, 
    CategoryEntity
)
from sqlalchemy.orm import Session
import pytest


class TestRequestTranslation:

    def test_when_no_language(self, translation_api_service: TranslationApiService) -> None:
        with pytest.raises(ValueError) as err:
            translation_api_service.request_translation(1, 1)
        assert 'Language does not exist' == str(err.value)

    def test_when_no_article(self, translation_api_service: TranslationApiService, db_session: Session) -> None:
        db_session.add(LanguageEntity(id=1, name='name', code='CODE'))
        db_session.commit()
        with pytest.raises(ValueError) as err:
            translation_api_service.request_translation(1, 1)
        assert 'Article does not exist' == str(err.value)

    def test_when_translation_exists(self, translation_api_service: TranslationApiService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            LanguageEntity(id=1, name='name', code='CODE'),
            ArticleEntity(id=1, title='title'),
            TranslationEntity(id=1, language_id=1, article_id=1)
        ])
        db_session.commit()
        with pytest.raises(ValueError) as err:
            translation_api_service.request_translation(1, 1)
        assert 'Translation already exists' == str(err.value)

    def test_when_translation_requested(self, translation_api_service: TranslationApiService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            LanguageEntity(id=1, name='name', code='CODE'),
            CategoryEntity(id=1, name='name'),
            ArticleEntity(id=1, title='title', category_id=1)
        ])
        db_session.commit()
        result = translation_api_service.request_translation(1, 1)
        assert 1 == result.article.id_
        assert 1 == result.language.id_
