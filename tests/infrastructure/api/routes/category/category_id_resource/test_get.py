from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourceGet:
    resource_path = "category_service.get_category_by_id"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        with patch(f"{base_path}.{self.resource_path}") as mock_get_category:
            mock_get_category.side_effect = ApplicationError()
            response = client.get(url_for("categoryidresource", id_=1))

        mock_get_category.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_found(self, client: Client, base_path: str) -> None:
        category_id = 1
        mock_category = MagicMock()
        mock_category.to_dict.return_value = {"id": category_id, "name": "test_name"}

        with patch(f"{base_path}.{self.resource_path}") as mock_get_category:
            mock_get_category.return_value = mock_category
            response = client.get(url_for("categoryidresource", id_=category_id))

        mock_get_category.assert_called_once_with(category_id)
        assert 200 == response.status_code
        assert {"id": category_id, "name": "test_name"} == response.get_json()
