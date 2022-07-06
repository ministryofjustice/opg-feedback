import os
from opgflaskapi import create_flask_app
from .incomes_blueprint import incomes_blueprint

postgres_url = "postgresql://{}:{}@{}/{}".format(
    os.getenv("POSTGRES_USERNAME"),
    os.getenv("POSTGRES_PASSWORD"),
    os.getenv("POSTGRES_HOSTNAME"),
    os.getenv("POSTGRES_NAME"),
)

api = create_flask_app("feedback", postgres_url)

from .feedback_blueprint import feedback_blueprint

api.register_blueprint(incomes_blueprint)
api.register_blueprint(feedback_blueprint)