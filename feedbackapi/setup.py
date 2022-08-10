from setuptools import setup, find_packages

setup(
    name="opgfeedbackapi",
    version="1.0",
    description="Feedback plugins for flask api",
    install_requires=[
        "opgflaskapi @ git+https://github.com/ministryofjustice/opg-flask-apps.git#subdirectory=flaskapi",
        "flask_httpauth",
        "boto3",
    ],
    packages=[],
)
