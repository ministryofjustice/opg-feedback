from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Feedback(Base):
    __tablename__ = "perf_feedback"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    rating = Column("rating", Integer, nullable=False)
    comment = Column("comment", String(200), nullable=False)
    datetime = Column("datetime", DateTime(), nullable=False)
