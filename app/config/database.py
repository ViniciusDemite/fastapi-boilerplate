import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = (
  f'mysql+pymysql://'
  f'{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@'
  f'{os.getenv("MYSQL_HOST")}:{os.getenv("MYSQL_PORT")}/'
  f'{os.getenv("MYSQL_DATABASE")}?charset=utf8'
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
