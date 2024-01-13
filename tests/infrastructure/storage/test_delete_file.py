from articles.infrastructure.storage.manager import S3BucketManager
from moto import mock_s3
import boto3


@mock_s3
def test_delete_file() -> None:
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

    s3_bucket_manager.delete_file(file_path)

    response = s3.list_objects_v2(Bucket=bucket_name)
    assert 'Contents' not in response
