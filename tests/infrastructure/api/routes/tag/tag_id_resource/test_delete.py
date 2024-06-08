from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import patch


class TestIdResourceDelete:
    resource_path = "tag_service.delete_tag"

    def test_when_application_error(self, client: Client, base_path: str) -> None:
        with patch(f"{base_path}.{self.resource_path}") as mock_delete_tag:
            mock_delete_tag.side_effect = ApplicationError()
            response = client.delete(url_for("tagidresource", id_=1))

        mock_delete_tag.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_deleted(self, client: Client, base_path: str) -> None:
        tag_id = 1

        with patch(f"{base_path}.{self.resource_path}") as mock_delete_tag:
            mock_delete_tag.return_value = tag_id
            response = client.delete(url_for("tagidresource", id_=tag_id))

        mock_delete_tag.assert_called_once_with(tag_id)
        assert 200 == response.status_code
        assert {"id": tag_id} == response.json
