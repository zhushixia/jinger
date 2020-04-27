from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError
from flask_mail import Mail

app = create_app()
mail = Mail(app)


# @app.errorhandler(Exception)
# def framework_error(e):
#     """
#     flask 1.0以后有这个功能，前面的版本只能捕获特定的异常
#     # APIException
#     # HTTPException
#     # Exception
#     :param e:
#     :return:
#     """
#     if isinstance(e, APIException):
#         return e
#     if isinstance(e, HTTPException):
#         code = e.code
#         msg = e.description
#         error_code = 1007
#         return APIException(msg, code, error_code)
#     else:
#         # 调试模式的话返回具体的错误信息，否则返回json格式具体的错误
#         if not app.config['DEBUG']:
#             return ServerError()
#         else:
#             raise e


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=False)