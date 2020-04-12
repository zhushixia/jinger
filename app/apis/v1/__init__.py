from flask import Blueprint

from app.apis.v1 import book, user, client, token


def create_blueprint_v1():
    v1 = Blueprint('v1', __name__)
    book.api.register(v1, url_prefix='/book')
    user.api.register(v1, url_prefix='/user')
    client.api.register(v1, url_prefix='/client')
    token.api.register(v1, url_prefix='/token')
    return v1
