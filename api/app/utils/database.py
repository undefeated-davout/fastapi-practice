import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL設定
DATABASE_URL = "mysql://{user_name}:{password}@{host_name}:{port}/{db_name}?charset=utf8".format(
    user_name=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    host_name=os.environ["MYSQL_HOST"],
    port=os.environ["MYSQL_TCP_PORT"],
    db_name=os.environ["MYSQL_DATABASE"],
)

engine = create_engine(DATABASE_URL, encoding="utf-8", echo=True)

sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
