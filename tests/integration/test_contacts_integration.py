import json
import time


import pytest
from app import app
from models import db, Contacts
from faker import Factory
from migrations import generate_fake_contacts

BASE_URL = "http://localhost:5000"

def setup_module(module):
    with app.app_context():
        # Clear the database before running tests
        db.drop_all()
        db.create_all()
        generate_fake_contacts(100)


def teardown_module(module):
    with app.app_context():
        # Drop all tables after running tests
        db.session.remove()
        db.drop_all()



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
    
    
    
    
