from articles.application.port.input import ArticleTranslationEventConsumer
from articles.infrastructure.broker.consumer import ArticleTranslationConsumer
from articles.infrastructure.broker.dto import TranslatedArticleDTO
from articles.domain.model import Translation
from unittest.mock import MagicMock, patch, create_autospec
import pytest 


class TestArticleTranslationConsumerHandleEvent:

    @pytest.fixture(scope='session')
    def article_translation_consumer(self, translation_domain_service: ArticleTranslationEventConsumer) -> ArticleTranslationConsumer:
        return ArticleTranslationConsumer(translation_domain_service)

    @pytest.mark.skip
    @patch.object(ArticleTranslationEventConsumer, 'handle_translated_article')
    def test_when_handled_correctly(
        self, 
        mock_handle_translated_article: MagicMock,
        article_translation_consumer: ArticleTranslationConsumer
    ) -> None:
        translated_article_dto = create_autospec(TranslatedArticleDTO)
        expected_translation = create_autospec(Translation)
        mock_handle_translated_article.return_value = expected_translation

        result = article_translation_consumer.handle_event(translated_article_dto)

        mock_handle_translated_article.assert_called_once_with(expected_translation)
        assert result == expected_translation

    @pytest.mark.skip
    @patch.object(ArticleTranslationEventConsumer, 'handle_translated_article')
    def test_when_error_occurs(
        self, 
        mock_handle_translated_article: MagicMock,
        article_translation_consumer: ArticleTranslationConsumer
    ) -> None:
        translated_article_dto = create_autospec(TranslatedArticleDTO)
        mock_handle_translated_article.side_effect = ValueError("An error occurred")

        with pytest.raises(ValueError) as e:
            article_translation_consumer.handle_event(translated_article_dto)

        assert "An error occurred" == str(e.value)
