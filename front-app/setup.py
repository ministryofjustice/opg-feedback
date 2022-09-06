from setuptools import setup, find_packages

setup(
    name="opgfeedbackfront",
    version="1.0",
    description="Feedback plugins for flask app",
    install_requires=[
        "opgflaskfront @ git+https://github.com/ministryofjustice/opg-flask-apps.git@LPAL-922-flask-front#subdirectory=flaskfront",
        "flask_httpauth",
        "boto3",
    ],
    packages=[],
)
