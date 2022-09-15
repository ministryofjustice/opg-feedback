FROM python:3.9-alpine

RUN addgroup -S opgfeedback && \
    adduser -S -G opgfeedback opgfeedbackuser

WORKDIR /feedbackfront

RUN apk update

RUN apk add git openssh build-base

COPY feedbackfront .

RUN cd /feedbackfront && pip install -e .

USER opgfeedbackuser

EXPOSE 8005
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8005", "--log-file", "-"]
