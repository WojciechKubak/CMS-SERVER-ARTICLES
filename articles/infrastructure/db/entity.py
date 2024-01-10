from sqlalchemy import Integer, String, Text, ForeignKey, func, Table, Column
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


class TagEntity(Base):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(String(25), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())


class ArticleEntity(Base):

    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(Text(), nullable=True)
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey('categories.id'), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=func.utc_timestamp(), onupdate=func.utc_timestamp())
    category: Mapped[CategoryEntity] = relationship(CategoryEntity, back_populates='articles')
    tags: Mapped[list[TagEntity]] = relationship(TagEntity, secondary=articles_tags)
