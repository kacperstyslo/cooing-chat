"""
Here cooing_chat store all services responsible for managing "rooms".
"""

# PSL
from string import ascii_uppercase
from random import randint
from typing import Dict, NoReturn

# Third part
from flask import flash
from boto3.dynamodb.conditions import Key

# Own
from cooing_chat.db import DB_OPERATOR

ROOMS_TABLE = DB_OPERATOR.Table("rooms")


def generate_key() -> Dict[str, str]:
    """
    This method just generate unique, seven characters room key.
    """
    characters_collections: str = ascii_uppercase + "@!#$0123456789"
    return {"generated_key": "".join([characters_collections[randint(0, 39)] for _ in range(8)])}


def check_if_user_typed_correct_room_key(user_typed_room_key: str, generated_room_key=None) -> bool:
    """
    This method checks if user or room admin typed correct room key.
    """
    if (
        generated_room_key == user_typed_room_key
        or ROOMS_TABLE.query(KeyConditionExpression=Key("room_key").eq(user_typed_room_key))[
            "Items"
        ]
    ):
        return True
    flash(f"{user_typed_room_key}", "error")


def add_new_room(**kwargs) -> NoReturn:
    """
    This method add new room into database. After that will redirect room admin to chat.
    """
    ROOMS_TABLE.put_item(
        Item={"room_key": kwargs["room_key"], "admin_nickname": kwargs["admin_nick"]}
    )
    kwargs["current_session"].add_to_session(
        user_nickname=kwargs["admin_nick"], room_key=kwargs["room_key"]
    )
