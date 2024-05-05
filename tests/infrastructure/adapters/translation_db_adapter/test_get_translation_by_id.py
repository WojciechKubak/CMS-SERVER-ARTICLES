from articles.infrastructure.adapters.adapters import TranslationDbAdapter
from articles.infrastructure.db.entity import TranslationEntity, ArticleEntity, LanguageEntity
from sqlalchemy.orm import Session


class TestGetTranslationById:

    def test_when_not_found(self, translation_db_adapter: TranslationDbAdapter, db_session: Session) -> None:
        result = translation_db_adapter.get_translation_by_id(1111)
        assert not result
        assert not db_session.query(TranslationEntity).filter_by(id=1111).first()

    def test_when_found(self, translation_db_adapter: TranslationDbAdapter, db_session: Session) -> None:
        db_session.bulk_save_objects([
            ArticleEntity(id=1, title='title'),
            LanguageEntity(id=1, name='lang', code='C'),
            TranslationEntity(id=1, article_id=1, language_id=1),
        ])
        db_session.commit()
        result = translation_db_adapter.get_translation_by_id(1)
        assert 1 == result.id_
