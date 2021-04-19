"""
Connecting to DynamoDb running on AWS.
Creating table in DynamoDb running on AWS.
"""

# PSL
from typing import NoReturn

# Third part
import boto3

DB_CLIENT = boto3.client("dynamodb")
DB_OPERATOR = boto3.resource("dynamodb")


def create_rooms_table() -> NoReturn:
    if "rooms" not in DB_CLIENT.list_tables()["TableNames"]:
        DB_OPERATOR.create_table(
            TableName="rooms",
            KeySchema=[
                {"AttributeName": "room_key", "KeyType": "HASH"},
                {"AttributeName": "admin_nickname", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "room_key", "AttributeType": "S"},
                {"AttributeName": "admin_nickname", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
