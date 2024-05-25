from articles.domain.configuration import domain_translation_service
from articles.application.port.input import ArticleTranslationEventConsumer
from articles.infrastructure.broker.dto import TranslatedArticleDTO
from articles.domain.model import Translation
from dataclasses import dataclass


@dataclass
class ConsumerService:
    translation_service: ArticleTranslationEventConsumer
 
    def handle_translated_article(self, translated_article_dto: TranslatedArticleDTO) -> Translation:
        event = translated_article_dto.to_domain()
        self.translation_service.handle_translated_article(event)


consumer_service = ConsumerService(domain_translation_service)
