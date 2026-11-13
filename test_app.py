from app import app

def test_root():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert b"Welcome" in r.data

def test_health():
    r = app.test_client().get("/health")
    assert r.get_json() == {"status": "UP"}
