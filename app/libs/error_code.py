from werkzeug.exceptions import HTTPException

from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400
    error_code = 4004
    msg = "client is invalid"


class ParameterException(APIException):
    code = 400
    error_code = 1000


class DatabaseException(APIException):
    code = 400
    error_code = 4001
    msg = "查询数据库错误"


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'


