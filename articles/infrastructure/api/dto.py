from articles.domain.model import Category, Tag, Article, Language, Translation
from dataclasses import dataclass
from typing import Any, Self
from abc import ABC


@dataclass
class CategoryBase(ABC):
    """
    Abstract base class for Category data transfer objects.

    Attributes:
        name (str): The name of the category.
        description (str | None): The description of the category. Optional.
    """

    name: str
    description: str | None


@dataclass
class CategoryDTO(CategoryBase):
    """
    Data transfer object for a Category.

    Attributes:
        id_ (int): The ID of the category.
    """

    id_: int

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the CategoryDTO to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the CategoryDTO.
        """
        return {
            'id': self.id_,
            'name': self.name,
        }

    @classmethod
    def from_domain(cls, category: Category) -> None:
        """
        Create a CategoryDTO from a Category domain object.

        Args:
            category (Category): The Category domain object.

        Returns:
            CategoryDTO: The created CategoryDTO.
        """
        return cls(
            id_=category.id_,
            name=category.name,
            description=category.description
        )


@dataclass
class CategoryCreateDTO(CategoryBase):
    """
    Data transfer object for creating a Category.
    """

    pass

    def to_domain(self) -> Category:
        """
        Convert the CategoryCreateDTO to a Category domain object.

        Returns:
            Category: The created Category domain object.
        """
        return Category(id_=None, **self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> None:
        """
        Create a CategoryCreateDTO from a dictionary.

        Args:
            data (dict[str, Any]): The dictionary.

        Returns:
            CategoryCreateDTO: The created CategoryCreateDTO.
        """
        return cls(
            name=data['name'],
            description=data.get('description', None)
        )


@dataclass
class CategoryUpdateDTO(CategoryBase):
    """
    Data transfer object for updating a Category.

    Attributes:
        id_ (int): The ID of the category.
    """

    id_: int

    def to_domain(self) -> Category:
        """
        Convert the CategoryUpdateDTO to a Category domain object.

        Returns:
            Category: The created Category domain object.
        """
        return Category(**self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> None:
        """
        Create a CategoryUpdateDTO from a dictionary.

        Args:
            data (dict[str, Any]): The dictionary.

        Returns:
            CategoryUpdateDTO: The created CategoryUpdateDTO.
        """
        return cls(
            id_=data['id'],
            name=data['name'],
            description=data.get('description', None)
        )


@dataclass
class TagBase(ABC):
    """
    Abstract base class for Tag data transfer objects.

    Attributes:
        name (str): The name of the tag.
    """

    name: str


@dataclass
class TagDTO(TagBase):
    """
    Data transfer object for a Tag.

    Attributes:
        id_ (int): The ID of the tag.
    """

    id_: int

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the TagDTO to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the TagDTO.
        """
        return {
            'id': self.id_,
            'name': self.name,
        }

    @classmethod
    def from_domain(cls, tag: Tag) -> Tag:
        """
        Create a TagDTO from a Tag domain object.

        Args:
            tag (Tag): The Tag domain object.

        Returns:
            TagDTO: The created TagDTO.
        """
        return cls(
            id_=tag.id_,
            name=tag.name
        )


