from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import patch


class TestIdResourceDelete:
    resource_path = 'category_service.delete_category'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(
            f'{base_path}.{self.resource_path}'
        ) as mock_delete_category:
            mock_delete_category.side_effect = ApplicationError()
            response = client.delete(url_for('categoryidresource', id_=1))

        mock_delete_category.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_deleted(self, client: Client, base_path: str) -> None:
        category_id = 1

        with patch(
            f'{base_path}.{self.resource_path}'
        ) as mock_delete_category:
            mock_delete_category.return_value = category_id
            response = client.delete(url_for(
                'categoryidresource',
                id_=category_id)
            )

        mock_delete_category.assert_called_once_with(category_id)
        assert 200 == response.status_code
        assert {'id': category_id} == response.json
