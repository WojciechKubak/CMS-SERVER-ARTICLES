from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePost:
    resource_path = 'article_service.create_article'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(f'{base_path}.{self.resource_path}') as mock_create_article:
            mock_create_article.side_effect = ApplicationError()
            response = client.post(url_for('articleresource'), json={})

        mock_create_article.assert_called_once()
        assert 400 == response.status_code

    def test_when_updated(
            self,
            client: Client,
            base_path: str
    ) -> None:
        mock_article = MagicMock()
        mock_article.to_dict.return_value = {
            'id': 1,
            'title': 'test_title'
        }

        with patch(f'{base_path}.{self.resource_path}') as mock_create_article:
            mock_create_article.return_value = mock_article
            response = client.post(url_for('articleresource'), json={})

        mock_create_article.assert_called_once()
        assert 201 == response.status_code
        assert {'id': 1, 'title': 'test_title'} == response.get_json()
