from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePost:
    resource_path = "category_service.create_category"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        with patch(f"{base_path}.{self.resource_path}") as mock_create_category:
            mock_create_category.side_effect = ApplicationError()
            response = client.post(url_for("categoryresource"), json={})

        mock_create_category.assert_called_once()
        assert 400 == response.status_code

    def test_when_updated(self, client: Client, base_path: str) -> None:
        mock_category = MagicMock()
        mock_category.to_dict.return_value = {"id": 1, "name": "test_name"}

        with patch(f"{base_path}.{self.resource_path}") as mock_create_category:
            mock_create_category.return_value = mock_category
            response = client.post(url_for("categoryresource"), json={})

        mock_create_category.assert_called_once()
        assert 201 == response.status_code
        assert {"id": 1, "name": "test_name"} == response.get_json()
