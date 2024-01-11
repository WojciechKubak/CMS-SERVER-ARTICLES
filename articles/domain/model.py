from dataclasses import dataclass


@dataclass
class Category:
    id_: int
    name: str
    description: str


@dataclass
class Tag:
    id_: int
    name: str


@dataclass
class Article:
    id_: int
    title: str
    content: str
    category: Category
    tags: list[Tag]

    def with_category_and_tags(self, category: Category, tags: list[Tag]) -> 'Article':
        return Article(
            id_=self.id_,
            title=self.title,
            content=self.content,
            category=category,
            tags=tags
        )
