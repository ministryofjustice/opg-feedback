FROM python:3.9-alpine

RUN addgroup -S opgfeedback && \
    adduser -S -G opgfeedback opgfeedbackuser

WORKDIR /feedbackapi

RUN apk update

#i git is required to pip install feedback api as it has a depedency on a git repo
RUN apk add git

COPY feedbackapi .

RUN cd /feedbackapi && pip install -e .

RUN apk del git

USER opgfeedbackuser

EXPOSE 8005
CMD ["gunicorn", "opgfeedbackapi:api", "--bind", "0.0.0.0:8005", "--log-file", "-"]
