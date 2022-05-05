import json
import os

from flask import request

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204
