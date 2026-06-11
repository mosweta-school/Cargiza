from services.auth_service import AuthService
from storage.fake_json_repository import FakeRepository



def test_register_and_login():
    repo = FakeRepository()
    auth = AuthService(repo)

    user = auth.register("testuser", "1234", "customer")

    assert user["username"] == "testuser"

    logged_in = auth.login("testuser", "1234")

    assert logged_in is not None
    assert logged_in["username"] == "testuser"

def test_duplicate_user_registration():
    repo = FakeRepository()
    auth = AuthService(repo)

    auth.register("testuser", "1234", "customer")

    result = auth.register("testuser", "9999", "customer")

    assert "error" in result

    assert "error" in result
def test_login_failure_wrong_password():
    repo = FakeRepository()
    auth = AuthService(repo)

    auth.register("testuser", "1234", "customer")

    result = auth.login("testuser", "wrongpass")

    assert result is None

def test_password_is_hashed():
    repo = FakeRepository()
    auth = AuthService(repo)

    user = auth.register("testuser", "1234", "customer")

    assert user["password"] != "1234"

def test_duplicate_user_error():
    repo = FakeRepository()
    auth = AuthService(repo)

    auth.register("john", "1234", "customer")
    result = auth.register("john", "9999", "customer")

    assert "error" in result