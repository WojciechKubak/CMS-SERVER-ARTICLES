from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePost:
    resource_path = "language_service.create_language"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        with patch(f"{base_path}.{self.resource_path}") as mock_create_language:
            mock_create_language.side_effect = ApplicationError()
            response = client.post(url_for("languageresource"), json={})

        mock_create_language.assert_called_once()
        assert 400 == response.status_code

    def test_when_updated(self, client: Client, base_path: str) -> None:
        mock_language = MagicMock()
        mock_language.to_dict.return_value = {"id": 1, "name": "test_name"}

        with patch(f"{base_path}.{self.resource_path}") as mock_create_language:
            mock_create_language.return_value = mock_language
            response = client.post(url_for("languageresource"), json={})

        mock_create_language.assert_called_once()
        assert 201 == response.status_code
        assert {"id": 1, "name": "test_name"} == response.get_json()
