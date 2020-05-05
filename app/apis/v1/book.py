
from flask_mail import Message
from app.libs.redprint import Redprint

api = Redprint('book')

@api.route('/get')
def get_book():
    msg = Message('test', sender="15868407338@163.com", recipients=["15868407338@163.com"])
    from jinger import mail
    mail.send(msg)
    return 'ok'
    # send_async_email(a)
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
#
# def send_email(to, subject, template, image, **kwargs):
#     app = current_app._get_current_object()
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
#                   sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     # msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#
#     with app.open_resource(image) as fp:
#         msg.attach('image.png', "image/png", fp.read(), 'inline', headers=[('Content-ID', 'image')])
#
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr