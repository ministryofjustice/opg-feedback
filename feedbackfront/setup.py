from setuptools import setup, find_packages

setup(
    name="opgfeedbackfront",
    version="1.0",
    description="Feedback plugins for flask app",
    install_requires=[
        "opgflaskfront @ git+https://github.com/ministryofjustice/opg-flask-apps.git#subdirectory=flaskfront",
        "govuk-frontend-wtf>=0.3.0",
        "gunicorn>=20.1.0,<21",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
        ],
    },
    packages=["opgfeedbackfront"],
    include_package_data=True,
)
