class DomainError(Exception):
    def __init__(self, message="Domain error"):
        self.message = message
        super().__init__(self.message)


class CategoryNameExistsError(DomainError):
    def __init__(self, message="Category name already exists"):
        self.message = message
        super().__init__(self.message)


class ArticleTitleExistsError(DomainError):
    def __init__(self, message="Title already exists"):
        self.message = message
        super().__init__(self.message)


class CategoryNotFoundError(DomainError):
    def __init__(self, message="Category does not exist"):
        self.message = message
        super().__init__(self.message)


class TagNotFoundError(DomainError):
    def __init__(self, message="Tag does not exist"):
        self.message = message
        super().__init__(self.message)


class ArticleNotFoundError(DomainError):
    def __init__(self, message="Article does not exist"):
        self.message = message
        super().__init__(self.message)


class TagNameExistsError(DomainError):
    def __init__(self, message="Tag name already exists"):
        self.message = message
        super().__init__(self.message)


class TranslationNotFoundError(DomainError):
    def __init__(self, message="Translation does not exist"):
        self.message = message
        super().__init__(self.message)


class LanguageNotFoundError(DomainError):
    def __init__(self, message="Language does not exist"):
        self.message = message
        super().__init__(self.message)


class LanguageNameExistsError(DomainError):
    def __init__(self, message="Language name already exists"):
        self.message = message
        super().__init__(self.message)


class TranslationExistsError(DomainError):
    def __init__(self, message="Translation already exists"):
        self.message = message
        super().__init__(self.message)


class TranslationPublishedError(DomainError):
    def __init__(self, message="Translation already published"):
        self.message = message
        super().__init__(self.message)
