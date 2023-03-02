import os

from database import Database
from sqlalchemy import create_engine, MetaData

DATABASE_URL = os.getenv("DATABASE_URL")