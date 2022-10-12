from flask import Blueprint, render_template
from .forms import (
    BankDetailsForm,
    CookiesForm,
    CreateAccountForm,
    KitchenSinkForm,
    SatisfactionForm,
)

feedbackfront_blueprint = Blueprint("feedbackfront_blueprint", __name__)


@feedbackfront_blueprint.route("/completed-feedback")
def feedback():
    return render_template("feedback.html")


@feedbackfront_blueprint.route("/forms/bank-details", methods=["GET", "POST"])
def bank_details():
    form = BankDetailsForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("index"))
    return render_template("bank_details.html", form=form)


@feedbackfront_blueprint.route("/forms/create-account", methods=["GET", "POST"])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("index"))
    return render_template("create_account.html", form=form)


@feedbackfront_blueprint.route("/forms/kitchen-sink", methods=["GET", "POST"])
def kitchen_sink():
    form = KitchenSinkForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("index"))
    return render_template("kitchen_sink.html", form=form)


@feedbackfront_blueprint.route("/forms/satisfaction", methods=["GET", "POST"])
def satisfaction():
    form = SatisfactionForm()
    if form.validate_on_submit():
        flash("Form successfully submitted", "success")
        return redirect(url_for("index"))
    return render_template("satisfaction.html", form=form)
