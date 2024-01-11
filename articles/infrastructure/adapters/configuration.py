from articles.infrastructure.adapters.adapters import CategoryDbAdapter, ArticleDbAdapter, TagDbAdapter
from articles.infrastructure.db.configuration import category_repository, article_repository, tag_repository

category_db_adapter = CategoryDbAdapter(category_repository)
article_db_adapter = ArticleDbAdapter(article_repository)
tag_db_adapter = TagDbAdapter(tag_repository)
