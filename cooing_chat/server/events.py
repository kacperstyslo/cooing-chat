"""
All cooing_chat events.
"""

# Third part
from flask import session
from flask_socketio import emit, join_room, leave_room

# Own
from cooing_chat import SOCKETIO


@SOCKETIO.on("joined", namespace="/chat")
def joined(message) -> None:
    """
    Method that informs already connected users about a new user who connect to the room.
    A status message is broadcast to all people in the room.
    """
    room = session.get("room_key")
    join_room(room)
    emit(
        "status", {"msg": session.get("user_nickname") + f" joined to the room: {room}"}, room=room
    )


@SOCKETIO.on("text", namespace="/chat")
def text(message) -> None:
    """
    Method that allows users to send messages.
    A status message is broadcast to all people in the room.
    """
    emit(
        "message",
        {"msg": session.get("user_nickname") + ": " + message["msg"]},
        room=session.get("room_key"),
    )


@SOCKETIO.on("left", namespace="/chat")
def left(message):
    """
    Sent by clients when they leave a room.
    A status message is broadcast to all people in the room.
    """
    room = session.get("room_key")
    leave_room(room)
    emit("status", {"msg": session.get("user_nickname") + f" has left the room: {room}"}, room=room)
