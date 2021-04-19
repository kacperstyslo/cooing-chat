"""
All cooing_chat endpoints.
"""

# PSL
from typing import NoReturn

# third part
from flask import make_response, session, redirect, render_template, url_for
from flask.views import MethodView

# Own
from . import SERVER_BLUEPRINT, ERROR_HANDLER_BLUEPRINT
from .forms import CurrentSession
from cooing_chat.services import rooms_manger


@SERVER_BLUEPRINT.route("/", methods=["GET", "POST"])
def index():
    """
    Start Page
    """
    return render_template("index.html"), 200


@SERVER_BLUEPRINT.class_route("/create-room", "create-room")
class RoomCreator(MethodView):
    ROOM_KEY: str = rooms_manger.generate_key().get("generated_key")

    def __init__(self) -> NoReturn:
        self.user_data = CurrentSession()

    def get(self):
        return (
            render_template(
                "create_room.html", form=self.user_data, generated_secret_key=RoomCreator.ROOM_KEY
            ),
            200,
        )

    def post(self):
        if (
            self.user_data.validate_on_submit()
            and self.user_data.user_nickname.data
            and rooms_manger.check_if_user_typed_correct_room_key(
                user_typed_room_key=self.user_data.room_key.data,
                generated_room_key=RoomCreator.ROOM_KEY,
            )
        ):
            rooms_manger.add_new_room(
                admin_nick=self.user_data.user_nickname.data,
                room_key=RoomCreator.ROOM_KEY,
                current_session=CurrentSession,
            )
            RoomCreator.ROOM_KEY = rooms_manger.generate_key().get("generated_key")
            return redirect(url_for(".render_cooing_chat"))
        return redirect(url_for("server_blueprint.create-room"))


@SERVER_BLUEPRINT.class_route("/connect-to-room", "connect-to-room")
class RoomConnector(MethodView):
    def __init__(self) -> NoReturn:
        self.user_data = CurrentSession()

    def get(self):
        return render_template("connect_to_room.html", form=self.user_data), 200

    def post(self):
        if (
            self.user_data.validate_on_submit()
            and rooms_manger.check_if_user_typed_correct_room_key(self.user_data.room_key.data)
        ):
            CurrentSession.add_to_session(
                user_nickname=self.user_data.user_nickname.data,
                room_key=self.user_data.room_key.data,
            )
            return redirect(url_for(".render_cooing_chat"))
        return redirect(url_for("server_blueprint.connect-to-room"))


@SERVER_BLUEPRINT.route("/cooing-chat")
def render_cooing_chat():
    """
    This method renders a functional chat for users.
    """
    return (
        render_template(
            "cooing_chat.html", name=session["user_nickname"], room=session["room_key"]
        ),
        200,
    )


@ERROR_HANDLER_BLUEPRINT.errorhandler(400)
def bad_request():
    """
    Bad request.
    """
    return make_response(render_template("400.html", title="400", content="Page not found."), 400)


@ERROR_HANDLER_BLUEPRINT.errorhandler(404)
def page_not_found(not_found):
    """
    Page not found.
    """
    return make_response(render_template("404.html", title="404", content="Page not found."), 404)


@ERROR_HANDLER_BLUEPRINT.errorhandler(500)
def server_error():
    """
    Internal server error.
    """
    return make_response(
        render_template("500.html", title="500", content="Internal server error."), 500
    )
