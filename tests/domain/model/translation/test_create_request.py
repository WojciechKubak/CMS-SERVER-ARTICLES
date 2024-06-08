from tests.factory import TranslationFactory


def test_create_request() -> None:
    translation = TranslationFactory()
    result = translation.create_request(translation.language, translation.article)
    assert translation.language == result.language
    assert translation.article == result.article
    assert not result.is_ready
