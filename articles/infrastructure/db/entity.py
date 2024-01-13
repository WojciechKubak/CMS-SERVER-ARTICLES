from articles.domain.model import Category, Article, Tag
from sqlalchemy import Integer, String, ForeignKey, func, Table, Column
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

Base = declarative_base()


articles_tags = Table(
    'article_tags',
    Base.metadata,
    Column('article_id', Integer(), ForeignKey('articles.id'), primary_key=True),
    Column('tag_id', Integer(), ForeignKey('tags.id'), primary_key=True),
)


class CategoryEntity(Base):

    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    articles = relationship('ArticleEntity', back_populates='category')

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


class TagEntity(Base):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())

    @classmethod
    def from_domain(cls, model: Tag) -> 'TagEntity':
        return cls(id=model.id_, name=model.name)

    def to_domain(self) -> Tag:
        return Tag(id_=self.id, name=self.name)


class ArticleEntity(Base):

    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content_path: Mapped[str] = mapped_column(String(255), nullable=True)
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey('categories.id'), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    category: Mapped[CategoryEntity] = relationship(CategoryEntity, back_populates='articles', lazy='immediate')
    tags: Mapped[list[TagEntity]] = relationship(TagEntity, secondary=articles_tags, lazy='immediate')

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
            tags=[tag.to_domain() for tag in self.tags]
        )
