from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePost:
    resource_path = "tag_service.create_tag"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        with patch(f"{base_path}.{self.resource_path}") as mock_create_tag:
            mock_create_tag.side_effect = ApplicationError()
            response = client.post(url_for("tagresource"), json={})

        mock_create_tag.assert_called_once()
        assert 400 == response.status_code

    def test_when_updated(self, client: Client, base_path: str) -> None:
        mock_tag = MagicMock()
        mock_tag.to_dict.return_value = {"id": 1, "name": "test_name"}

        with patch(f"{base_path}.{self.resource_path}") as mock_create_tag:
            mock_create_tag.return_value = mock_tag
            response = client.post(url_for("tagresource"), json={})

        mock_create_tag.assert_called_once()
        assert 201 == response.status_code
        assert {"id": 1, "name": "test_name"} == response.get_json()
