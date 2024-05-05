from articles.domain.configuration import domain_translation_service
from articles.application.port.input import ArticleTranslationEventConsumer
from articles.infrastructure.broker.dto import TranslatedArticleDTO
from articles.domain.model import Translation
from dataclasses import dataclass
import logging


@dataclass
class ArticleTranslationConsumer:
    translation_service: ArticleTranslationEventConsumer
    
    def handle_event(self, translated_article_dto: TranslatedArticleDTO) -> Translation:
        try:
            translation = self.translation_service.handle_translated_article(
                translated_article_dto.to_domain()
            )
            return translation
        except ValueError as e:
            logging.error(f"Domain error: {e}")


article_translation_consumer = ArticleTranslationConsumer(domain_translation_service)
