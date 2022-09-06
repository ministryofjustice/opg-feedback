from flask import Blueprint, render_template
from flask import jsonify
from flask import current_app
import logging

feedbackfront_blueprint = Blueprint("feedbackfront_blueprint", __name__)


@feedbackfront_blueprint.route("/completed-feedback")
def feedback():
    return render_template("feedback.html")
