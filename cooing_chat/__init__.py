"""
Creating & registration all app components. From here app will start up.
"""

# Third part
from flask import Flask
from flask_socketio import SocketIO

# Own
from cooing_chat.db import create_rooms_table

SOCKETIO = SocketIO()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.Config")

    from .server import SERVER_BLUEPRINT, ERROR_HANDLER_BLUEPRINT

    app.register_blueprint(SERVER_BLUEPRINT)
    app.register_blueprint(ERROR_HANDLER_BLUEPRINT)

    SOCKETIO.init_app(app)
    create_rooms_table()
    return app
