import pytest
from starlette.testclient import TestClient

from src.main import app


@pytest.fixture(scope="session")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here