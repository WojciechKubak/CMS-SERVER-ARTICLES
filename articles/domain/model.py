from dataclasses import dataclass
from typing import Self


@dataclass
class Category:
    """
    Data class representing a Category.

    Attributes:
        id_ (int | None): The ID of the category. None if the category
        is not yet persisted.
        name (str): The name of the category.
        description (str | None): The description of the category. Can be None.
    """

    id_: int | None
    name: str
    description: str | None


@dataclass
class Tag:
    """
    Data class representing a Tag.

    Attributes:
        id_ (int | None): The ID of the tag. None if the tag
        is not yet persisted.
        name (str): The name of the tag.
    """

    id_: int | None
    name: str


@dataclass
class Language:
    """
    Data class representing a Language.

    Attributes:
        id_ (int | None): The ID of the language. None if the language is not
        yet persisted.
        name (str): The name of the language.
        code (str): The code of the language.
    """

    id_: int | None
    name: str
    code: str


@dataclass
class Article:
    """
    Data class representing an Article.

    Attributes:
        id_ (int | None): The ID of the article. None if the article
        is not yet persisted.
        title (str): The title of the article.
        content (str): The content of the article.
        category (Category | int): The category of the article.
        tags (list[Tag] | list[int]): The tags of the article.
    """

    id_: int | None
    title: str
    content: str
    category: Category | int
    tags: list[Tag] | list[int]

    def change_category_and_tags(self, category: Category, tags: list[Tag]) -> Self:
        """
        Method to change the category and tags of the article.

        Args:
            category (Category): The new category of the article.
            tags (list[Tag]): The new tags of the article.

        Returns:
            Article: The updated article with the new category and tags.
        """
        return self.__class__(
            id_=self.id_,
            title=self.title,
            content=self.content,
            category=category,
            tags=tags,
        )

    def change_content(self, content: str) -> Self:
        """
        Method to change the content of the article.

        Args:
            content (str): The new content of the article.

        Returns:
            Article: The updated article with the new content.
        """
        return self.__class__(
            id_=self.id_,
            title=self.title,
            content=content,
            category=self.category,
            tags=self.tags,
        )


@dataclass
class Translation:
    """
    Data class representing a Translation.

    Attributes:
        id_ (int | None): The ID of the translation. None if the translation
        is not yet persisted.
        language (Language): The language of the translation.
        content (str): The content of the translation.
        is_ready (bool): Whether the translation is ready.
        article (Article): The article that the translation is for.
    """

    id_: int | None
    language: Language
    content: str
    is_ready: bool
    article: Article

    def publish(self, content_path: str) -> Self:
        """
        Method to publish the translation.

        Args:
            content_path (str): The path to the content of the translation.

        Returns:
            Translation: The updated translation with the new content
            path and is_ready set to True.
        """
        return self.__class__(
            id_=self.id_,
            content=content_path,
            language=self.language,
            is_ready=True,
            article=self.article,
        )

    @classmethod
    def create_request(cls, language: Language, article: Article) -> Self:
        """
        Class method to create a Translation request.

        Args:
            language (Language): The language of the translation.
            article (Article): The article that the translation is for.

        Returns:
            Translation: The created Translation request with is_ready
            set to False.
        """
        return cls(
            id_=None, content=None, language=language, is_ready=False, article=article
        )
