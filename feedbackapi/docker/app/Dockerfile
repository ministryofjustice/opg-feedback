FROM python:3.9-alpine

RUN addgroup -S opgfeedback && \
    adduser -S -G opgfeedback opgfeedbackuser

WORKDIR /restapi

RUN apk update

RUN apk add git openssh build-base

COPY feedbackapi .

RUN cd /restapi && pip install -e .

USER opgfeedbackuser

EXPOSE 8005
CMD ["gunicorn", "opgfeedbackapi:api", "--bind", "0.0.0.0:8005", "--log-file", "-"]
