import pytest
import tempfile
import os
from app import app


@pytest.fixture
def client():
    with tempfile.TemporaryDirectory() as tmpdir:
        app.config['TESTING'] = True
        os.environ['DATA_FILE'] = os.path.join(tmpdir, 'items.json')
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