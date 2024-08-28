from . import client

def test_main(client):
    r = client.get('/main')