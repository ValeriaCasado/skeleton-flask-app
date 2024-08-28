from app import create_app
import app as app_file
import pytest
import os

@pytest.fixture
def client(monkeypatch):

    # If environment variables are required, they need to be patched here
    os.environ["SOMEVAR"] = ''

    app = create_app()

    monkeypatch.setattr(app_file, 'before_request_function', lambda: None)

    client = app.test_client()

    with client, app.app_context():
        g = {}
        yield client