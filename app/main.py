from flask import Blueprint

main = Blueprint('main', __name__)

@main.get('/')
def hello_world():
    return 'hello world'