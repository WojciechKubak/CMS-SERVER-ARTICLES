from articles.domain.model import Category, Article, Tag, Language, Translation
from articles.infrastructure.persistance.configuration import sa
from sqlalchemy import Integer, String, Boolean, ForeignKey, Column, func
from sqlalchemy.orm import Mapped, relationship, mapped_column
from datetime import datetime
from typing import Self


articles_tags = sa.Table(
    "article_tags",
    Column("article_id", Integer, ForeignKey("articles.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class CategoryEntity(sa.Model):
    """
    SQLAlchemy model for the 'categories' table.
    """

    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    articles = relationship("ArticleEntity", back_populates="category")

    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utc_timestamp(), onupdate=func.utc_timestamp()
    )

    @classmethod
    def from_domain(cls, model: Category) -> Self:
        """
        Class method to create a CategoryEntity instance from a Category
        domain model.

        Args:
            model (Category): The Category domain model instance.

        Returns:
            CategoryEntity: The created CategoryEntity instance.
        """
        return cls(id=model.id_, name=model.name, description=model.description)

    def to_domain(self) -> Category:
        return Category(id_=self.id, name=self.name, description=self.description)


class TagEntity(sa.Model):
    """
    SQLAlchemy model for the 'tags' table.
    """

    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())

    @classmethod
    def from_domain(cls, model: Tag) -> Self:
        """
        Class method to create a TagEntity instance from a Tag domain model.

        Args:
            model (Tag): The Tag domain model instance.

        Returns:
            TagEntity: The created TagEntity instance.
        """
        return cls(id=model.id_, name=model.name)

    def to_domain(self) -> Tag:
        """
        Instance method to convert the TagEntity instance to a Tag domain
        model.

        Returns:
            Tag: The created Tag domain model instance.
        """
        return Tag(id_=self.id, name=self.name)


class LanguageEntity(sa.Model):
    """
    SQLAlchemy model for the 'languages' table.
    """

    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    code: Mapped[str] = mapped_column(String(10), nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utc_timestamp(), onupdate=func.utc_timestamp()
    )

    @classmethod
    def from_domain(cls, model: Language) -> Self:
        """
        Class method to create a LanguageEntity instance from a Language
        domain model.

        Args:
            model (Language): The Language domain model instance.

        Returns:
            LanguageEntity: The created LanguageEntity instance.
        """
        return cls(id=model.id_, name=model.name, code=model.code)

    def to_domain(self) -> Language:
        """
        Instance method to convert the LanguageEntity instance
        to a Language domain model.

        Returns:
            Language: The created Language domain model instance.
        """
        return Language(id_=self.id, name=self.name, code=self.code)


class ArticleEntity(sa.Model):
    """
    SQLAlchemy model for the 'articles' table.
    """

    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content_path: Mapped[str] = mapped_column(String(255), nullable=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped[CategoryEntity] = relationship(
        CategoryEntity, back_populates="articles", lazy="immediate"
    )
    tags: Mapped[list[TagEntity]] = relationship(
        TagEntity, secondary=articles_tags, lazy="immediate"
    )
    translations: Mapped[list["TranslationEntity"]] = relationship(
        "TranslationEntity", back_populates="article", lazy="immediate"
    )

    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utc_timestamp(), onupdate=func.utc_timestamp()
    )

    @classmethod
    def from_domain(cls, model: Article) -> Self:
        """
        Class method to create an ArticleEntity instance from an Article
        domain model.

        Args:
            model (Article): The Article domain model instance.

        Returns:
            ArticleEntity: The created ArticleEntity instance.
        """
        return cls(
            id=model.id_,
            title=model.title,
            content_path=model.content,
            category=CategoryEntity.from_domain(model.category),
            tags=[TagEntity.from_domain(tag) for tag in model.tags],
        )

    def to_domain(self) -> Article:
        """
        Instance method to convert the ArticleEntity instance to an Article
        domain model.

        Returns:
            Article: The created Article domain model instance.
        """
        return Article(
            id_=self.id,
            title=self.title,
            content=self.content_path,
            category=self.category.to_domain() if self.category else None,
            tags=[tag.to_domain() for tag in self.tags],
        )


class TranslationEntity(sa.Model):
    """
    SQLAlchemy model for the 'translations' table.
    """

    __tablename__ = "translations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content_path: Mapped[str] = mapped_column(String(255), nullable=True)
    is_ready: Mapped[bool] = mapped_column(Boolean, default=False)

    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"))
    language: Mapped[LanguageEntity] = relationship(LanguageEntity, lazy="immediate")
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"))
    article: Mapped[ArticleEntity] = relationship(
        "ArticleEntity", back_populates="translations", lazy="immediate"
    )

    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.utc_timestamp(), onupdate=func.utc_timestamp()
    )

    @classmethod
    def from_domain(cls, model: Translation) -> Self:
        """
        Class method to create a TranslationEntity instance from
        a Translation domain model.

        Args:
            model (Translation): The Translation domain model instance.

        Returns:
            TranslationEntity: The created TranslationEntity instance.
        """
        return cls(
            id=model.id_,
            content_path=model.content,
            language=LanguageEntity.from_domain(model.language),
            is_ready=model.is_ready,
            article=ArticleEntity.from_domain(model.article),
        )

    def to_domain(self) -> Translation:
        """
        Instance method to convert the TranslationEntity instance
        to a Translation domain model.

        Returns:
            Translation: The created Translation domain model instance.
        """
        return Translation(
            id_=self.id,
            content=self.content_path,
            language=self.language.to_domain(),
            is_ready=self.is_ready,
            article=self.article.to_domain(),
        )
