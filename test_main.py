'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'abc123abc1234'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODc5NTExMDcsIm5iZiI6MTU4Njc0MTUwNywiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSJ9.N8_D7hA0DTickReO_QrZ76fAq5GyDf0pEg02B_6iUbo'
EMAIL = 'test@gmail.com'
PASSWORD = 'test'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
