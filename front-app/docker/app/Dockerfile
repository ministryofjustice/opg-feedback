FROM python:3.9-alpine

RUN addgroup -S opgfeedback && \
    adduser -S -G opgfeedback opgfeedbackuser

WORKDIR /frontapp

RUN apk update

RUN apk add git openssh build-base

COPY front-app .

# placeholder for now. Line below will be uncommented as part of LPAL-422
#RUN cd /frontapp && pip install -e .

USER opgfeedbackuser

EXPOSE 8005
# placeholder for now, line below will be uncommented as part of LPAL-422
#CMD ["gunicorn", "opgfeedbackapi:api", "--bind", "0.0.0.0:8005", "--log-file", "-"]
