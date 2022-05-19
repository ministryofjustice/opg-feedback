import json
import requests
import pytest

url = "http://localhost:8005"

def test_healthcheck():
    expected_return = {'health': 'healthy'}

    r = requests.get(
        url + "/healthcheck"
    )

    assert r.status_code == 200
    assert r.json() == expected_return

def test_save_feedback():

    test_data = {}

    test_headers = {"Content-Type": "application/json"}

    #r = requests.post(
    #    server.url + "/healthcheck", headers=test_headers, data=json.dumps(test_data)
    #)

    r = requests.get(
        url + "/feedback"
    )
    assert r.status_code == 201
#    assert r.json() == expected_return
