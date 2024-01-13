from articles.infrastructure.adapters.adapters import CategoryDbAdapter, ArticleDbAdapter, TagDbAdapter, FileStorageAdapter
from articles.infrastructure.db.configuration import category_repository, article_repository, tag_repository
from articles.infrastructure.storage.configuration import s3_bucket_manager

category_db_adapter = CategoryDbAdapter(category_repository)
article_db_adapter = ArticleDbAdapter(article_repository)
tag_db_adapter = TagDbAdapter(tag_repository)
storage_manager = FileStorageAdapter(s3_bucket_manager)
