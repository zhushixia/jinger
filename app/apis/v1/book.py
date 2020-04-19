from app.libs.error_code import NotFound
from app.libs.redprint import Redprint

api = Redprint('book')

@api.route('/get')
def get_book():
    raise NotFound()