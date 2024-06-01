from articles.infrastructure.api.errors import ApplicationError
from flask.testing import Client
from flask import url_for
from unittest.mock import patch


class TestIdResourceDelete:
    resource_path = 'article_service.delete_article'

    def test_when_application_error(
            self,
            client: Client,
            base_path: str
    ) -> None:
        with patch(f'{base_path}.{self.resource_path}') as mock_delete_article:
            mock_delete_article.side_effect = ApplicationError()
            response = client.delete(url_for('articleidresource', id_=1))

        mock_delete_article.assert_called_once_with(1)
        assert 400 == response.status_code

    def test_when_deleted(self, client: Client, base_path: str) -> None:
        article_id = 1

        with patch(f'{base_path}.{self.resource_path}') as mock_delete_article:
            mock_delete_article.return_value = article_id
            response = client.delete(url_for(
                'articleidresource',
                id_=article_id)
            )

        mock_delete_article.assert_called_once_with(article_id)
        assert 200 == response.status_code
        assert {'id': article_id} == response.json
