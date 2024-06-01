from articles.infrastructure.broker.errors import TranslationHandlerError
from articles.infrastructure.broker.dto import TranslatedArticleDTO
from articles.domain.configuration import domain_translation_service
from articles.domain.errors import DomainError
from articles.domain.model import Translation
from articles.application.ports.input import TranslationConsumer
from dataclasses import dataclass


@dataclass
class ConsumerService:
    translation_service: TranslationConsumer

    def handle_translated_article(
            self,
            translated_article_dto: TranslatedArticleDTO
    ) -> Translation:
        event = translated_article_dto.to_domain()
        try:
            return self.translation_service.handle_translation_event(event)
        except DomainError as e:
            raise TranslationHandlerError(str(e))


consumer_service = ConsumerService(domain_translation_service)
