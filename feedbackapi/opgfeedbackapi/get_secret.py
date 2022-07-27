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


def get_secret():
    secret_name = "opg-flask-api-token"
    client = get_client()

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            print("The requested secret " + secret_name + " was not found")
        elif e.response["Error"]["Code"] == "InvalidRequestException":
            print("The request was invalid due to:", e)
        elif e.response["Error"]["Code"] == "InvalidParameterException":
            print("The request had invalid params:", e)
        elif e.response["Error"]["Code"] == "DecryptionFailure":
            print(
                "The requested secret can't be decrypted using the provided KMS key:", e
            )
        elif e.response["Error"]["Code"] == "InternalServiceError":
            print("An error occurred on service side:", e)
    else:
        print("found the secret string")
        if "SecretString" in get_secret_value_response:
            secret_data = get_secret_value_response["SecretString"]
        else:
            secret_data = get_secret_value_response["SecretBinary"]
    return secret_data


if __name__ == "__main__":
    get_secret()
