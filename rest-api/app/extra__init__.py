class Feedback(db.Model):
    __table_name__ = 'perf_feedback',
    id = db.Column('id', sa.Integer, primary_key=True),
    rating = db.Column('rating', sa.Integer, nullable=False),
    comment = db.Column('comment', sa.String(1200), nullable=False),
    datetime = db.Column('datetime', sa.DateTime(), nullable=False)
