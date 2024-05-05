from articles.infrastructure.storage.manager import S3BucketManager
from articles.infrastructure.adapters.adapters import FileStorageAdapter
from articles.domain.model import Article
from moto import mock_aws
import boto3


@mock_aws
def test_read_article_content() -> None:
    bucket_name = 'my-bucket'
    bucket_subfolder_name = 'my-subfolder'
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)

    s3_bucket_manager = S3BucketManager(
        access_key_id='',
        secret_access_key='',
        bucket_name=bucket_name,
        bucket_subfolder_name=bucket_subfolder_name
    )

    content = 'Hello, World!'
    file_path = s3_bucket_manager.upload_to_file(content)

    file_storage_adapter = FileStorageAdapter(s3_bucket_manager)
    article = Article(
        id_=1, 
        title='title', 
        content=file_path, 
        category=None, 
        tags=[]
    )
    result = file_storage_adapter.read_content(article.content)

    response = s3.get_object(Bucket=bucket_name, Key=file_path)
    content = response['Body'].read().decode('utf-8')

    assert content == result
