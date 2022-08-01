import boto3
import os
from botocore.exceptions import ClientError


def get_client():
    sts = boto3.client(
        "sts",
        region_name="eu-west-1",
    )

    # the following relies upon AWS credentials being provided in the relevant env vars, for a role that has access to this particular secret
    client = boto3.client(
        "secretsmanager",
    )

    return client


def get_secret(secret_name="opg-flask-api-token"):
    client = get_client()

    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    if "SecretString" in get_secret_value_response:
        secret_data = get_secret_value_response["SecretString"]
    else:
        secret_data = get_secret_value_response["SecretBinary"]
    return secret_data


if __name__ == "__main__":
    get_secret()
