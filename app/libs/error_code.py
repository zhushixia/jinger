from werkzeug.exceptions import HTTPException

from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400
    error_code = 9999
    msg = "client is invalid"