from articles.domain.model import Category, Article, Tag, Language, Translation
from articles.infrastructure.persistance.configuration import sa
from sqlalchemy import Integer, String, Boolean, ForeignKey, Column, func
from sqlalchemy.orm import Mapped, relationship, mapped_column
from datetime import datetime


articles_tags = sa.Table(
    'article_tags',
    Column('article_id', Integer, ForeignKey('articles.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)


class CategoryEntity(sa.Model):

    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    articles = relationship('ArticleEntity', back_populates='category')

    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utc_timestamp(),
        onupdate=func.utc_timestamp()
    )

    @classmethod
    def from_domain(cls, model: Category) -> 'CategoryEntity':
        return cls(
            id=model.id_,
            name=model.name,
            description=model.description
        )

    def to_domain(self) -> Category:
        return Category(
            id_=self.id,
            name=self.name,
            description=self.description
        )


class TagEntity(sa.Model):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())

    @classmethod
    def from_domain(cls, model: Tag) -> 'TagEntity':
        return cls(id=model.id_, name=model.name)

    def to_domain(self) -> Tag:
        return Tag(id_=self.id, name=self.name)


class LanguageEntity(sa.Model):

    __tablename__ = 'languages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    code: Mapped[str] = mapped_column(String(10), nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utc_timestamp(),
        onupdate=func.utc_timestamp()
    )

    @classmethod
    def from_domain(cls, model: Language) -> 'LanguageEntity':
        return cls(id=model.id_, name=model.name, code=model.code)

    def to_domain(self) -> Language:
        return Language(id_=self.id, name=self.name, code=self.code)


class ArticleEntity(sa.Model):

    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content_path: Mapped[str] = mapped_column(String(255), nullable=True)

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped[CategoryEntity] = relationship(
        CategoryEntity,
        back_populates='articles',
        lazy='immediate'
    )
    tags: Mapped[list[TagEntity]] = relationship(
        TagEntity,
        secondary=articles_tags,
        lazy='immediate'
    )
    translations: Mapped[list['TranslationEntity']] = relationship(
        'TranslationEntity',
        back_populates='article',
        lazy='immediate'
    )

    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utc_timestamp(),
        onupdate=func.utc_timestamp()
    )

    @classmethod
    def from_domain(cls, model: Article) -> 'ArticleEntity':
        return cls(
            id=model.id_,
            title=model.title,
            content_path=model.content,
            category=CategoryEntity.from_domain(model.category),
            tags=[TagEntity.from_domain(tag) for tag in model.tags]
        )

    def to_domain(self) -> Article:
        return Article(
            id_=self.id,
            title=self.title,
            content=self.content_path,
            category=self.category.to_domain() if self.category else None,
            tags=[tag.to_domain() for tag in self.tags],
        )


class TranslationEntity(sa.Model):

    __tablename__ = 'translations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content_path: Mapped[str] = mapped_column(String(255), nullable=True)
    is_ready: Mapped[bool] = mapped_column(Boolean, default=False)

    language_id: Mapped[int] = mapped_column(ForeignKey('languages.id'))
    language: Mapped[LanguageEntity] = relationship(
        LanguageEntity,
        lazy='immediate'
    )
    article_id: Mapped[int] = mapped_column(ForeignKey('articles.id'))
    article: Mapped[ArticleEntity] = relationship(
        'ArticleEntity',
        back_populates='translations',
        lazy='immediate'
    )

    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utc_timestamp(),
        onupdate=func.utc_timestamp()
    )

    @classmethod
    def from_domain(cls, model: Translation) -> 'TranslationEntity':
        return cls(
            id=model.id_,
            content_path=model.content,
            language=LanguageEntity.from_domain(model.language),
            is_ready=model.is_ready,
            article=ArticleEntity.from_domain(model.article)
        )

    def to_domain(self) -> Translation:
        return Translation(
            id_=self.id,
            content=self.content_path,
            language=self.language.to_domain(),
            is_ready=self.is_ready,
            article=self.article.to_domain()
        )
