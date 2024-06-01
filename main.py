from articles.env_config import DEBUG_MODE
from articles.app import create_app
from articles.config import DevelopmentConfig, ProductionConfig


app = create_app(DevelopmentConfig if DEBUG_MODE else ProductionConfig)
