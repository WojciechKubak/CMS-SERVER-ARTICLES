from articles.infrastructure.storage.boto3 import Boto3Service
from articles.env_config import (
    S3_ACCESS_KEY_ID,
    S3_SECRET_ACCESS_KEY,
    S3_BUCKET_NAME,
    BUCKET_SUBFOLDER_NAME
)


s3_bucket_manager = Boto3Service(
    S3_ACCESS_KEY_ID,
    S3_SECRET_ACCESS_KEY,
    S3_BUCKET_NAME,
    BUCKET_SUBFOLDER_NAME
)
