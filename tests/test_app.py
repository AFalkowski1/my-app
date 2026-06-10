import os
import tempfile
import pytest

os.environ['DATA_FILE'] = os.path.join(tempfile.mkdtemp(), 'items.json')

from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200


def test_get_items(client):
    res = client.get('/api/items')
    assert res.status_code == 200


def test_add_item(client):
    res = client.post(
        '/api/items',
        json={"name": "test"},
        content_type='application/json'
    )
    assert res.status_code == 201