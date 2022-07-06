FROM python:3.9-alpine

RUN addgroup -S opgfeedback && \
    adduser -S -G opgfeedback opgfeedbackuser

WORKDIR /restapi

RUN apk update

RUN apk add git openssh build-base

RUN git clone --branch lpal-421-library-for-api https://github.com/ministryofjustice/opg-flask-apps.git

COPY rest-api .

RUN cd opg-flask-apps/flaskapi && pip install -e .

#RUN cd /restapi && python setup.py build && python setup.py install

RUN cd /restapi && pip install -e .

USER opgfeedbackuser

EXPOSE 8005
CMD ["gunicorn", "opgfeedbackapi:api", "--bind", "0.0.0.0:8005", "--log-file", "-"]
