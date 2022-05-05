FROM 311462405659.dkr.ecr.eu-west-1.amazonaws.com/opg-flask-apps/rest-api:latest

WORKDIR /restapi

COPY rest-api .

# append extra routes onto the original routes.py from opg-flask-apps
RUN cat /rest-api/app/extra_routes.py >> /rest-api/app/routes.py

EXPOSE 8005
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8005", "--log-file", "-"]
