FROM 311462405659.dkr.ecr.eu-west-1.amazonaws.com/opg-flask-apps/front-app:latest

WORKDIR /frontapp

COPY front-app .

EXPOSE 8005
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8005", "--log-file", "-"]
