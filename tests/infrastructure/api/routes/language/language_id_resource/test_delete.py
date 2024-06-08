from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import patch


class TestIdResourceDelete:
    resource_path = "language_service.delete_language"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        with patch(f"{base_path}.{self.resource_path}") as mock_delete_language:
            mock_delete_language.side_effect = ApplicationError()
            response = client.delete(url_for("languageidresource", id_=1))

        mock_delete_language.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_deleted(self, client: Client, base_path: str) -> None:
        language_id = 1

        with patch(f"{base_path}.{self.resource_path}") as mock_delete_language:
            mock_delete_language.return_value = language_id
            response = client.delete(url_for("languageidresource", id_=language_id))

        mock_delete_language.assert_called_once_with(language_id)
        assert 200 == response.status_code
        assert {"id": language_id} == response.json
