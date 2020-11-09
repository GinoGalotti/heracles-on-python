import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_gets_200(client):
    res = client.get('/')
    assert res.status_code == 200