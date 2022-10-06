from flask import Flask
from opgflaskfront import create_flask_app
from jinja2 import PackageLoader
from .feedbackfront_blueprint import feedbackfront_blueprint
from jinja2 import PrefixLoader
from flask_wtf.csrf import CSRFProtect
from govuk_frontend_wtf.main import WTFormsHelpers


def create_feedback_app(name: str, force_https=False) -> Flask:
    print(force_https)
    app = create_flask_app(
        "feedbackfront",
        force_https=force_https,
        loaders=[
            PackageLoader("opgfeedbackfront"),
            PrefixLoader({"govuk_frontend_wtf": PackageLoader("govuk_frontend_wtf")}),
        ],
    )

    app.register_blueprint(feedbackfront_blueprint)
    return app
