from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourceGet:
    resource_path = "tag_service.get_tag_by_id"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        with patch(f"{base_path}.{self.resource_path}") as mock_get_tag:
            mock_get_tag.side_effect = ApplicationError()
            response = client.get(url_for("tagidresource", id_=1))

        mock_get_tag.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_found(self, client: Client, base_path: str) -> None:
        tag_id = 1
        mock_tag = MagicMock()
        mock_tag.to_dict.return_value = {"id": tag_id, "name": "test_name"}

        with patch(f"{base_path}.{self.resource_path}") as mock_get_tag:
            mock_get_tag.return_value = mock_tag
            response = client.get(url_for("tagidresource", id_=tag_id))

        mock_get_tag.assert_called_once_with(tag_id)
        assert 200 == response.status_code
        assert {"id": tag_id, "name": "test_name"} == response.get_json()
