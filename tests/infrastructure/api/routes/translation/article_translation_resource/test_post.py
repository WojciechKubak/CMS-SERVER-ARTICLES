from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePost:
    resource_path = "translation_service.request_translation"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        article_id, language_id = 1, 1

        with patch(f"{base_path}.{self.resource_path}") as mock_create_translation:
            mock_create_translation.side_effect = ApplicationError()
            response = client.post(
                url_for(
                    "articletranslationresource",
                    article_id=article_id,
                    language_id=language_id,
                )
            )

        mock_create_translation.assert_called_once_with(article_id, language_id)
        assert 400 == response.status_code

    def test_when_updated(self, client: Client, base_path: str) -> None:
        article_id, language_id = 1, 1
        mock_translation = MagicMock()
        mock_translation.to_dict.return_value = {"id": 1, "is_ready": False}

        with patch(f"{base_path}.{self.resource_path}") as mock_create_translation:
            mock_create_translation.return_value = mock_translation
            response = client.post(
                url_for(
                    "articletranslationresource",
                    article_id=article_id,
                    language_id=language_id,
                )
            )

        mock_create_translation.assert_called_once_with(article_id, language_id)
        assert 201 == response.status_code
        assert {"id": 1, "is_ready": False} == response.get_json()
