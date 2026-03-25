import json
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def get_json(response):
    return json.loads(response.data)


class TestIndex:
    def test_root_returns_endpoints(self, client):
        resp = client.get('/api/v1/')
        assert resp.status_code == 200
        data = get_json(resp)
        assert 'endpoints' in data


class TestGetStates:
    def test_returns_all_states(self, client):
        resp = client.get('/api/v1/states')
        assert resp.status_code == 200
        data = get_json(resp)
        assert len(data) == 37

    def test_state_has_required_fields(self, client):
        resp = client.get('/api/v1/states')
        state = get_json(resp)[0]
        assert 'name' in state
        assert 'capital' in state
        assert 'latitude' in state
        assert 'longitude' in state


class TestGetState:
    def test_by_name(self, client):
        resp = client.get('/api/v1/state/lagos')
        assert resp.status_code == 200
        data = get_json(resp)
        assert data['name'] == 'Lagos'
        assert data['capital'] == 'Ikeja'

    def test_by_code(self, client):
        resp = client.get('/api/v1/state/LA')
        assert resp.status_code == 200
        data = get_json(resp)
        assert data['name'] == 'Lagos'

    def test_case_insensitive(self, client):
        resp = client.get('/api/v1/state/LAGOS')
        assert resp.status_code == 200
        assert get_json(resp)['name'] == 'Lagos'

    def test_not_found(self, client):
        resp = client.get('/api/v1/state/nonexistent')
        assert resp.status_code == 404
        assert 'message' in get_json(resp)

    def test_single_char_not_found(self, client):
        resp = client.get('/api/v1/state/x')
        assert resp.status_code == 404


class TestGetLGAs:
    def test_returns_lgas(self, client):
        resp = client.get('/api/v1/state/lagos/lgas')
        assert resp.status_code == 200
        data = get_json(resp)
        assert len(data) == 20
        assert all('name' in lga for lga in data)

    def test_not_found(self, client):
        resp = client.get('/api/v1/state/nonexistent/lgas')
        assert resp.status_code == 404


class TestGetCities:
    def test_returns_cities(self, client):
        resp = client.get('/api/v1/state/lagos/cities')
        assert resp.status_code == 200
        data = get_json(resp)
        assert len(data) > 0
        assert all('name' in city for city in data)

    def test_not_found(self, client):
        resp = client.get('/api/v1/state/nonexistent/cities')
        assert resp.status_code == 404


class TestCORS:
    def test_cors_headers(self, client):
        resp = client.get('/api/v1/states')
        assert resp.headers.get('Access-Control-Allow-Origin') == '*'
