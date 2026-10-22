from app import app

def test_home_page():
    app.testing = True
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Little Bloom Cafe" in response.data
    assert b"Cappuccino" in response.data

def test_menu_and_contact():
    app.testing = True
    client = app.test_client()

    response = client.get("/")

    assert b"Strawberry Cake" in response.data
    assert b"Cheese Sandwich" in response.data
    assert b"Pune, Maharashtra" in response.data