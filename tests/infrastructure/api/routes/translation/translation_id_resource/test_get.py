from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourceGet:
    resource_path = 'translation_service.get_translation_by_id'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(
            f'{base_path}.{self.resource_path}'
        ) as mock_get_translation:
            mock_get_translation.side_effect = ApplicationError()
            response = client.get(url_for('translationidresource', id_=1))

        mock_get_translation.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_found(self, client: Client, base_path: str) -> None:
        translation_id = 1
        mock_translation = MagicMock()
        mock_translation.to_dict.return_value = {
            'id': translation_id,
            'is_ready': False
        }

        with patch(
            f'{base_path}.{self.resource_path}'
        ) as mock_get_translation:
            mock_get_translation.return_value = mock_translation
            response = client.get(
                url_for('translationidresource', id_=translation_id)
            )

        mock_get_translation.assert_called_once_with(translation_id)
        assert 200 == response.status_code
        assert {'id': translation_id, 'is_ready': False} == response.get_json()
