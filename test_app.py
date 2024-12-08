import pytest
from app00 import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert f'Shkruaj diçka' in response.data
