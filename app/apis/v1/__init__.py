from flask import Blueprint

from app.apis.v1 import book, user


def create_blueprint_v1():
    v1 = Blueprint('v1', __name__)
    book.api.register(v1, url_prefix='/book')
    user.api.register(v1, url_prefix='/user')
    return v1
