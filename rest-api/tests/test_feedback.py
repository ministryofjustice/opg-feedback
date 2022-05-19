import json
import requests
import pytest

def test_save_feedback():

    url = "http://localhost:8005"

    test_data = {}

    test_headers = {"Content-Type": "application/json"}

    expected_return = {'health': 'healthy'}

    #r = requests.post(
    #    server.url + "/healthcheck", headers=test_headers, data=json.dumps(test_data)
    #)

    r = requests.get(
        url + "/healthcheck"
    )
    assert r.status_code == 200
    assert r.json() == expected_return
