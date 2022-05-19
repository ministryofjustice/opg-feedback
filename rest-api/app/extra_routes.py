import json
import os
from datetime import datetime
from flask import request

class Feedback(app.db.Model):
    __tablename__ = 'perf_feedback'
    id = app.db.Column('id', app.db.Integer, primary_key=True, autoincrement=True)
    rating = app.db.Column('rating', app.db.Integer, nullable=False)
    comment = app.db.Column('comment', app.db.String(1200), nullable=False)
    datetime = app.db.Column('datetime', app.db.DateTime(), nullable=False)

    def __init__(self, rating, comment, datetime):
        self.rating = rating
        self.comment = comment
        self.datetime = datetime

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
