# PSL
import types

# third part
from flask import Blueprint

SERVER_BLUEPRINT = Blueprint("server_blueprint", __name__)
ERROR_HANDLER_BLUEPRINT = Blueprint("error_handler_blueprint", __name__)


def class_route(self, rule, endpoint, **options):
    """
    This decorator allows to add routed to class view.
    :param self: any flask object that have `add_url_rule` method.
    :param rule: flask url rule.
    :param endpoint: endpoint name
    """

    def wrapper(cls):
        self.add_url_rule(rule, view_func=cls.as_view(endpoint), **options)
        return cls

    return wrapper


SERVER_BLUEPRINT.class_route = types.MethodType(class_route, SERVER_BLUEPRINT)

# Own
from . import routes, events
