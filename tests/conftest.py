import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.main import app, get_db
from app.database import Base

TEST_DATABASE_URL = (
    "postgresql://admin:admin@localhost:5433/pokemon_test_db"
)

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def sub_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = sub_get_db

@pytest.fixture()
def client():

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as client:
        yield client

    Base.metadata.drop_all(bind=engine)