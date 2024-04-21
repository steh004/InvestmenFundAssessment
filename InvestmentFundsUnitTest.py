import pytest
from InvestmentFundsAPI import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_funds(client):
    response = client.get('/funds')
    assert response.status_code == 200

def test_create_fund(client):
    response = client.post('/funds', json={'fund_id': '3', 'fund_name': 'New Fund'})
    assert response.status_code == 201

def test_get_fund(client):
    response = client.get('/funds/1')
    assert response.status_code == 200

def test_update_performance(client):
    response = client.put('/funds/1', json={'performance': 12.5})
    assert response.status_code == 200

def test_delete_fund(client):
    response = client.delete('/funds/1')
    assert response.status_code == 200

if __name__ == '__main__':
    pytest.main()
