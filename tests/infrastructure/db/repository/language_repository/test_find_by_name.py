from articles.infrastructure.persistance.repository import LanguageRepository
from tests.factory import LanguageEntityFactory


def test_find_by_name(language_repository: LanguageRepository) -> None:
    language = LanguageEntityFactory()
    result = language_repository.find_by_name(language.name)
    assert language == result
