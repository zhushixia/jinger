from flask import Flask



def register_blueprints(ap):
    from app.apis.v1 import create_blueprint_v1
    ap.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

def register_plugin(ap):
    from app.models.base import db
    db.init_app(ap)
    with ap.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprints(app)
    register_plugin(app)
    return app
