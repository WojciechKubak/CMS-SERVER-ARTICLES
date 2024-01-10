from articles.config import get_app_configuration
from articles.infrastructure.db.repository import ArticleRepository, CategoryRepository, TagRepository
from sqlalchemy import create_engine

engine = create_engine(get_app_configuration().DATABASE_URI)

article_repository = ArticleRepository(engine)
category_repository = CategoryRepository(engine)
tag_repository = TagRepository(engine)
