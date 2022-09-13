from flask import Flask
from opgflaskfront import create_flask_app
from .feedbackfront_blueprint import feedbackfront_blueprint


def create_feedback_app(name: str, force_https=False) -> Flask:
    app = create_flask_app("feedbackfront", force_https)

    app.register_blueprint(feedbackfront_blueprint)
    return app
