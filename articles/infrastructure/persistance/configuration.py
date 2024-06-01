from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy


Base = declarative_base()
sa = SQLAlchemy(model_class=Base)
