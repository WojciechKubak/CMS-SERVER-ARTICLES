from articles.domain.service import (
    CategoryService,
    ArticleService,
    TagService,
    LanguageService,
    TranslationService,
)
from articles.infrastructure.adapters.configuration import (
    category_db_adapter,
    article_db_adapter,
    tag_db_adapter,
    translation_db_adapter,
    language_db_adapter,
    storage_manager,
    article_message_broker,
    language_message_broker,
)


domain_article_service = ArticleService(
    article_db_adapter, category_db_adapter, tag_db_adapter, storage_manager
)
domain_translation_service = TranslationService(
    article_db_adapter,
    language_db_adapter,
    translation_db_adapter,
    storage_manager,
    article_message_broker,
)
domain_category_service = CategoryService(category_db_adapter)
domain_tag_service = TagService(tag_db_adapter)
domain_language_service = LanguageService(language_db_adapter, language_message_broker)
