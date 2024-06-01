from articles.infrastructure.storage.boto3 import Boto3Service
from botocore.exceptions import ClientError
from boto3 import resource
import pytest


def test_delete_file(
        conn: resource,
        boto3_service: Boto3Service,
        bucket_name: str
) -> None:
    conn.Bucket(bucket_name).put_object(Key='myfile.txt', Body='content')
    boto3_service.delete_file('myfile.txt')

    with pytest.raises(ClientError) as e:
        conn.Object(bucket_name, 'myfile.txt').load()

    assert 'not found' in str(e.value).lower()
