from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourceGet:
    resource_path = 'article_service.get_article_by_id'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(f'{base_path}.{self.resource_path}') as mock_get_article:
            mock_get_article.side_effect = ApplicationError()
            response = client.get(url_for('articleidresource', id_=1))

        mock_get_article.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_found(self, client: Client, base_path: str) -> None:
        article_id = 1
        mock_article = MagicMock()
        mock_article.to_dict.return_value = {
            'id': article_id,
            'title': 'test_title'
        }

        with patch(f'{base_path}.{self.resource_path}') as mock_get_article:
            mock_get_article.return_value = mock_article
            response = client.get(url_for('articleidresource', id_=article_id))

        mock_get_article.assert_called_once_with(article_id)
        assert 200 == response.status_code
        assert {'id': article_id, 'title': 'test_title'} == response.get_json()
