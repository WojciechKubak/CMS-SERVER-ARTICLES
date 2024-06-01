from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import MagicMock, patch


class TestIdResourcePut:
    resource_path = 'article_service.update_article'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(f'{base_path}.{self.resource_path}') as mock_update_article:
            mock_update_article.side_effect = ApplicationError()
            response = client.put(url_for('articleidresource', id_=1), json={})

        mock_update_article.assert_called_once()
        assert 400 == response.status_code
        assert {'message': ApplicationError().message} == response.get_json()

    def test_when_updated(
            self,
            client: Client,
            base_path: str
    ) -> None:
        article_id = 1
        mock_article = MagicMock()
        mock_article.to_dict.return_value = {
            'id': article_id,
            'title': 'test_title'
        }

        with patch(f'{base_path}.{self.resource_path}') as mock_update_article:
            mock_update_article.return_value = mock_article
            response = client.put(
                url_for('articleidresource', id_=article_id), json={})

        mock_update_article.assert_called_once()
        assert 200 == response.status_code
        assert {'id': article_id, 'title': 'test_title'} == response.get_json()
