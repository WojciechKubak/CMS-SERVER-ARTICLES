from articles.domain.service import CategoryDomainService, ArticleDomainService, TagDomainService
from articles.infrastructure.adapters.configuration import (
    category_db_adapter, 
    article_db_adapter, 
    tag_db_adapter,
    storage_manager
)

domain_article_service = ArticleDomainService(
    article_db_adapter, 
    category_db_adapter, 
    tag_db_adapter,
    storage_manager
)
domain_category_service = CategoryDomainService(category_db_adapter)
domain_tag_service = TagDomainService(tag_db_adapter)
