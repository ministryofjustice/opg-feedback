import boto3
import os
from botocore.exceptions import ClientError


def assume_role_and_get_client():
    sts = boto3.client(
        "sts",
        region_name="eu-west-1",
    )

    if os.getenv("FEEDBACK_CI"):
        print(" starting, Assuming CI role")
        role_arn = "arn:aws:iam::050256574573:role/opg-lpa-ci"
    else:
        print(" starting, Assuming operator role")
        role_arn = "arn:aws:iam::050256574573:role/operator"

    result = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName="session1",
    )

    client = boto3.client(
        "secretsmanager",
        aws_access_key_id=result["Credentials"]["AccessKeyId"],
        aws_secret_access_key=result["Credentials"]["SecretAccessKey"],
        aws_session_token=result["Credentials"]["SessionToken"],
        region_name="eu-west-1",
    )

    return client


def get_secret():
    secret_name = "opg-flask-api-token"
    client = assume_role_and_get_client()

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
        # Secrets Manager decrypts the secret value using the associated KMS CMK
        # Depending on whether the secret was a string or binary, only one of these fields will be populated
        if "SecretString" in get_secret_value_response:
            secret_data = get_secret_value_response["SecretString"]
            print(secret_data)
        else:
            secret_data = get_secret_value_response["SecretBinary"]
    return secret_data


if __name__ == "__main__":
    get_secret()
