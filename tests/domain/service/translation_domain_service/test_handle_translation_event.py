from articles.domain.service import TranslationService
from articles.domain.errors import (
    ArticleNotFoundError,
    LanguageNotFoundError,
    TranslationNotFoundError,
    TranslationPublishedError
)
from articles.infrastructure.persistance.entity import TranslationEntity
from tests.factory import (
    ArticleTranslatedEventFactory,
    ArticleEntityFactory,
    TranslationEntityFactory,
    LanguageEntityFactory
)
import pytest


class TestHandleTranslatedArticle:

    def test_when_no_article(
            self,
            translation_domain_service: TranslationService
    ) -> None:
        event = ArticleTranslatedEventFactory()
        with pytest.raises(ArticleNotFoundError) as e:
            translation_domain_service.handle_translation_event(event)
        assert ArticleNotFoundError().message == str(e.value)

    def test_when_no_language(
            self,
            translation_domain_service: TranslationService
    ) -> None:
        article = ArticleEntityFactory()
        event = ArticleTranslatedEventFactory(article_id=article.id)

        with pytest.raises(LanguageNotFoundError) as e:
            translation_domain_service.handle_translation_event(event)

        assert LanguageNotFoundError().message == str(e.value)

    def test_when_no_translation(
            self,
            translation_domain_service: TranslationService
    ) -> None:
        article = ArticleEntityFactory()
        language = LanguageEntityFactory()
        event = ArticleTranslatedEventFactory(
            article_id=article.id,
            language_id=language.id
        )

        with pytest.raises(TranslationNotFoundError) as e:
            translation_domain_service.handle_translation_event(event)

        assert TranslationNotFoundError().message == str(e.value)

    def test_when_translation_published(
            self,
            translation_domain_service: TranslationService
    ) -> None:
        article = ArticleEntityFactory()
        language = LanguageEntityFactory()
        TranslationEntityFactory(
            article=article,
            language=language,
            is_ready=True
        )
        event = ArticleTranslatedEventFactory(
            article_id=article.id,
            language_id=language.id,
        )

        with pytest.raises(TranslationPublishedError) as e:
            translation_domain_service.handle_translation_event(event)

        assert TranslationPublishedError().message == str(e.value)

    def test_when_handled(
            self,
            translation_domain_service: TranslationService
    ) -> None:
        article = ArticleEntityFactory()
        language = LanguageEntityFactory()
        TranslationEntityFactory(
            article=article,
            language=language,
            is_ready=False
        )
        event = ArticleTranslatedEventFactory(
            article_id=article.id,
            language_id=language.id,
        )

        result = translation_domain_service.handle_translation_event(event)
        expected = TranslationEntity.query.filter_by(id=result.id_).first()

        assert expected.is_ready
        assert expected.content_path == event.content_path
