from articles.domain.configuration import (
    domain_category_service, 
    domain_article_service, 
    domain_tag_service,
    domain_language_service,
    domain_translation_service
)
from articles.infrastructure.api.service import (
    CategoryApiService, 
    ArticleApiService, 
    TagApiService,
    TranslationApiService,
    LanguageApiService
)

category_service = CategoryApiService(domain_category_service)
article_service = ArticleApiService(domain_article_service)
tag_service = TagApiService(domain_tag_service)
language_service = LanguageApiService(domain_language_service)
translation_service = TranslationApiService(domain_translation_service)
