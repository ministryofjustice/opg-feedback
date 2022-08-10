import boto3
import os
from botocore.exceptions import ClientError


def get_client():

    if "LOCAL_AWS_ENDPOINT" in os.environ:
        # use localstack if instructed to by env var
        client = boto3.client(
            "secretsmanager",
            aws_access_key_id="accesskey",
            aws_secret_access_key="secretkey",
            region_name="eu-west-1",
            verify=False,
            endpoint_url=os.getenv("LOCAL_AWS_ENDPOINT"),
        )
    else:
        # the following relies upon AWS credentials being provided in the environment, for a role that has access to this particular secret
        client = boto3.client(
            "secretsmanager",
            region_name="eu-west-1",
        )

    return client


def get_secret(
    secret_name="opg-flask-api-token",
):
    client = get_client()

    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    if "SecretString" in get_secret_value_response:
        secret_data = get_secret_value_response["SecretString"]
    else:
        secret_data = get_secret_value_response["SecretBinary"]
    return secret_data


if __name__ == "__main__":
    get_secret()
