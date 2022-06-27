from datetime import datetime
from flask import current_app


class Feedback(current_app.db.Model):
    __tablename__ = "perf_feedback"
    id = current_app.db.Column(
        "id", current_app.db.Integer, primary_key=True, autoincrement=True
    )
    rating = current_app.db.Column("rating", current_app.db.Integer, nullable=False)
    comment = current_app.db.Column(
        "comment", current_app.db.String(200), nullable=False
    )
    datetime = current_app.db.Column(
        "datetime", current_app.db.DateTime(), nullable=False
    )
