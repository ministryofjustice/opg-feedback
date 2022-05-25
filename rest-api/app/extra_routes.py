import json
import os
import sys
#sys.path.append('/restapi/app')
from datetime import datetime
from flask import request
from feedback import Feedback

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

@app.route('/feedback')
def post_feedback():
  # create instance of Feedback object, save to db.  1st hardcode it, then take params
  feedback = Feedback(rating = 1, comment = "Very happy with the service", datetime = datetime.now())
  app.db.session.add(feedback)
  app.db.session.commit()
  return '', 201
