from articles.env_config import (
    TRANSLATED_ARTICLES_TOPIC, 
    TRANSLATION_REQUESTS_TOPIC,
    LANGUAGE_CHANGES_TOPIC
)
from articles.infrastructure.adapters.adapters import (
    CategoryDbAdapter, 
    ArticleDbAdapter, 
    TagDbAdapter,
    LanguageDbAdapter,
    TranslationDbAdapter,
    FileStorageAdapter,
    ArticleMessageBroker,
    LanguageMessageBroker
)
from articles.infrastructure.db.configuration import (
    category_repository, 
    article_repository, 
    tag_repository,
    language_repository,
    translation_repository
)
from articles.infrastructure.storage.configuration import s3_bucket_manager
from articles.infrastructure.broker.configuration import kafka_manager


category_db_adapter = CategoryDbAdapter(category_repository)
article_db_adapter = ArticleDbAdapter(article_repository)
tag_db_adapter = TagDbAdapter(tag_repository)
language_db_adapter = LanguageDbAdapter(language_repository)
translation_db_adapter = TranslationDbAdapter(translation_repository)
storage_manager = FileStorageAdapter(s3_bucket_manager)
article_message_broker = ArticleMessageBroker(
    kafka_manager,
    TRANSLATION_REQUESTS_TOPIC,
    TRANSLATED_ARTICLES_TOPIC
)
language_message_broker = LanguageMessageBroker(
    kafka_manager, LANGUAGE_CHANGES_TOPIC
)
