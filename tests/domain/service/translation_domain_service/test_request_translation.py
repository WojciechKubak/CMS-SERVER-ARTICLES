from articles.infrastructure.persistance.entity import TranslationEntity
from articles.domain.service import TranslationService
from articles.domain.errors import (
    ArticleNotFoundError,
    LanguageNotFoundError,
    TranslationExistsError,
)
from tests.factory import (
    ArticleEntityFactory,
    LanguageEntityFactory,
    TranslationEntityFactory,
)
from unittest.mock import patch
import pytest


class TestRequestArticleTranslation:

    def test_when_no_language(
        self, translation_domain_service: TranslationService
    ) -> None:
        article = ArticleEntityFactory()

        with pytest.raises(LanguageNotFoundError) as e:
            translation_domain_service.request_translation(article.id, 999)

        assert LanguageNotFoundError().message == str(e.value)

    def test_when_no_article(
        self, translation_domain_service: TranslationService
    ) -> None:
        language = LanguageEntityFactory()

        with pytest.raises(ArticleNotFoundError) as err:
            translation_domain_service.request_translation(999, language.id)

        assert ArticleNotFoundError().message == str(err.value)

    def test_when_translation_exists(
        self, translation_domain_service: TranslationService
    ) -> None:
        translation = TranslationEntityFactory()
        with pytest.raises(TranslationExistsError) as err:
            translation_domain_service.request_translation(
                translation.article_id, translation.language_id
            )
        assert TranslationExistsError().message == str(err.value)

    @pytest.mark.skip("Adapter not returning ID of dao")
    def test_when_translation_request(
        self, translation_domain_service: TranslationService
    ) -> None:
        article = ArticleEntityFactory()
        language = LanguageEntityFactory()

        with patch.object(
            translation_domain_service.article_event_publisher, "publish_event"
        ) as publish:
            result = translation_domain_service.request_translation(
                article.id, language.id
            )

        publish.assert_called_once()
        assert TranslationEntity.query.filter_by(id=result.id_).first()
