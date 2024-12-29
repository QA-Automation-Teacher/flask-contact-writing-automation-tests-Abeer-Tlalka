import json
import time

BASE_URL = "http://localhost:5000"

def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_get_contacts(client):
    response = client.get(BASE_URL + "/api/contacts")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    

def test_get_response_time_is_less_than_400ms(client):
    user_id = 1
    """Test to check if the PUT response time is less than 400ms."""
    start = time.time()
    response = client.get(BASE_URL + "/api/contacts")
    end = time.time()
    
    assert end - start < 0.4, "PUT response time is too slow"
        