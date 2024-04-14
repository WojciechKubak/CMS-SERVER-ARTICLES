from articles.infrastructure.storage.manager import S3BucketManager
from articles.settings import S3_BUCKET_CONFIG


s3_bucket_manager = S3BucketManager(**S3_BUCKET_CONFIG)
