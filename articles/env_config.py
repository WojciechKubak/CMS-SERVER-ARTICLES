from dotenv import load_dotenv
import os

load_dotenv()

DEBUG_MODE = int(os.environ.get('DEBUG', 1))

BROKER_URI = os.getenv('BROKER_URI')
GROUP_ID = os.getenv('GROUP_ID')
TRANSLATED_ARTICLES_TOPIC = os.getenv('TRANSLATED_ARTICLES_TOPIC')
TRANSLATION_REQUESTS_TOPIC = os.getenv('TRANSLATION_REQUESTS_TOPIC')
TRANSLATION_UPDATES_TOPIC = os.getenv('TRANSLATION_UPDATES_TOPIC')

S3_BUCKET_CONFIG = {
    'access_key_id': os.getenv("ACCESS_KEY_ID"),
    'secret_access_key': os.getenv("SECRET_ACCESS_KEY"),
    'bucket_name': os.getenv("BUCKET_NAME"),
    'bucket_subfolder_name': os.getenv("BUCKET_SUBFOLDER_NAME")
} 
DATABASE_URI = 'mysql://user:user1234@mysql-articles:3310/db_1' \
    if DEBUG_MODE else os.getenv("PRODUCTION_DB_URI")
