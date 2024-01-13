from articles.infrastructure.storage.manager import S3BucketManager
from articles.infrastructure.adapters.adapters import FileStorageAdapter
from articles.domain.model import Article
from moto import mock_s3
import boto3


@mock_s3
def test_upload_article_content() -> None:
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
    
    file_storage_adapter = FileStorageAdapter(s3_bucket_manager)

    article = Article(
        id_=1, 
        title='title', 
        content='Hello, World!', 
        category=None, 
        tags=[]
    )
    file_path = file_storage_adapter.upload_article_content(article)
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=bucket_subfolder_name)
    assert file_path.startswith(bucket_subfolder_name)
    assert 'Contents' in response
