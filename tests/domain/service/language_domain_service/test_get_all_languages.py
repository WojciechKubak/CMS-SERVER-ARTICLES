from articles.domain.service import LanguageService
from tests.factory import LanguageEntityFactory


class TestGetAllLanguages:

    def test_when_no_languages(self, language_domain_service: LanguageService) -> None:
        result = language_domain_service.get_all_languages()
        assert not result

    def test_when_languages(self, language_domain_service: LanguageService) -> None:
        languages = LanguageEntityFactory.create_batch(5)
        result = language_domain_service.get_all_languages()
        assert len(result) == len(languages)
