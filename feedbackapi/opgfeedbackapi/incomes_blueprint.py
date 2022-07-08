import json
from flask import request, jsonify, Blueprint

incomes_blueprint = Blueprint("incomes_blueprint", __name__)

incomes = [{"description": "salary", "amount": 5000}]


@incomes_blueprint.route("/incomes")
def get_incomes():
    return jsonify(incomes)


@incomes_blueprint.route("/incomes", methods=["POST"])
def add_income():
    incomes.append(request.get_json())
    return "", 204
