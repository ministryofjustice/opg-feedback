from flask import Flask
from opgfeedbackfront import create_feedback_app


def test_create_feedback_app():
    app = create_feedback_app("bob", force_https=False)
    assert isinstance(app, Flask)

    response = app.test_client().get("/")
    assert response.status_code == 200

    response = app.test_client().get("/completed-feedback")
    assert response.status_code == 200
