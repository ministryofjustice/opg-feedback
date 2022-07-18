import os
from opgflaskapi import create_flask_app

postgres_uri = "postgresql://{}:{}@{}/{}".format(
    os.getenv("POSTGRES_USERNAME"),
    os.getenv("POSTGRES_PASSWORD"),
    os.getenv("POSTGRES_HOSTNAME"),
    os.getenv("POSTGRES_NAME"),
)

api = create_flask_app("feedback", postgres_uri)

from .feedback_blueprint import feedback_blueprint

api.register_blueprint(feedback_blueprint)
