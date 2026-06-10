from services.auth_service import AuthService


def test_register_and_login():
    auth = AuthService()

    user = auth.register("testuser", "1234", "customer")

    assert user["username"] == "testuser"

    logged_in = auth.login("testuser", "1234")

    assert logged_in is not None
    assert logged_in["username"] == "testuser"