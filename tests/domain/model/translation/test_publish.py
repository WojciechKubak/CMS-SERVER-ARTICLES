from tests.factory import TranslationFactory


def test_publish() -> None:
    translation = TranslationFactory(is_ready=False)
    content_path = "path/to/content"

    result = translation.publish(content_path)

    assert content_path == result.content
    assert result.is_ready
