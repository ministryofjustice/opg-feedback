from datetime import datetime
from app import app

class Feedback(app.db.Model):
    __tablename__ = 'perf_feedback'
    id = app.db.Column('id', app.db.Integer, primary_key=True, autoincrement=True)
    rating = app.db.Column('rating', app.db.Integer, nullable=False)
    comment = app.db.Column('comment', app.db.String(1200), nullable=False)
    datetime = app.db.Column('datetime', app.db.DateTime(), nullable=False)

