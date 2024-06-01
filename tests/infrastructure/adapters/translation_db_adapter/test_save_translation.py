from articles.infrastructure.adapters.adapters import TranslationDbAdapter
from articles.infrastructure.persistance.entity import TranslationEntity
from tests.factory import TranslationFactory


def test_save_translation(
        translation_db_adapter: TranslationDbAdapter
) -> None:
    translation = TranslationFactory()
    result = translation_db_adapter.save_translation(translation)
    assert TranslationEntity.query.filter_by(id=result.id_).first()
