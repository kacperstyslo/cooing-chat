"""
All cooing_chat forms.
"""
# PSL
from typing import NoReturn

# third part
from flask import session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField


class CurrentSession(FlaskForm):
    """
    This class stored all forms.
    """

    user_nickname = StringField("user_nickname", render_kw={"placeholder": "Type your nickname"})
    room_key = StringField("room_key", render_kw={"placeholder": "Type room key"})
    create_room_button = SubmitField("Create room!")
    connect_to_the_room_button = SubmitField("Connect to the room!")

    @staticmethod
    def add_to_session(**kwargs) -> NoReturn:
        """
        This method add typed by user: nickname, room key to session.
        """
        session["user_nickname"] = kwargs["user_nickname"]
        session["room_key"] = kwargs["room_key"]
