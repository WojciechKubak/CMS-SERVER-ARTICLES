from articles.domain.service import (
    CategoryDomainService, 
    ArticleDomainService, 
    TagDomainService,
    LanguageDomainService,
    TranslationDomainService
)
from articles.infrastructure.adapters.configuration import (
    category_db_adapter, 
    article_db_adapter, 
    tag_db_adapter,
    translation_db_adapter,
    language_db_adapter,
    storage_manager,
    message_broker
)


domain_article_service = ArticleDomainService(
    article_db_adapter, 
    category_db_adapter, 
    tag_db_adapter,
    storage_manager
)
domain_translation_service = TranslationDomainService(
    article_db_adapter,
    language_db_adapter,
    translation_db_adapter,
    storage_manager,
    message_broker
)
domain_category_service = CategoryDomainService(category_db_adapter)
domain_tag_service = TagDomainService(tag_db_adapter)
domain_language_service = LanguageDomainService(language_db_adapter)
