"""
Unit tests for the Flask application
"""
import pytest
from main import app

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_get_info(client):
    """Test info endpoint"""
    response = client.get('/api/v1/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'app_name' in data
    assert 'version' in data

def test_echo_endpoint(client):
    """Test echo endpoint"""
    test_data = {'test': 'data', 'value': 123}
    response = client.post('/api/v1/echo', json=test_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Echo successful'
    assert data['received_data'] == test_data

def test_metrics_endpoint(client):
    """Test metrics endpoint"""
    response = client.get('/api/v1/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'requests_processed' in data

