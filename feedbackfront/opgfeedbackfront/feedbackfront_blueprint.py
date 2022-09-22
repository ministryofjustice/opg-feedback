from flask import Blueprint, render_template

feedbackfront_blueprint = Blueprint("feedbackfront_blueprint", __name__)


@feedbackfront_blueprint.route("/completed-feedback")
def feedback():
    return render_template("feedback.html")
