import os

from sqlalchemy import create_engine
from src.database.orm import Base


DATABASE_URL = os.getenv('DATABASE_URL')

# SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)
metadata = Base.metadata