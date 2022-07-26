from datetime import datetime
from flask import current_app, Blueprint, request
from flask_httpauth import HTTPTokenAuth
from .feedback import Feedback
from .get_secret import get_secret
import json

auth = HTTPTokenAuth(scheme="Bearer")
feedback_blueprint = Blueprint("feedback_blueprint", __name__)

# TODO DO NOT MERGE - next coding step is to get the token from AWS secretsmanager
tokens = {"secret-token-1": "john", "secret-token-2": "susan"}
# tokens = get_secret()


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


@feedback_blueprint.route("/feedback", methods=["POST"])
@auth.login_required
def post_feedback():
    # create instance of Feedback object, save to db.
    content_type = request.headers.get("Content-Type")
    if content_type != "application/json":
        return "Content-Type needs to be json", 400

    data = json.loads(request.data)

    if not ("comment" in data and "rating" in data):
        return "Missing data", 400

    feedback = Feedback(
        rating=data["rating"], comment=data["comment"], datetime=datetime.now()
    )
    current_app.database.add(feedback)
    return "", 201
