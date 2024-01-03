import pytest
from httpx import AsyncClient

from src.deps import get_db
from src.main import app


from starlette.testclient import TestClient


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    test_api_client = TestClient(app)

    yield test_api_client
    del app.dependency_overrides[get_db]


@pytest.fixture(scope="function")
async def async_client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as client:
        print("Client is ready")
        yield client

    del app.dependency_overrides[get_db]
