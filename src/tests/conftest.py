import pytest
from starlette.testclient import TestClient
from app.main import app

@pytest.fixture(scope="modeul")
def test_app():
    client = TestClient(app)
    yield client # testing happens here
    