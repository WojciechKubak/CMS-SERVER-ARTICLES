from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePut:
    resource_path = "language_service.update_language"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        with patch(f"{base_path}.{self.resource_path}") as mock_update_language:
            mock_update_language.side_effect = ApplicationError()
            response = client.put(url_for("languageidresource", id_=1), json={})

        mock_update_language.assert_called_once()
        assert 400 == response.status_code
        assert {"message": ApplicationError().message} == response.get_json()

    def test_when_updated(self, client: Client, base_path: str) -> None:
        language_id = 1
        mock_language = MagicMock()
        mock_language.to_dict.return_value = {"id": language_id, "name": "test_name"}

        with patch(f"{base_path}.{self.resource_path}") as mock_update_language:
            mock_update_language.return_value = mock_language
            response = client.put(
                url_for("languageidresource", id_=language_id), json={}
            )

        mock_update_language.assert_called_once()
        assert 200 == response.status_code
        assert {"id": language_id, "name": "test_name"} == response.get_json()
