from articles.infrastructure.broker.dto import TranslatedArticleDTO
from articles.domain.errors import DomainError
from articles.infrastructure.broker.errors import TranslationHandlerError
from articles.infrastructure.broker.consumer import ConsumerService
from unittest.mock import Mock, patch
import pytest


@pytest.fixture(scope='session')
def consumer_service() -> ConsumerService:
    with patch(
        'articles.infrastructure.broker.consumer.domain_translation_service'
    ) as mock_translation_service:
        yield ConsumerService(mock_translation_service)


class TestHandleTranslatedArticle:

    @pytest.mark.skip('Refactor this test')
    def test_when_domain_error(
        self,
        consumer_service: ConsumerService
    ) -> None:
        consumer_service.translation_service.reset_mock()

        mock_dto = Mock(spec=TranslatedArticleDTO)
        mock_dto.to_domain.return_value = 'mock_event'
        consumer_service.translation_service.\
            handle_translation_event.side_effect = DomainError('mock_error')

        with pytest.raises(TranslationHandlerError) as exc_info:
            consumer_service.handle_translated_article(mock_dto)

        assert 'mock_error' == str(exc_info.value)
        mock_dto.to_domain.assert_called_once()
        consumer_service.translation_service.handle_translation_event \
            .assert_called_once_with('mock_event')

    @pytest.mark.skip('Refactor this test')
    def test_when_handled(
            self,
            consumer_service: ConsumerService
    ) -> None:
        mock_dto = Mock(spec=TranslatedArticleDTO)
        mock_dto.to_domain.return_value = 'mock_event'
        mock_translation = 'mock_translation'
        consumer_service.translation_service. \
            handle_translation_event.return_value = mock_translation

        result = consumer_service.handle_translated_article(mock_dto)

        mock_dto.to_domain.assert_called_once()
        consumer_service.translation_service.handle_translation_event \
            .assert_called_once_with('mock_event')
        assert mock_translation == result
