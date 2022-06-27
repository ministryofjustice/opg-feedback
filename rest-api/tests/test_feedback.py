import json
import requests
import pytest
import sys
#sys.path.append('../app:..')
from feedback import Feedback

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

    # ensure we don't already have saved data before we start the test
    feedback = Feedback.query.filter_by(comment='Very happy with the service').all()
    assert len(feedback) == 0

    #r = requests.post(
    #    server.url + "/healthcheck", headers=test_headers, data=json.dumps(test_data)
    #)

    r = requests.get(
        url + "/feedback"
    )
    assert r.status_code == 201

    # ensure we have exactly 1 comment saved
    feedback = Feedback.query.filter_by(comment='Very happy with the service').all()
    assert len(feedback) == 1

    db.session.delete(feedback)
    db.session.commit()