@dataclass
class TagCreateDTO(TagBase):
    """
    Data transfer object for creating a Tag.
    """

    pass

    def to_domain(self) -> Tag:
        """
        Convert the TagCreateDTO to a Tag domain object.

        Returns:
            Tag: The created Tag domain object.
        """
        return Tag(id_=None, **self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """
        Create a TagCreateDTO from a dictionary.

        Args:
            data (dict[str, Any]): The dictionary.

        Returns:
            TagCreateDTO: The created TagCreateDTO.
        """
        return cls(
            name=data['name']
        )


@dataclass
class TagUpdateDTO(TagBase):
    """
    Data transfer object for updating a Tag.

    Attributes:
        id_ (int): The ID of the tag.
    """

    id_: int

    def to_domain(self) -> Tag:
        """
        Convert the TagUpdateDTO to a Tag domain object.

        Returns:
            Tag: The created Tag domain object.
        """
        return Tag(**self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """
        Create a TagUpdateDTO from a dictionary.

        Args:
            data (dict[str, Any]): The dictionary.

        Returns:
            TagUpdateDTO: The created TagUpdateDTO.
        """
        return cls(
            id_=data['id'],
            name=data['name']
        )


@dataclass
class LanguageBase(ABC):
    """
    Abstract base class for Language data transfer objects.

    Attributes:
        name (str): The name of the language.
        code (str): The code of the language.
    """

    name: str
    code: str


@dataclass
class LanguageDTO(LanguageBase):
    """
    Data transfer object for a Language.

    Attributes:
        id_ (int): The ID of the language.
    """

    id_: int

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the LanguageDTO to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the LanguageDTO.
        """
        return {
            'id': self.id_,
            'name': self.name,
            'code': self.code
        }

    @classmethod
    def from_domain(cls, language: Language) -> Self:
        """
        Create a LanguageDTO from a Language domain object.

        Args:
            language (Language): The Language domain object.

        Returns:
            LanguageDTO: The created LanguageDTO.
        """
        return cls(
            id_=language.id_,
            name=language.name,
            code=language.code
        )


@dataclass
class LanguageCreateDTO(LanguageBase):
    """
    Data transfer object for creating a Language.
    """

    pass

    def to_domain(self) -> Language:
        """
        Convert the LanguageCreateDTO to a Language domain object.

        Returns:
            Language: The created Language domain object.
        """
        return Language(id_=None, **self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """
        Create a LanguageCreateDTO from a dictionary.

        Args:
            data (dict[str, Any]): The dictionary.

        Returns:
            LanguageCreateDTO: The created LanguageCreateDTO.
        """
        return cls(
            name=data['name'],
            code=data['code']
        )


@dataclass
class LanguageUpdateDTO(LanguageBase):
    """
    Data transfer object for updating a Language.

    Attributes:
        id_ (int): The ID of the language.
    """
    id_: int

    def to_domain(self) -> Language:
        """
        Convert the LanguageUpdateDTO to a Language domain object.

        Returns:
            Language: The created Language domain object.
        """
        return Language(**self.__dict__)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """
        Create a LanguageUpdateDTO from a dictionary.

        Args:
            data (dict[str, Any]): The dictionary.

        Returns:
            LanguageUpdateDTO: The created LanguageUpdateDTO.
        """
        return cls(
            id_=data['id'],
            name=data['name'],
            code=data['code']
        )


@dataclass
class ArticleBase(ABC):
    """
    Abstract base class for Article data transfer objects.

    Attributes:
        title (str): The title of the article.
    """

    title: str


@dataclass
class ArticleDTO(ArticleBase):
    """
    Data transfer object for an Article.

    Attributes:
        id_ (int): The ID of the article.
        content (str): The content of the article.
        category (CategoryDTO): The category of the article.
        tags (list[TagDTO]): The tags of the article.
    """

    id_: int
    content: str
    category: CategoryDTO
    tags: list[TagDTO]

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the ArticleDTO to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the ArticleDTO.
        """
        return {
            'id': self.id,
            'content': self.content,
            'title': self.title,
            'category': self.category.to_dict(),
            'tags': [tag.to_dict() for tag in self.tags],
        }

    @classmethod
    def from_domain(cls, article: Article) -> Self:
        """
        Create an ArticleDTO from an Article domain object.

        Args:
            article (Article): The Article domain object.

        Returns:
            ArticleDTO: The created ArticleDTO.
        """
        return cls(
            id_=article.id_,
            title=article.title,
            content=article.content,
            category=article.category,
            tags=article.tags
        )


@dataclass
class ArticleListDTO(ArticleBase):
    """
    Data transfer object for a list of Articles.

    Attributes:
        id_ (int): The ID of the article.
        category (CategoryDTO): The category of the article.
        tags (list[TagDTO]): The tags of the article.
    """

    id_: int
    category: CategoryDTO
    tags: list[TagDTO]

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the ArticleListDTO to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the
            ArticleListDTO.
        """
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category.to_dict(),
            'tags': [tag.to_dict() for tag in self.tags],
        }

    @classmethod
    def from_domain(cls, article: Article) -> Self:
        """
        Create an ArticleListDTO from an Article domain object.

        Args:
            article (Article): The Article domain object.

        Returns:
            ArticleListDTO: The created ArticleListDTO.
        """
        return cls(
            id_=article.id_,
            title=article.title,
            category=article.category,
            tags=article.tags
        )


@dataclass
class ArticleCreateDTO(ArticleBase):
    """
    Data transfer object for creating an Article.

    Attributes:
        content (str): The content of the article.
        category_id (int): The ID of the category of the article.
        tags_id (list[int]): The IDs of the tags of the article.
    """

    content: str
    category_id: int
    tags_id: list[int]

    def to_domain(self) -> Article:
        """
        Convert the ArticleCreateDTO to an Article domain object.

        Returns:
            Article: The created Article domain object.
        """
        return Article(
            id_=None,
            title=self.title,
            content=self.content,
            category=self.category_id,
            tags=list(set(self.tags_id))
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """
        Create an ArticleCreateDTO from a dictionary.

        Args:
            data (dict[str, Any]): The dictionary.

        Returns:
            ArticleCreateDTO: The created ArticleCreateDTO.
        """
        return cls(
            title=data['title'],
            content=data['content'],
            category_id=data['category_id'],
            tags_id=data['tags_id']
        )


@dataclass
class ArticleUpdateDTO(ArticleBase):
    """
    Data transfer object for updating an Article.

    Attributes:
        id_ (int): The ID of the article.
        content (str): The content of the article.
        category_id (int): The ID of the category of the article.
        tags_id (list[int]): The IDs of the tags of the article.
    """

    id_: int
    content: str
    category_id: int
    tags_id: list[int]

    def to_domain(self) -> Article:
        """
        Convert the ArticleUpdateDTO to an Article domain object.

        Returns:
            Article: The created Article domain object.
        """
        return Article(
            id_=self.id_,
            title=self.title,
            content=self.content,
            category=self.category_id,
            tags=list(set(self.tags_id))
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """
        Create an ArticleUpdateDTO from a dictionary.

        Args:
            data (dict[str, Any]): The dictionary.

        Returns:
            ArticleUpdateDTO: The created ArticleUpdateDTO.
        """
        return cls(
            id_=data['id'],
            title=data['title'],
            content=data['content'],
            category_id=data['category_id'],
            tags_id=data['tags_id']
        )


@dataclass
class TranslationDTO:
    """
    Data transfer object for a Translation.

    Attributes:
        id_ (int): The ID of the translation.
        language (LanguageDTO): The language of the translation.
        article (ArticleDTO): The article of the translation.
        title (str): The title of the translation.
        content (str): The content of the translation.
    """

    id_: int
    language: LanguageDTO
    article: ArticleDTO
    title: str
    content: str

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the TranslationDTO to a dictionary.

        Returns:
            dict[str, Any]: The dictionary representation of the
            TranslationDTO.
        """
        return {
            'id': self.id_,
            'language': self.language.to_dict(),
            'article': self.article.to_dict(),
            'title': self.title,
            'content': self.content
        }

    @classmethod
    def from_domain(cls, translation: Translation) -> Self:
        """
        Create a TranslationDTO from a Translation domain object.

        Args:
            translation (Translation): The Translation domain object.

        Returns:
            TranslationDTO: The created TranslationDTO.
        """
        return cls(
            id_=translation.id_,
            language=translation.language,
            article=translation.article,
            title=translation.title,
            content=translation.content
        )
