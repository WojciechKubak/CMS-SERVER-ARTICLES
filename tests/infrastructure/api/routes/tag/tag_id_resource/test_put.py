from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePut:
    resource_path = 'tag_service.update_tag'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(
            f'{base_path}.{self.resource_path}'
        ) as mock_update_tag:
            mock_update_tag.side_effect = ApplicationError()
            response = client.put(
                url_for('tagidresource', id_=1),
                json={}
            )

        mock_update_tag.assert_called_once()
        assert 400 == response.status_code
        assert {'message': ApplicationError().message} == response.get_json()

    def test_when_updated(
            self,
            client: Client,
            base_path: str
    ) -> None:
        tag_id = 1
        mock_tag = MagicMock()
        mock_tag.to_dict.return_value = {
            'id': tag_id,
            'name': 'test_name'
        }

        with patch(
            f'{base_path}.{self.resource_path}'
        ) as mock_update_tag:
            mock_update_tag.return_value = mock_tag
            response = client.put(
                url_for('tagidresource', id_=tag_id), json={})

        mock_update_tag.assert_called_once()
        assert 200 == response.status_code
        assert {'id': tag_id, 'name': 'test_name'} == response.get_json()
