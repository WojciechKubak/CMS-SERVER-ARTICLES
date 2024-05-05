from articles.infrastructure.api.service import TranslationApiService
from articles.infrastructure.db.entity import TranslationEntity, ArticleEntity, LanguageEntity
from sqlalchemy.orm import Session
import pytest


class TestGetTranslationById:

    def test_when_not_found(self, translation_api_service: TranslationApiService) -> None:
        with pytest.raises(ValueError) as err:
            translation_api_service.get_translation_by_id(9999)
        assert 'Translation does not exist' == str(err.value)

    def test_when_found(self, translation_api_service: TranslationApiService, db_session: Session) -> None:
        db_session.bulk_save_objects([
            LanguageEntity(id=1, name='name', code='CODE'),
            ArticleEntity(id=1, title='title'),
            TranslationEntity(id=1, language_id=1, article_id=1)
        ])
        db_session.commit()
        result = translation_api_service.get_translation_by_id(1)
        assert db_session.query(TranslationEntity).filter_by(id=result.id_).first()
