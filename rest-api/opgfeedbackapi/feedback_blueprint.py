from datetime import datetime
from flask import current_app, Blueprint
from .feedback import Feedback

feedback_blueprint = Blueprint("feedback_blueprint", __name__)


@feedback_blueprint.route("/feedback")
def post_feedback():
    # create instance of Feedback object, save to db.  1st hardcode it, then take params
    feedback = Feedback(
        rating=1, comment="Very happy with the service", datetime=datetime.now()
    )
    current_app.database.add(feedback)
    return "", 201
