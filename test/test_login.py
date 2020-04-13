def test_login(app):
    app.session.login("9400000110","QqWwE!1")
    assert app.session.is_logged_in_as("9400000110")