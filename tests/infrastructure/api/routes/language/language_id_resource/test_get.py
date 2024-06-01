from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourceGet:
    resource_path = 'language_service.get_language_by_id'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(f'{base_path}.{self.resource_path}') as mock_get_language:
            mock_get_language.side_effect = ApplicationError()
            response = client.get(url_for('languageidresource', id_=1))

        mock_get_language.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_found(self, client: Client, base_path: str) -> None:
        language_id = 1
        mock_language = MagicMock()
        mock_language.to_dict.return_value = {
            'id': language_id,
            'name': 'test_name'
        }

        with patch(f'{base_path}.{self.resource_path}') as mock_get_language:
            mock_get_language.return_value = mock_language
            response = client.get(
                url_for('languageidresource', id_=language_id)
            )

        mock_get_language.assert_called_once_with(language_id)
        assert 200 == response.status_code
        assert {'id': language_id, 'name': 'test_name'} == response.get_json()
