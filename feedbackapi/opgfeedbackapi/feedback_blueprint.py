from datetime import datetime
from flask import current_app, Blueprint, request
from .feedback import Feedback
import json

feedback_blueprint = Blueprint("feedback_blueprint", __name__)


@feedback_blueprint.route("/feedback", methods=["POST"])
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
