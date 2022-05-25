FROM 311462405659.dkr.ecr.eu-west-1.amazonaws.com/opg-flask-apps/rest-api:latest

WORKDIR /restapi

COPY rest-api .

RUN cat /restapi/app/extra_routes.py >> /restapi/app/routes.py

RUN rm /restapi/app/extra_routes.py 

ENV PYTHONPATH="/restapi/app:/restapi:$PYTHONPATH"

EXPOSE 8005
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8005", "--log-file", "-"]
