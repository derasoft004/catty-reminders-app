def test_app_import():
    from app.main import app
    assert app is not None

def test_app_has_routes():
    from app.main import app
    assert len(app.routes) > 0

