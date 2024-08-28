from flask import Flask

def before_request_function():
    print('Should not print in testing!')

def create_app():
    app = Flask(__name__)

    config = {
        "DEBUG": True,
        "SECRET_KEY": "secret",
        'SUPPORTED_ISSUERS': ['https://accounts.google.com']

    }
    app.config = app.config | config
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    app.before_request(lambda: before_request_function())

    from .main import main 
    app.register_blueprint(main, url_prefix='/main')

    return app