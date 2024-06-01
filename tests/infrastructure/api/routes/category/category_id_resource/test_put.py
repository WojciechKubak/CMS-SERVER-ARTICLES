from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePut:
    resource_path = 'category_service.update_category'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(
            f'{base_path}.{self.resource_path}'
        ) as mock_update_category:
            mock_update_category.side_effect = ApplicationError()
            response = client.put(
                url_for('categoryidresource', id_=1),
                json={}
            )

        mock_update_category.assert_called_once()
        assert 400 == response.status_code
        assert {'message': ApplicationError().message} == response.get_json()

    def test_when_updated(
            self,
            client: Client,
            base_path: str
    ) -> None:
        category_id = 1
        mock_category = MagicMock()
        mock_category.to_dict.return_value = {
            'id': category_id,
            'name': 'test_name'
        }

        with patch(
            f'{base_path}.{self.resource_path}'
        ) as mock_update_category:
            mock_update_category.return_value = mock_category
            response = client.put(
                url_for('categoryidresource', id_=category_id), json={})

        mock_update_category.assert_called_once()
        assert 200 == response.status_code
        assert {'id': category_id, 'name': 'test_name'} == response.get_json()
