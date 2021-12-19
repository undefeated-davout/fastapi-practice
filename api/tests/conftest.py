from typing import Generator

import pytest
from app.main import app
from app.utils.database import Base, get_db
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

# 読み込みミス防止のためハードコーディング
MYSQL_HOST = "testdb"
MYSQL_DATABASE = "testdb"
MYSQL_TCP_PORT = 3309
MYSQL_ROOT_PASSWORD = "testrootpassword"
MYSQL_USER = "testuser"
MYSQL_PASSWORD = "testpassword"


def get_engine_session() -> tuple[Engine, sessionmaker]:
    TEST_DB_URL = "mysql://{user_name}:{password}@{host_name}:{port}/{db_name}?charset=utf8".format(
        user_name=MYSQL_USER,
        password=MYSQL_PASSWORD,
        host_name=MYSQL_HOST,
        port=MYSQL_TCP_PORT,
        db_name=MYSQL_DATABASE,
    )
    test_engine = create_engine(TEST_DB_URL, encoding="utf-8", echo=True)
    test_session_local = sessionmaker(
        bind=test_engine, autocommit=False, autoflush=False
    )
    return test_engine, test_session_local


@pytest.fixture(scope="session")
def db() -> Generator:
    _, test_session_local = get_engine_session()
    yield test_session_local()


@pytest.fixture(scope="module")
def client() -> Generator:
    test_engine, test_session_local = get_engine_session()

    # テスト用テーブルはテスト関数ごとに初期化
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)

    # DIを使ってFastAPIのDBの向き先をテスト用DBに変更
    def get_test_db():
        db = test_session_local()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = get_test_db
    client = TestClient(app)
    yield client
