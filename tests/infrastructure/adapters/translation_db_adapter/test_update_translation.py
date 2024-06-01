from articles.infrastructure.adapters.adapters import TranslationDbAdapter
from articles.infrastructure.persistance.entity import TranslationEntity
from tests.factory import TranslationEntityFactory, TranslationFactory


def test_update_translation(
        translation_db_adapter: TranslationDbAdapter
) -> None:
    translation_dao = TranslationEntityFactory(is_ready=False)
    translation = TranslationFactory(
        id_=translation_dao.id,
        is_ready=True
    )

    result = translation_db_adapter.update_translation(translation)

    assert TranslationEntity.query.filter_by(id=result.id_).first().is_ready
