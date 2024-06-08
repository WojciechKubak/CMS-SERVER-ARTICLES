from articles.infrastructure.persistance.configuration import sa
from articles.infrastructure.persistance.entity import (
    ArticleEntity,
    CategoryEntity,
    TagEntity,
    TranslationEntity,
    LanguageEntity,
)
from articles.domain.model import Article, Category, Tag, Language, Translation
from articles.domain.event import (
    ArticleTranslatedEvent,
    TranslationRequestEvent,
    LanguageEvent,
    LanguageEventType,
)
from factory import (
    Factory,
    SubFactory,
    Sequence,
    RelatedFactoryList,
    LazyFunction,
    Faker,
)
from factory.alchemy import SQLAlchemyModelFactory


class CategoryEntityFactory(SQLAlchemyModelFactory):
    class Meta:
        model = CategoryEntity
        sqlalchemy_session = sa.session
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n + 1)
    name = Sequence(lambda n: f"name{n}")
    description = Sequence(lambda n: f"description{n}")


class TagEntityFactory(SQLAlchemyModelFactory):
    class Meta:
        model = TagEntity
        sqlalchemy_session = sa.session
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n + 1)
    name = Sequence(lambda n: f"name{n}")


class LanguageEntityFactory(SQLAlchemyModelFactory):
    class Meta:
        model = LanguageEntity
        sqlalchemy_session = sa.session
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n + 1)
    name = Sequence(lambda n: f"name{n}")
    code = Sequence(lambda n: f"code{n}")


class ArticleEntityFactory(SQLAlchemyModelFactory):
    class Meta:
        model = ArticleEntity
        sqlalchemy_session = sa.session
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n + 1)
    title = Sequence(lambda n: f"title{n}")
    content_path = Sequence(lambda n: f"content_path{n}")
    category = SubFactory(CategoryEntityFactory)
    tags = RelatedFactoryList(TagEntityFactory, size=3)


class TranslationEntityFactory(SQLAlchemyModelFactory):
    class Meta:
        model = TranslationEntity
        sqlalchemy_session = sa.session
        sqlalchemy_session_persistence = "commit"

    id = Sequence(lambda n: n + 1)
    content_path = Sequence(lambda n: f"content_path{n}")
    is_ready = True
    language = SubFactory(LanguageEntityFactory)
    article = SubFactory(ArticleEntityFactory)


class CategoryFactory(Factory):
    class Meta:
        model = Category

    id_ = Sequence(lambda n: n + 1)
    name = Sequence(lambda n: f"Category{n}")
    description = Sequence(lambda n: f"Description{n}")


class TagFactory(Factory):
    class Meta:
        model = Tag

    id_ = Sequence(lambda n: n + 1)
    name = Sequence(lambda n: f"Tag{n}")


class LanguageFactory(Factory):
    class Meta:
        model = Language

    id_ = Sequence(lambda n: n + 1)
    name = Sequence(lambda n: f"Language{n}")
    code = Sequence(lambda n: f"Code{n}")


class ArticleFactory(Factory):
    class Meta:
        model = Article

    id_ = Sequence(lambda n: n + 1)
    title = Sequence(lambda n: f"Title{n}")
    content = Sequence(lambda n: f"Content{n}")
    category = SubFactory(CategoryFactory)
    tags = LazyFunction(lambda: [TagFactory() for _ in range(3)])


class TranslationFactory(Factory):
    class Meta:
        model = Translation

    id_ = Sequence(lambda n: n + 1)
    language = SubFactory(LanguageFactory)
    content = Sequence(lambda n: f"Content{n}")
    is_ready = False
    article = SubFactory(ArticleFactory)


class ArticleTranslatedEventFactory(Factory):
    class Meta:
        model = ArticleTranslatedEvent

    article_id = Sequence(lambda n: n + 1)
    title = Sequence(lambda n: f"Title{n}")
    content_path = Sequence(lambda n: f"ContentPath{n}")
    language_id = Sequence(lambda n: n + 1)
    author_id = Sequence(lambda n: n + 1)


class TranslationRequestEventFactory(Factory):
    class Meta:
        model = TranslationRequestEvent

    article_id = Sequence(lambda n: n + 1)
    title = Sequence(lambda n: f"Title{n}")
    content_path = Sequence(lambda n: f"ContentPath{n}")
    language_id = Sequence(lambda n: n + 1)
    date = Faker("date_time")


class LanguageEventFactory(Factory):
    class Meta:
        model = LanguageEvent

    id_ = Sequence(lambda n: n + 1)
    name = Sequence(lambda n: f"Name{n}")
    code = Sequence(lambda n: f"Code{n}")
    event_type = LanguageEventType.CREATE
