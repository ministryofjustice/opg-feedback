import json
import requests
import pytest
import sys

from opgfeedbackapi.feedback import Feedback
from opgflaskapi import *

import os

# create feedback flask app to test against, pointing at local postgres instance
postgres_uri = "postgresql://{}:{}@{}/{}".format(
    os.getenv("POSTGRES_USERNAME"),
    os.getenv("POSTGRES_PASSWORD"),
    "localhost",
    os.getenv("POSTGRES_NAME"),
)

api = create_flask_app("feedback", postgres_uri)
url = "http://localhost:9004"

# TODO DO NOT MERGE - next coding step is to get the token from AWS secretsmanager
test_headers = {
    "Authorization": "Bearer secret-token-1",
    "Content-Type": "application/json",
}


def test_healthcheck():
    expected_return = {"health": "healthy"}

    r = requests.get(url + "/healthcheck")

    assert r.status_code == 200
    assert r.json() == expected_return


def test_save_feedback():
    test_data = {"rating": 1, "comment": "Very happy with the service"}

    # ensure we don't already have saved data before we start the test
    feedback = (
        api.database.query(Feedback)
        .filter(Feedback.comment == "Very happy with the service")
        .all()
    )
    assert len(feedback) == 0

    r = requests.post(
        url + "/feedback", headers=test_headers, data=json.dumps(test_data)
    )

    assert r.status_code == 201

    # ensure we have exactly 1 comment saved
    feedback = (
        api.database.query(Feedback)
        .filter(Feedback.comment == "Very happy with the service")
        .all()
    )
    assert len(feedback) == 1

    api.database.delete(Feedback, feedback[0].id)


def test_save_feedback_with_data_but_missing_content_type():
    test_data = {"rating": 1, "comment": "Very happy with the service"}
    test_headers_without_content_type = {"Authorization": "Bearer secret-token-1"}

    r = requests.post(
        url + "/feedback",
        headers=test_headers_without_content_type,
        data=json.dumps(test_data),
    )

    assert r.status_code == 400


def test_save_feedback_without_auth_token():
    test_data = {"rating": 1, "comment": "Very happy with the service"}
    test_headers_without_auth_token = {"Content-Type": "application/json"}

    r = requests.post(
        url + "/feedback",
        headers=test_headers_without_auth_token,
        data=json.dumps(test_data),
    )

    assert r.status_code == 401


def test_save_feedback_with_missing_rating():
    test_data = {"comment": "Very happy with the service"}

    r = requests.post(
        url + "/feedback", headers=test_headers, data=json.dumps(test_data)
    )

    assert r.status_code == 400


def test_save_feedback_with_missing_comment():
    test_data = {"rating": 1}

    r = requests.post(
        url + "/feedback", headers=test_headers, data=json.dumps(test_data)
    )

    assert r.status_code == 400
