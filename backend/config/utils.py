from importlib import import_module

from django.conf import settings
from django.http import HttpRequest


def create_request_object():
    request = HttpRequest()
    engine = import_module(settings.SESSION_ENGINE)
    session_key = None
    request.session = engine.SessionStore(session_key)

    return request