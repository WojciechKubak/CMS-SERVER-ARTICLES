from articles.infrastructure.storage.manager import S3BucketManager
import os


s3_bucket_manager = S3BucketManager(
    os.getenv("ACCESS_KEY_ID"),
    os.getenv("SECRET_ACCESS_KEY"),
    os.getenv("BUCKET_NAME"),
    os.getenv("BUCKET_SUBFOLDER_NAME"),
)
