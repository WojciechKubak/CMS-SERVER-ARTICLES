from articles.infrastructure.db.repository import (
    ArticleRepository, 
    CategoryRepository, 
    TagRepository,
    LanguageRepository,
    TranslationRepository
)
from articles.env_config import DATABASE_URI
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)

article_repository = ArticleRepository(engine)
category_repository = CategoryRepository(engine)
tag_repository = TagRepository(engine)
language_repository = LanguageRepository(engine)
translation_repository = TranslationRepository(engine)
