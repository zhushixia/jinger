from flask import request, jsonify
from wtforms import ValidationError

from app.libs.enums import ClientTypeEnums
from app.libs.error_code import ClientTypeError, DatabaseException
from app.libs.redprint import Redprint
from app.libs.response_code import RET
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_user():
    data = request.json
    form = ClientForm(data=data).validate_for_api()
    promise = {
        ClientTypeEnums.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return 'success'


def __register_user_by_email():
    form = UserEmailForm(data=request.json).validate_for_api()
    try:
        User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data
        )
    except Exception as e:
        raise DatabaseException()
