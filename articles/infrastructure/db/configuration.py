from articles.settings import DATABASE_URI
from articles.infrastructure.db.repository import ArticleRepository, CategoryRepository, TagRepository
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)

article_repository = ArticleRepository(engine)
category_repository = CategoryRepository(engine)
tag_repository = TagRepository(engine)
