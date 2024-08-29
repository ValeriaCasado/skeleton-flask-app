from flask import Flask, g
from flask_oidc import OpenIDConnect

def before_request_function():
    print('Should not print in testing!')

def create_app():
    app = Flask(__name__)

    config = {
        "DEBUG": True,
        "SECRET_KEY": "secret",
        'SUPPORTED_ISSUERS': ['accounts.google.com']

    }
    app.config = app.config | config
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"
    app.config["OIDC_CLIENT_SECRETS"] = ''

    app.before_request(lambda: before_request_function())

    from .main import main 
    app.register_blueprint(main, url_prefix='/main')

    # oidc = OpenIDConnect(app)

    return app