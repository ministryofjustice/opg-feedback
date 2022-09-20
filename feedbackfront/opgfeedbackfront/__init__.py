from flask import Flask
from opgflaskfront import create_flask_app
from jinja2 import PackageLoader
from .feedbackfront_blueprint import feedbackfront_blueprint


def create_feedback_app(name: str, force_https=False) -> Flask:
    print(force_https)
    app = create_flask_app(
        "feedbackfront",
        force_https=force_https,
        loaders=[PackageLoader("opgfeedbackfront")],
    )

    app.register_blueprint(feedbackfront_blueprint)
    return app
