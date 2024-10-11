import os
from dotenv import load_dotenv, find_dotenv
import pytest
import mongomock
import requests
from todo_app import app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Use the app to create a test_client that can be used in our tests.
    with mongomock.patch(servers=((os.environ.get('AZURE_COSMOS_DB_CONNECT'), 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(monkeypatch, client):
    # This replaces any call to requests.get with our own function
    monkeypatch.setattr(requests, 'get', stub)

    response = client.get('/')
    assert response.status_code == 200
    #assert 'Test card' in response.data.decode()

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def raise_for_status(self):
        pass

    def json(self):
        return self.fake_response_data

def stub():
    fake_response_data = mongomock.MongoClient().db.collection
    objects = [{'title': 'Test card','status':'open'},
                        {'title': 'New card','status':'open'}]
    for obj in objects:
        obj['_id'] = fake_response_data.insert_one(obj).inserted_id
    return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

