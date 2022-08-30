FROM python:3.8-alpine

RUN apk upgrade

RUN apk add build-base

RUN pip install awscli psycopg2-binary sqlalchemy alembic

RUN alembic init alembic

COPY feedbackdb/ /app/

RUN apk del build-base

WORKDIR /app

CMD alembic upgrade head && python scripts/db/create_feedback_user.py
