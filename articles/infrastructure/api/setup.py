from articles.infrastructure.api.routes import (
    CategoryResource,
    CategoryIdResource,
    CategoryListResource,
    ArticleResource,
    ArticleIdResource,
    ArticlesWithCategoryResource,
    ArticleListResource,
    TagResource,
    TagIdResource,
    TagListResource,
    ArticleTranslationResource,
    TranslationIdResource,
    LanguageIdResource,
    LanguageResource,
    LanguageListResource
)
from flask_restful import Api


def setup_routing(api: Api) -> None:
    api.add_resource(CategoryResource, '/categories')
    api.add_resource(CategoryListResource, '/categories')
    api.add_resource(CategoryIdResource, '/categories/<int:id_>')

    api.add_resource(ArticleResource, '')
    api.add_resource(ArticleIdResource, '/<int:id_>')
    api.add_resource(
        ArticlesWithCategoryResource,
        '/category/<int:category_id>'
    )
    api.add_resource(ArticleListResource, '')

    api.add_resource(TagResource, '/tags')
    api.add_resource(TagIdResource, '/tags/<int:id_>')
    api.add_resource(TagListResource, '/tags')

    api.add_resource(LanguageResource, '/languages')
    api.add_resource(LanguageIdResource, '/languages/<int:id_>')
    api.add_resource(LanguageListResource, '/languages')

    api.add_resource(
        ArticleTranslationResource,
        '/<int:article_id>/languages/<int:language_id>'
    )
    api.add_resource(TranslationIdResource, '/translations/<int:id_>')
