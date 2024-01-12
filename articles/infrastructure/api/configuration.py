from articles.domain.configuration import domain_category_service, domain_article_service, domain_tag_service
from articles.infrastructure.api.service import CategoryApiService, ArticleApiService, TagApiService

category_service = CategoryApiService(domain_category_service)
article_service = ArticleApiService(domain_article_service)
tag_service = TagApiService(domain_tag_service)
