from dotenv import load_dotenv
import logging
import os


load_dotenv()
logging.basicConfig(level=logging.INFO)

DEBUG_MODE = int(os.environ.get('DEBUG', 1))

BROKER_URI = os.getenv('BROKER_URI')
GROUP_ID = os.getenv('GROUP_ID')
TRANSLATED_ARTICLES_TOPIC = os.getenv('TRANSLATED_ARTICLES_TOPIC')
TRANSLATION_REQUESTS_TOPIC = os.getenv('TRANSLATION_REQUESTS_TOPIC')
LANGUAGE_CHANGES_TOPIC = os.getenv('LANGUAGE_CHANGES_TOPIC')

S3_ACCESS_KEY_ID = os.getenv("S3_ACCESS_KEY_ID")
S3_SECRET_ACCESS_KEY = os.getenv("S3_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
BUCKET_SUBFOLDER_NAME = os.getenv("BUCKET_SUBFOLDER_NAME")
