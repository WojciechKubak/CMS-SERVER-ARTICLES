from articles.infrastructure.broker.errors import TranslationHandlerError
from articles.infrastructure.broker.dto import TranslatedArticleDTO
from articles.domain.configuration import domain_translation_service
from articles.domain.errors import DomainError
from articles.domain.model import Translation
from articles.application.ports.input import TranslationConsumer
from dataclasses import dataclass


@dataclass
class ConsumerService:
    """
    Service for consuming translation events.

    This class provides a method to handle translated articles.

    Attributes:
        translation_service (TranslationConsumer): The translation
        consumer service.
    """

    translation_service: TranslationConsumer

    def handle_translated_article(
            self,
            translated_article_dto: TranslatedArticleDTO
    ) -> Translation:
        """
        Handle a translated article.

        This method converts the DTO to a domain event and passes it to the
        translation service.
        If the translation service raises a DomainError, it is converted to
        a TranslationHandlerError.

        Args:
            translated_article_dto (TranslatedArticleDTO): The DTO of the
            translated article.

        Returns:
            Translation: The translation result.

        Raises:
            TranslationHandlerError: If the translation service raises
            a DomainError.
        """
        event = translated_article_dto.to_domain()
        try:
            return self.translation_service.handle_translation_event(event)
        except DomainError as e:
            raise TranslationHandlerError(str(e))


consumer_service = ConsumerService(domain_translation_service)
